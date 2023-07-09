from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template("form.html")

@app.route('/loginform', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        u_name = request.form['name']
        password = request.form['password']
        if email == 'abc@gmail.com' and u_name == 'Hamza' and password == '123':
            resp = make_response(render_template('success.html'))
            resp.set_cookie('email', u_name)
            return resp
        else:
            message = 'Invalid Username or Password'
            return render_template('form.html', msg=message)

@app.route('/logoutform')
def logout():
    return render_template('form.html')

@app.route('/myprofile')
def profile():
    email = request.cookies.get('email')
    resp = make_response(render_template('profile.html', username=email))
    return resp

app.run(debug=True)