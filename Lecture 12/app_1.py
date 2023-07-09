# Set and Get Cookie
from flask import Flask, make_response, request
app = Flask(__name__)

@app.route('/set')
def set_cookie():
    res = make_response('<h1> Cookie is set </h1>')
    res.set_cookie('Framework', 'Flask')
    return res

@app.route('/get')
def get_cookie():
    name = request.cookies.get('Framework')
    return name

app.run(debug=True)