#!/bin/bash

# switch to Python 3
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# install pip
sudo apt install python-pip3

# install mysql
sudo apt-get install mysql-server
sudo apt install libmysqlclient-dev

# install flask and mysql Python libraries
sudo pip3 install -i https://fbsd-build.isi.deterlab.net/pypi/web/simple flask mysql flask_mysqldb

# run server code
sudo python3 app.py