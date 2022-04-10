# install.py made by lambda
# this is super wacky code
# this will only work on a debian or debian based distro
# please learn from my pain and suffering.
# this code also completely opts out from using a virtualenv
# you also need to run this with sudo lol

# imports
import subprocess, time, os

print("This is the dev install script. Dont use this in a production environment.")    
time.sleep(1)

# sanity check
ask = input('Warning. This installer will overwrite any existing room-server database files. Would you like to proceed?\n: ')
if ask in ["yes", "Yes", "Y", "y"]:
    print("Ok. Starting install")
    time.sleep(1)
else:
  quit()


# install cool things
subprocess.run(["apt", "install", "postgresql", "postgresql-client", "libpq-dev", "python3-dev", "pip" "-y"])

# make sql run
subprocess.run(["systemctl", "enable", "postgresql"])

subprocess.run(["systemctl", "start", "postgresql"])

subprocess.run(["./db-setup.sh"])

# pip stuff
subprocess.run(["pip3 install -r requirements.txt"])

# check if config.py is a thing. if so change the name so the code below it can work
if os.path.exists("config.py"):
    subprocess.run(["mv", "config.py", "config-defaults.py"])


domain = input("Enter the root domain you want in quotes: ")

string = "\nroot_domain = {}".format(domain)

with open("config-defaults.py", "a") as f:
    f.write(string)


subprocess.run(["mv", "config-defaults.py", "config.py"])

print("Install Done! Now just run startup.py")