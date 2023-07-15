from flask import Flask, json, render_template, request
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
    return render_template('form.html')
@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['msg']
    # 1st parameter is subject in mail and 2nd & 3rd are sender & reciever
    msg = Message(subject, sender=[email], 
                recipients=['ibneshakeel2000@gmail.com'])
    msg.body = message

    mail.send(msg)
    return 'Message sent'

app.run(debug=True)