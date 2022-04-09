# why not do this instead of a shell script

# import things

import os, subprocess


print("starting server")


# this is stupid but it works
class NotSudo(Exception):
    pass

if os.getuid() != 0:
    raise NotSudo("You need superuser perms to run this. Port 80 wont be allocated otherwise.")


try:
    subprocess.run(['flask run --host 0.0.0.0 --port 80'], check = True)
except subprocess.CalledProcessError:
    print ('Run failed. Install flask.')

# profit? 