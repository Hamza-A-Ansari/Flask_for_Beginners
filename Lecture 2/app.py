from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/<name>')
def na_func(name):
    return 'Hello ' + name

@app.route('/<int:date>')
def da_func(date):
    return f'Date= {date}'

app.run(debug=True)
