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

mail = Mail(app)

@app.route('/')
def mainpage():
    # 1st parameter is subject in mail and 2nd & 3rd are sender & reciever
    msg = Message('Important mail', sender='ibneshakeel2000@gmail.com', 
                  recipients=['ibneshakeel2000@gmail.com'])
    msg.body = 'Hi, My name is Hamza Ahmed Ansari!'
    with app.open_resource('D:/Hamza/Flask Practice/Playlist/Lecture 6/static/Image') as image:
        # 1st parameter is name which we have to show on email
        # 2nd parameter is to show that your attachment is image in png form (image/png)
        msg.attach('my image', 'image/png', image.read())
    mail.send(msg)
    return 'Message sent'

app.run(debug=True)