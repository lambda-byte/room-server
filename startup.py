# why not do this instead of a shell script

# import things

import subprocess


print("starting server")

# for this command you have to use sudo. not a good idea but this is not prod anyways.

try:
    subprocess.run(['flask run --host 0.0.0.0 --port 80'], check = True)
except subprocess.CalledProcessError:
    print ('Run failed. Install flask')

# profit? 