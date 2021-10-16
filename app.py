from flask import Flask, request, jsonify, make_response
from flask_mysqldb import MySQL
import uuid

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'csci430'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)

@app.route('/register')
def register():
        # get the username and password
        username = request.args.get('user')
        password = request.args.get('pass')

        # add mySQL stuff here
        print(username)
        print(password)
        cur = mysql.connection.cursor()

        # validate before inserting
        cur.execute("SELECT * FROM user WHERE username = %s", [username])
        rows = cur.fetchone()
        cur.close()
        if rows is not None:
                res = make_response("fail signing up")
                return res

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(password, username) VALUES (%s, %s)", (hash(username), username))
        mysql.connection.commit()
        cur.close()
        res = make_response("signup succeed")
        return res

@app.route('/login')
def login():
        # get the username and password
        username = request.args.get('user')
        password = request.args.get('pass')

        # add mySQL stuff here
        print(username)
        print(password)

        # serve the user a cookie
        res = make_response("Setting a cookie")
        res.set_cookie('auth_cookie', uuid.uuid4(), max_age=60*30)
        return res

@app.route('/manage')
def manage():
        if not request.cookies.get('auth_cookie'):
                # return unauth
                pass
        else:
                # check auth
                pass
        # get the action and amount
        action = request.args.get('action')
        amount = request.args.get('amount')

        status_code = 200

        if (action == "deposit"):
                # add mySQL stuff here
                print("deposited $" + str(amount))
        elif (action == "withdraw"):
                # add mySQL stuff here
                print("withdrew $" + str(amount))
        elif (action == "balance"):
                # add mySQL stuff here
                print("balance=")
        elif (action == "close"):
                # add mySQL stuff here
                print("account closed")
        else:
                status_code = 400
        
        return jsonify({
                'Status': status_code,
                'Response': 'account action'
        })

@app.route('/logout')
def logout():
        print("Logged out")
        # add mySQL stuff here
        # delete user cookie


context = ('cert.pem', 'key.pem')
app.run(debug=False, ssl_context=context, host='0.0.0.0', port=1)
