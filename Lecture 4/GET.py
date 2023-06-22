from flask import Flask, request
app = Flask(__name__)

@app.route('/form', methods = ['GET'])
def login():
    name = request.args.get('user')
    email = request.args.get('email')
    pasw = request.args.get('pass')
    if name == 'Hamza' and email == 'ibneshakeel2000@gmail.com' and pasw == '123':
        return 'Welcome to your account'
    else:
        return 'Try again'
    
app.run(debug=True)

