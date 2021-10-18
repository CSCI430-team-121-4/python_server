#!/bin/sh
sudo apt install mysql-server
#Do you want to continue
Y
#run security script
sudo mysql_secure_installation
# enables validate password plugin
y
# password validation policy (1 = MEDIUM)
1
#new password
ZEw2Uk2+merS@uQa
ZEw2Uk2+merS@uQa
# do you wish to proceed with the password provided
y
# remove anonymous users
y
# disallow root login remotely
y
# remove test database
y
# reload privilege tables now
y
# ALL DONE! now adjust user authentification and Privileges
