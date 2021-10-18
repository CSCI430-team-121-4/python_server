#!/bin/bash

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
# install pip
sudo apt install python3-pip

# install flask
sudo pip3 install -i https://fbsd-build.isi.deterlab.net/pypi/web/simple flask
sudo pip3 install -i https://fbsd-build.isi.deterlab.net/pypi/web/simple flask-mysqldb
sudo pip3 install -i https://fbsd-build.isi.deterlab.net/pypi/web/simple uuid