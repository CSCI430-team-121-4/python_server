import hashlib
from flask import Flask, request, jsonify, make_response
from flask_mysqldb import MySQL
import uuid
from SqlHandler import SqlHandler as sql

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ZEw2Uk2+merS@uQa'
app.config['MYSQL_DB'] = 'csci430'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)

@app.route('/register')
def register():
        # get the username and password
        username = request.args.get('user')
        password = request.args.get('pass')
        ipaddress = request.remote_addr
        db = sql()
        # add mySQL stuff here
        res = make_response("signup succeed")
        try:
                sessionId = request.cookies.get('cookie')
                ipaddress = request.remote_addr
                db.logout(db.getUserByCookie(sessionId, ipaddress))
        except Exception as e:
                print('user was not logged in initially')
        try:
                user = db.register(username, password, ipaddress)
                print(user)
                res.set_cookie('cookie', user.sessionID)  
        except Exception as e:
                print(e)
                res = make_response("signup failed")
        return res

@app.route('/login')
def login():
        # get the username and password
        username = request.args.get('user')
        password = request.args.get('pass')
        ipaddress = request.remote_addr
        db = sql()
        # add mySQL stuff here
        try:
                user = db.login(username, password, ipaddress)  
        except Exception as e:
                print(e)
                res = make_response("login failed")
                return res
        res = make_response("login succeed signed in as " + user.username)
        res.set_cookie('cookie', user.sessionID)
        return res

@app.route('/manage')
def manage():
#need to add responses for each
        action = str(request.args.get('action'))
        cookie = str(request.cookies.get('cookie'))
        ipaddress = request.remote_addr
        db = sql()
        user = db.getUserByCookie(cookie, ipaddress)
        if user is None:
                return make_response('not logged in')
        print(user)
        if (action == 'close'):
                db.deleteUser(cookie, ipaddress)
                return make_response('user deleted')
        elif (action == 'withdraw'):
                amount = abs(float(request.args.get('amount')))
                db.getBalance(user)
                if (user.balance < amount):
                        resp = make_response('failed, insufficient balance')
                        return resp
                db.changeBalance(user, amount *-1)
        elif action == 'balance':
                db.changeBalance(user, 0)
        else:
                amount = abs(float(request.args.get('amount')))
                db.changeBalance(user, amount)
        return make_response("balance is " + str(user.balance))

@app.route('/logout')
def logout():
        # delete user cookie
        sessionId = request.cookies.get('cookie')
        ipaddress = request.remote_addr
        db = sql()
        db.logout(db.getUserByCookie(sessionId, ipaddress))
        res = make_response("log out succeeds")
        return res

app.run(debug=False, host='localhost', port=80)

def hashing(password):
        return hashlib.md5(password.encode('utf-8')).hexdigest()