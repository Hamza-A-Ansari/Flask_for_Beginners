from flask import Flask, json
from flask_mail import *
app = Flask(__name__)

with open('config.json', 'r') as f:
    param = json.load(f)['parameter']

app.config['MAIL_SERVER'] = 'sntp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = param['gmail-user']
app.config['MAIL_PASSWORD'] = param['gmail-password']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

users = [{'name': 'Hamza', 'email': 'abc@gmail.com'},
        {'name': 'Noman', 'email': 'def@gmail.com'}]
mail = Mail(app)

@app.route('/')
def mainpage():
    with mail.connect() as con:
        for user in users:
            msg = 'Hello %s' % user['name']
            msgs = Message(recipients=[user['name']], body=msg, subject='imp mail',
                           sender='ibneshakeel2000@gmail.com')
            con.send(msgs)

app.run(debug=True)