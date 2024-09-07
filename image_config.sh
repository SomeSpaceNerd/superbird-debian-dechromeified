#!/usr/bin/env bash

# Shared config for image scripts
# shellcheck disable=SC2034

# where to find an existing superbird device dump, to use for creating a debian image
EXISTING_DUMP="./dumps/debian_current"

# Network info
HOST_NAME="superbird"
USBNET_PREFIX="192.168.7"  # usb network will use .1 as host device, and .2 for superbird

# User info
USER_NAME="superbird"
# generate hash: openssl passwd -6 "superbird"
#   shellcheck disable=SC2016
USER_PASS_HASH='$6$zeM8ZwO/Xke05h6X$UtmM0sIBznj4hxmd/UGUO1YHUr0emOn.9u7G1yQRVGR4XutYCstDzVLzpUw9PNWrhYRAEg73ovkC4JNPFlSmI1'

# config for debootstrap
ARCHITECTURE="arm64"
DISTRO_REPO_URL="http://deb.debian.org/debian/"
DISTRO_BRANCH="trixie"
DISTRO_VARIANT="minbase"

# you can add extra packages here to install during stage 2
#   will be installed like this (in chroot): apt install -y --no-install-recommends --no-install-suggests $EXTRA_PACKAGES
EXTRA_PACKAGES="libxfce4ui-utils thunar xfce4-appfinder xfce4-panel xfce4-session xfce4-settings xfce4-terminal xfconf xfdesktop4 xfwm4 shared-mime-info python3.12 python3.12-venv python3.12-minimal"

# timezone and locale
TIMEZONE="America/Los_Angeles"
LOCALE="en_US.UTF-8"

# directory for FTP server
FTP_DIR="/ftp/"
