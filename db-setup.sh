#!/bin/bash

# make db user
sudo -u postgres psql -c "CREATE USER roomsql WITH PASSWORD 'room-pass';"

# drop existing db
sudo -u postgres psql -c "DROP DATABASE roomdb;"

# make db 
sudo -u postgres psql -c "CREATE DATABASE roomdb OWNER roomsql;"