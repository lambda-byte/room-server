# setup.py made by lambda
# this is super wacky code
# this will prob only work on a debian or debian based distro
# please learn from my pain and suffering.

import os, subprocess

subprocess.run(["apt", "install", "postgresql postgresql-client", ""])