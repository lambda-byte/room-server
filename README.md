# room-server
WIP: put a docker action image here at some point i guess.

## What is this?
A fork of room-server. made for the kicks and whatnot.

## Running

#### Only do this in a dev environment. 

1. Make a Debian vm.

2. Setup sudo and ssh if you need to.

3. Run this script to install the server and setup the database.
```
python3 install.py
```

4. Run this script to start the server
```
python3 startup.py
```

## Manual Setup

1. You'll most likely want to [create a virtualenv](https://docs.python.org/3/library/venv.html) to install things. For example:
```
python3 -m venv virtualenv
```
Ensure you activate the environment.

2. Regardless of the above, ensure you have installed requirements:
```
pip3 install -r requirements.txt
# Useful for reading .flaskenv.
pip3 install python-dotenv
```

3. You'll then need to install PostgreSQL. Copy `config-example.py` to `config.py` and update this config.

Also WIP: Make a script that makes the database

4. Read `conf/README.md` for instructions of static files you should provide.

5. WIP.

6. You will now be able to visit The Underground (http://root_domain/theunderground). The default username is `admin`, and password `admin`.
It's highly advised to change it as soon as possible.
