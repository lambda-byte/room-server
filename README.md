# room-server
[![Push Docker image](https://github.com/lambda-byte/room-server/actions/workflows/push_docker_image.yml/badge.svg)](https://github.com/lambda-byte/room-server/actions/workflows/push_docker_image.yml)

## What is this?
A fork of room-server. made for the kicks and whatnot.

## Setup


1. Make a Debian vm.

2. Install sudo 
```
apt install sudo
```

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


4. Read `conf/README.md` for instructions of static files you should provide.

5. Finally, start the server:
```
flask run --host 0.0.0.0
```

6. You will now be able to visit The Underground (http://root_domain/theunderground). The default username is `admin`, and password `admin`.
It's highly advised to change it as soon as possible.
