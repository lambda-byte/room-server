# why not do this instead of a shell script

import os

print("starting server")

# Terrible code that will only work on linux systems. Should be moved to subprocess asap 

username=os.system("whoami > /dev/null")
if username is not "root":
    print ("You aren't root. This script cant use port 80 otherwise.")
    exit()

# run if in root

os.system("flask run --host 0.0.0.0 --port 80")

# profit? 
