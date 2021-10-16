import mysql
import json
import bcrypt
from random import randint
from time import sleep

# Make a json file named sqlconfig.txt, it will have these values
#  
# user = username, database = insert database name here
# sslkey = key file name here
# sslca = sslcafile
# ssl_verify_identity = True, 
# port = portnumber here, password = passw here 
# ssl_verify_cert = True

class SqlHandler:
    conn = None 
    config = None
    def __init__(self, file = 'sqlconfig.txt'):
        self.__setConfigData__(file)
        self.conn = mysql.connector.connect(**self.config)

    def __setConfigData__(self, f):
        self.config = json.load(f)

    def register(self, username, password, ipaddress):
        ''' 
            1) check if username already exists, if it does throw exception
            2) if not, generate salt
            3) add salt to password
            4) hash password
            5) add username, hashed password, non-hashed ip to database
            6) create session for this user, return user object by using getUserByCookie
        '''
        ######## Bullet point 1 #########
        rows = self.__getUsername__(username)
        if rows is not None:
            raise Exception('Username already exists')
        
        ######## Bullet point 2 #########
        salt = self.__generateSalt__()

        ######## Bullet point 3 and 4 #########
        hashedpw = bcrypt.hash(password, salt)

        ######## Bullet point 5 #########
        try:
            self.__addUser__(username, hashedpw, salt, ipaddress)
        except Exception as identifier:
            print('Could not add user due to a sql issue')
            print(identifier)
            raise mysql.connector.DatabaseError('Sql error, please check the connection')
        
        ######## Bullet point 6 #########
        hashedCookieID = self.__createSession__(username, ipaddress)
        return getUserByCookie(hashedCookieID, ipaddress)

        

    
    def login(self, username, password, ipaddress):
        ''' 
            0) delay a small, random amount of time
            1) check if username already exists, if not, throw exception
            2) if it does, get the user's salt
                hashed_password = rows[0] 
            3) add salt to password
            4) hash password
            5) check that the two hashes match, if not, throw exception
               check_match = bcrypt.checkpw(password, hashed_password)
            6) create session for this user, return user object by using getUserByCookie
        '''
        ######## Bullet point 0 and 1 #########
        sleep(0.001 * randint(10,100))

        rows = self.__getUsername__(username)
        if rows is None:
            raise Exception('Invalid Login')
            
        ######## Bullet point 2 #########
        salt = rows.get('salt')

        ######## Bullet point 3, 4, and 5 #########
        hashedattempt = bcrypt.hash(password, salt)
        hashedpw = rows.get('hash')
        if hashedpw != hashedattempt:
            raise Exception('Invalid Login')
        
        ######## Bullet point 6 #########
        hashedCookieID = self.__createSession__(username, ipaddress)
        return getUserByCookie(hashedCookieID, ipaddress)


    
    def changeBalance(self, user, amountToChangeBy):
        '''
            1) Authenticate by User, if the user is not logged in, an exception will be thrown
            2) Change the balance
            3) Get new balance and set the user object's balance to the new balance
        '''
        self.authenticateByUserObject(user)
        self.conn.cursor().execute("UPDATE user SET balance = (balance + %f) WHERE username = %s", amountToChangeBy, user.username)
        rows = self.conn.cursor().execute("SELECT balance FROM user WHERE username = %s", [user.username])
        user.balance = rows.get('balance') + amountToChangeBy
        return
    
    def getBalance(self, user):
        '''
            Sets the new balance of the user in the user object
        '''
        self.changeBalance(user, 0)
        return

    def logout(self, user):
        '''
            1) Authenticate by User, if the user is not logged in, an exception will be thrown
            2) Delete the session id and ip address from the database
        '''
        self.authenticateByUserObject(user)
        self.conn.cursor().execute("UPDATE user SET cookie = NULL WHERE username = %s", user.username)
        return
    
    def authenticateByUserObject(self, user):
        '''
            1) Get the user object's hashed cookie value and ip address
            2) Compare this value to the hashed session id and ip address in the database for this username
            3) if they are equal, the user is logged in, otherwise throw an exception
        '''
        sid = user.sessionID
        ipaddr = user.ipaddress
        hashedsid = bcrypt.hash(sid)

        rows = self.__getUsername__(user.username)
        checksid = bcrypt.hash(rows.get('sessionID'))
        checkip = rows.get('ipaddress')

        if checksid is None:
            raise Exception('Not logged in')
        if checkip is None: 
            raise Exception('Not logged in')

        if checksid != hashedsid:
            raise Exception('Not logged in')
        if checkip != ipaddr: 
            raise Exception('Not logged in')


    
    def getUserByCookie(self, stringInsideCookie, ipaddress):
        '''
            1) Get row by hashed session id and non-hashed ip address
            2) If there is no such row, throw an exception
            2) Return a user object with all the info
        '''
        

        
    def __createSession__(self, username, ipaddress):
        '''
            This function is not to be called directly ever
            1) Generate some random session id
            2) Store the non-hashed id along with the ip address in the database by username
            3) Return the hashed session id, this will be our cookie
        '''
        salt = bcrypt.genSalt(10)
        self.conn.cursor().execute("UPDATE user SET sessionID = %s WHERE username = %s", salt, username)
        self.conn.cursor().execute("UPDATE user SET ipaddress = %s WHERE username = %s", ipaddress, username)

        return bcrypt.hash(salt)


    def __getUsername__(self, username):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM user WHERE username = %s", [username])
        rows = cur.fetchone()
        cur.close()
        return rows
    
    def __generateSalt__(self):
        saltRounds = 12
        return bcrypt.genSalt(saltRounds)

    def __addUser__(self, username, hashedpw, salt, ipaddress):
        query1 = "INSERT INTO user(username, password, ipaddress, balance) VALUES (%s,%s,%s, 0)"
        insdata = (username, hashedpw, ipaddress)
        self.conn.cursor().execute(query1, insdata)
    
