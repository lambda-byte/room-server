# setup.py made by lambda
# this is super wacky code
# this will prob only work on a debian or debian based distro
# please learn from my pain and suffering.
# this code also completely opts out from using a virtualenv
# you also need to run this with sudo lol


import os, subprocess

subprocess.run(["apt", "install", "postgresql", "postgresql-client", "libpq-dev", "python3-dev", "-y"])