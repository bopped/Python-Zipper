import sys, time, os

from classes.zip import Zipped
Zipped = Zipped()

def log(msg):
    currenttime = time.strftime("%H:%M:%S")
    sys.stdout.write("[%s] %s\n" % (currenttime, str(msg)))
    sys.stdout.flush()

Auto = True


try:
    sys.argv[1]
except IndexError:
    log("Auto Mode Enabled!!")
    Auto = False

if Auto == True:
    DIR_TO_ZIP = sys.argv[1]
ANBPATH = "C:\Program Files (x86)\AIO Bot"
if Auto == False:
    DIR_TO_ZIP = raw_input("Enter Full Path You Wish To ZIP. Check readme for help. ")
    if DIR_TO_ZIP == "1":
        DIR_TO_ZIP = ANBPATH


CURRENT_DIR = raw_input("Enter Zip Name ") + '.zip'



log("Zipping Directory [ %s ] to Current Directory [ %s ]" % (DIR_TO_ZIP,CURRENT_DIR))

Zipped.zipdir(CURRENT_DIR, DIR_TO_ZIP)

