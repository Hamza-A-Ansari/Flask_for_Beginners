from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = 'login form'

@app.route('/')
def mainpage():
    return render_template('form.html')
@app.route('/loginform', methods=['GET'])
def login():
    u_name = request.args.get('user')
    pas = request.args.get('pass')
    if u_name == 'Hamza' and pas == '1234':
        flash('You are successfully logged in!')
        return render_template('message.html', name=u_name)
    else:
        error='Invalid usernamr or Password'
        return render_template('form.html', error=error)
        #return redirect(url_for('mainpage'))
    
app.run(debug=True)