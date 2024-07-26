# FTP file transfer script

import ftplib
from ftp_settings import USERNAME, PASSWORD, USBNET_PREFIX, TEMP_DIR

HOSTNAME = f"{USBNET_PREFIX}.1"
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
ftp_server.encoding = "utf-8"

if ftp_server.retrlines("LIST") != None:
    main = "thread" #placeholder main thread to prevent syntax error
else:
    print("FTP Server directory is empty, check host")
    exit()