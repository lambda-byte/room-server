# why not do this instead of a shell script

import os

print("starting server")

# for this command you have to use sudo. not a good idea but this is not prod anyways.

username=os.system("whoami")
if username is not "root":
    print ("You aren't root. This script cant use port 80 otherwise.")
    exit()

# run if in root

os.system("flask run --host 0.0.0.0 --port 80")

# profit? 
