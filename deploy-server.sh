#!/bin/bash

# install pip
sudo apt install python-pip

# install mysql
sudo apt-get install mysql-server
sudo apt install libmysqlclient-dev

# install flask and mysql Python libraries
sudo pip install -i https://fbsd-build.isi.deterlab.net/pypi/web/simple flask mysql flask_mysqldb

# run server code
sudo python app.py