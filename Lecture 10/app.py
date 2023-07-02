from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key='login'

@app.route('/')
def mainform():
    return render_template('form.html')

@app.route('/loginform', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        u_name = request.form['name']
        password = request.form['password']
        if email=='abc@gmail.com' and u_name=='Hamza' and password=='123':
            session['email'] = u_name
            return render_template('success.html',username=u_name)
        else:
            message = 'Invalid Username or Password'
            return render_template('form.html',msg=message)
        
@app.route('/logoutform')
def logout():
    session.pop('email',None)
    return render_template('form.html')
    
app.run(debug=True)