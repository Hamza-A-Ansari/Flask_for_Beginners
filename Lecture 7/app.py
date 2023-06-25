from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def registration():
    return render_template('form.html')
@app.route('/success', methods=['POST','GET'])
def printdata():
    if request.method=='POST':
        result = request.form
        return render_template('display.html', result=result)

app.run(debug=True)