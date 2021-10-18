-- will create new user with specific privileges
CREATE USER 'server-user'@'localhost' IDENTIFIED BY '[-pBthX#-7Qkq#kZ';

GRANT ALTER, ALTER ROUTINE, CREATE ROUTINE, CREATE, DELETE, DROP, EVENT, EXECUTE, INDEX, INSERT, SELECT, UPDATE ON csci430.* TO 'server-user'@'localhost';

-- will require password for root user
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'ZEw2Uk2+merS@uQa';

FLUSH PRIVILEGES;
