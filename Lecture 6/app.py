from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/page')
def page1():
    return render_template('pure.html')
@app.route('/page/<uname>')
def page2(uname):
    return 'Hello, Welcome ' + uname

app.run(debug=True)
