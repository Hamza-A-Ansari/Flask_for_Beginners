from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my page'
@app.route('/student')
def std():
    return 'Welcome Students'
@app.route('/faculty')
def fac():
    return 'Welcome Faculty'
@app.route('/user/<name>')
def red(name):
    if name == 'student':
        return redirect(url_for('std'))
    if name == 'faculty':
        return redirect(url_for('fac'))

app.run(debug=True)