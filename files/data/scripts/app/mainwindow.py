# This Python file uses the following encoding: utf-8
import sys
import os
import struct
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QTimer, QThread, Signal
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *

# Import the generated UI class
from ui_form import Ui_MainWindow

# Device paths
DEV_BUTTONS = '/dev/input/event0'
DEV_KNOB = '/dev/input/event1'

# Button code map
BUTTONS_CODE_MAP = {
    2: 'Button1',
    3: 'Button2',
    4: 'Button3',
    5: 'Button4',
    50: 'MenuButton',
    28: 'Button5',
}

# Knob direction codes
KNOB_LEFT = 4294967295  # actually -1 but unsigned int so wraps around
KNOB_RIGHT = 1

# Input event format: timeval (2x long), type (unsigned short), code (unsigned short), value (int)
EVENT_FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

# Subclassing OpenGLDemo to implement the OpenGL rendering
class OpenGLDemo(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

        # Timer to update the cube's rotation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_rotation)
        self.timer.start(16)  # Approximately 60 FPS

    def initializeGL(self):
        glClearColor(0.1, 0.1, 0.1, 1.0)  # Set background color
        glEnable(GL_DEPTH_TEST)  # Enable depth testing for 3D

    def resizeGL(self, w, h):
        aspect_ratio = w / h if h != 0 else 1
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, aspect_ratio, 1, 100)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)  # Move the cube into the screen
        glRotatef(self.angle_x, 1.0, 0.0, 0.0)  # Rotate around X-axis
        glRotatef(self.angle_y, 0.0, 1.0, 0.0)  # Rotate around Y-axis
        glRotatef(self.angle_z, 0.0, 0.0, 1.0)  # Rotate around Z-axis
        self.draw_cube()

    def draw_cube(self):
        glBegin(GL_QUADS)

        # Front face (red)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)

        # Back face (green)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)

        # Top face (blue)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)

        # Bottom face (yellow)
        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)

        # Right face (magenta)
        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)

        # Left face (cyan)
        glColor3f(0.0, 1.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)

        glEnd()

    def update_rotation(self):
        self.angle_x += 1  # Increment the angle around the X-axis
        self.angle_y += 1  # Increment the angle around the Y-axis
        self.angle_z += 1  # Increment the angle around the Z-axis
        self.angle_x %= 360
        self.angle_y %= 360
        self.angle_z %= 360
        self.update()

# Thread to handle button events
class ButtonEventThread(QThread):
    button_pressed = Signal(int, bool)  # Signal to emit when a button is pressed (code, is_pressed)

    def __init__(self):
        super().__init__()
        self.device_file = None

    def run(self):
        self.device_file = os.open(DEV_BUTTONS, os.O_RDONLY | os.O_NONBLOCK)
        try:
            while True:
                event = os.read(self.device_file, EVENT_SIZE)
                if len(event) == EVENT_SIZE:
                    _, _, event_type, code, value = struct.unpack(EVENT_FORMAT, event)
                    if event_type == 1:  # EV_KEY type
                        is_pressed = value == 1  # Key press event
                        self.button_pressed.emit(code, is_pressed)
        finally:
            if self.device_file:
                os.close(self.device_file)

# Worker thread to handle knob events
class KnobEventThread(QThread):
    knob_turned = Signal(int)  # Signal to emit when the knob is turned (value)

    def __init__(self):
        super().__init__()
        self.device_file = None

    def run(self):
        self.device_file = os.open(DEV_KNOB, os.O_RDONLY | os.O_NONBLOCK)
        try:
            while True:
                event = os.read(self.device_file, EVENT_SIZE)
                if len(event) == EVENT_SIZE:
                    _, _, event_type, code, value = struct.unpack(EVENT_FORMAT, event)
                    if event_type == 2 and code == 7:  # EV_REL type and REL_DIAL code
                        self.knob_turned.emit(value)
        finally:
            if self.device_file:
                os.close(self.device_file)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.opengl_widget = OpenGLDemo(self.ui.OpenGL_Demo)
        self.opengl_widget.setGeometry(self.ui.OpenGL_Demo.geometry())
        self.ui.OpenGL_Demo.setParent(None)
        self.opengl_widget.setParent(self)

        self.button_thread = ButtonEventThread()
        self.button_thread.button_pressed.connect(self.update_button_label)
        self.button_thread.start()

        self.knob_thread = KnobEventThread()
        self.knob_thread.knob_turned.connect(self.update_knob_label)
        self.knob_thread.start()

        self.setup_ui()

    def setup_ui(self):
        self.button_labels = {
            'Button1': self.findChild(QLabel, "button1"),
            'Button2': self.findChild(QLabel, "button2"),
            'Button3': self.findChild(QLabel, "button3"),
            'Button4': self.findChild(QLabel, "button4"),
            'Button5': self.findChild(QLabel, "button5"),
            'MenuButton': self.findChild(QLabel, "MenuButton"),
        }
        self.knob_label = self.findChild(QLabel, "Knob")

    def update_button_label(self, code, is_pressed):
        button_name = BUTTONS_CODE_MAP.get(code)
        if button_name and button_name in self.button_labels:
            self.button_labels[button_name].setStyleSheet("background-color: lightgreen;" if is_pressed else "")

    def update_knob_label(self, value):
        if value == KNOB_LEFT:
            self.knob_label.setText("LEFT")
        elif value == KNOB_RIGHT:
            self.knob_label.setText("RIGHT")
        else:
            self.knob_label.setText(str(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
