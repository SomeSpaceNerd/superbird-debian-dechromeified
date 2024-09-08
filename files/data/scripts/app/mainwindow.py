# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *

# Import the generated UI class
from ui_form import Ui_MainWindow


# Subclassing OpenGL_Demo to implement the OpenGL rendering
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


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Replace OpenGL_Demo with the OpenGLDemo widget
        self.opengl_widget = OpenGLDemo(self.ui.OpenGL_Demo)
        self.opengl_widget.setGeometry(self.ui.OpenGL_Demo.geometry())
        self.ui.OpenGL_Demo.setParent(None)
        self.opengl_widget.setParent(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
