import sys, time, os
#init Class
from classes.zip import Zipped
Zipped = Zipped()

def log(msg):
    currenttime = time.strftime("%H:%M:%S")
    sys.stdout.write("[%s] %s\n" % (currenttime, str(msg)))
    sys.stdout.flush()

#Mode
Auto    = True

#Common Places
BOTS = {}
if os.name == 'nt':
    USERNAME                =   os.getenv('username')
    BOTS["ANB AIO"]         =   "C:\Program Files (x86)\AIO Bot"
    BOTS["YCOPP"]           =   "C:\Users\%s\AppData\Local\yCopp\UltimateAdidasBot" % (USERNAME)
    BOTS["SUPREME SLAYER"]  =   "C:\Program Files (x86)\SupremeSlayer"
    BOTS["SOLE SLAYER"]     =   "C:\Program Files (x86)\SoleSlayer"
    BOTS["TheSnkrsBot"]     =   "C:\Users\%s\Downloads\TheSnkrsBot\%shesnkrsbot"    % (USERNAME,"t")

    i = 0
    for BOT in BOTS:
         log("Choice: %d Bot: %s" % (i, BOT))
         i += 1
elif os.name == 'nt':
    log("No Bot's Path Loaded for your OS.")

try:
    sys.argv[1]
except IndexError:
    log("Auto Mode Enabled!!")
    Auto = True

if Auto == False:
    DIR_TO_ZIP = sys.argv[1]

if Auto == True:

    DIR_TO_ZIP = raw_input("Enter Full Path You Wish To ZIP. Check readme for help. ")

    if DIR_TO_ZIP == "0":
        DIR_TO_ZIP = BOTS["SOLE SLAYER"]

    if DIR_TO_ZIP == "1":
        DIR_TO_ZIP = BOTS["YCOPP"]

    if DIR_TO_ZIP == "2":
        DIR_TO_ZIP = BOTS["SUPREME SLAYER"]

    if DIR_TO_ZIP == "3":
        DIR_TO_ZIP = BOTS["TheSnkrsBot"]

    if DIR_TO_ZIP == "4":
        DIR_TO_ZIP = BOTS["ANB AIO"]



CURRENT_DIR = raw_input("Enter Zip Name ") + '.zip'



log("Zipping Directory [ %s ] to Current Directory [ %s ]" % (DIR_TO_ZIP,CURRENT_DIR))

Zipped.zipdir(CURRENT_DIR, DIR_TO_ZIP)

