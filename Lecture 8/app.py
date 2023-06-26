from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('form.html')
@app.route('/success', methods=['POST','GET'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save('Lecture 8/static/Image'+f.filename)
        return render_template('result.html')
    
app.run(debug=True)
