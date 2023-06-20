from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<htlml><body><h4>Welcom to html page</h4></body></html>'

app.run(debug=True)