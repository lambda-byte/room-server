# why not do this instead of a shell script

import os



# Terrible code that will only work on linux systems. Should be moved to subprocess asap 

username=os.system("whoami > /dev/null")
if username != "root":
    print ("You aren't root. This script cant use port 80 otherwise.")
    exit()

# run if in root

print("starting server")
os.system("flask run --host 0.0.0.0 --port 80")

# profit? 
