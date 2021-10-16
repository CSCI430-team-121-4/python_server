import mysql
import json


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
    
    def login(self, username, password, ipaddress):
        ''' 
            0) delay a small, random amount of time
            1) check if username already exists, if not, throw exception
            2) if it does, get the user's salt
            3) add salt to password
            4) hash password
            6) check that the two hashes match, if not, throw exception
            7) create session for this user, return user object by using getUserByCookie
        '''
    
    def changeBalance(self, user, amountToChangeBy):
        '''
            1) Authenticate by User, if the user is not logged in, an exception will be thrown
            2) Change the balance
            3) Get new balance and set the user object's balance to the new balance
        '''
    
    def getBalance(self, user):
        '''
            Sets the new balance of the user in the user object
        '''
        self.changeBalance(user, 0)

    def logout(self, user):
        '''
            1) Authenticate by User, if the user is not logged in, an exception will be thrown
            2) Delete the session id and ip address from the database
        '''
    
    def authenticateByUserObject(self, user):
        '''
            1) Get the user object's hashed cookie value and ip address
            2) Compare this value to the hashed session id and ip address in the database for this username
            3) if they are equal, the user is logged in, otherwise throw an exception
        '''
    
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
            2) Hash the id
            3) Store the hashed id along with the ip address in the database by username
            4) Return the hashed session id, this will be our cookie
        '''


    
