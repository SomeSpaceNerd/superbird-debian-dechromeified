#!/bin/bash
# Start X with just a single fullscreen program
#	fullscreen, kiosk mode, tweaked for touchscreen, with given url

source /scripts/run_on_start_settings.sh

## Hardcoded Vars you dont need to mess with
USER_DATA_DIR="/config"
DISK_CACHE_DIR="/dev/null"  # prevent chromium from caching anything

# log this script's actions to a file
exec 1>/var/log/run_on_start.log 2>&1

echo "Starting fullscreen kiosk"

command -v "$PROGRAM_BINARY" >/dev/null || {
	echo "Program not found!"
	exit 1
}

/scripts/setup_display.sh

# does not get cleaned up properly after previous exit
rm ${USER_DATA_DIR}/SingletonLock

# get current resolution so we can match it
#	if you don't set --window-size, chromium will go almost-fullscreen, about 10px shy on all sides
#	if you don't set --window-position, chromium will start at about 10,10 instead of 0,0
#	why does chromium do this??!?!
# here we detect resolution by briefly starting X11 and then parsing output of xrandr
#	this is simpler and more reliable than parsing xorg.conf
#	by avoiding a hardcoded resolution here, we only need to make changes in xorg.conf if we want to change resolution or rotate

echo "Briefly starting X11 in order to detect configured resolution"
DISP_REZ=$(xinit /usr/bin/xrandr 2>/dev/null|grep "\*"|awk '{print $1}'|tr 'x' ',')
echo "Detected resolution: $DISP_REZ"

PROGRAM_CMD="xinit $PROGRAM_BINARY \ --$EXTRA_XORG_ARGS \ --$EXTRA_PROGRAM_ARGS"

echo ""
echo "running kiosk command: $PROGRAM_CMD"
echo ""
$PROGRAM_CMD

# clear the display after the program is killed, otherwise the last image will remain frozen
/scripts/clear_display.sh
