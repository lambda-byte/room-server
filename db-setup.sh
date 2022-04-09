#!/bin/bash


sudo -u postgres psql -c "CREATE USER roomsql WITH PASSWORD 'room-pass';"
