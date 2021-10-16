from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register')
def register():
        # get the username and password
        username = request.args.get('user')
        password = request.args.get('pass')

        # add mySQL stuff here
        print(username)
        print(password)

@app.route('/login')
def login():
        # get the username and password
        username = request.args.get('user')
        password = request.args.get('pass')

        # add mySQL stuff here
        print(username)
        print(password)

        # serve the user a cookie

@app.route('/manage')
def manage():
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
