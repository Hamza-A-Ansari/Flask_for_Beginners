from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to my page'
@app.route('/marksheet')
def msheet():
    dict = {'Numerical Computing':72, 'Operation Research':89, 'DataBase': 90}
    return render_template('index2.html', result = dict, name = 'Hamza')

app.run(debug=True)
