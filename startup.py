# why not do this instead of a shell script

import os, subprocess


print("starting server")

subprocess.run(["systemctl", "start", "postgresql"])
subprocess.run(["flask", "run", "--host", "0.0.0.0"])

# profit? 
