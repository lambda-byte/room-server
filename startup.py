# why not do this instead of a shell script
import os

print("starting server")

# for this command you have to use sudo. not a good idea but this is not prod anyways.
os.system("flask run --host 0.0.0.0 --port 80")

# profit? 
