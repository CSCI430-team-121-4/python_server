-- change login to use password instead of auth_socket
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'ZEw2Uk2+merS@uQa';
-- then flush privileges to tell server to reload grant tables and use new changes
FLUSH PRIVILEGES;
exit