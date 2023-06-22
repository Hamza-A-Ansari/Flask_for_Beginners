from flask import Flask, request
app = Flask(__name__)

@app.route('/form', methods = ['POST'])
def login():
    name = request.form['user']
    email = request.form['email']
    pasw = request.form['pass']
    if name == 'Hamza' and email == 'ibneshakeel2000@gmail.com' and pasw == '123':
        return "Welcome to your account"
    else:
        return "Please try again"


app.run(debug=True)