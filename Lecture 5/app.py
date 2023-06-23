from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to my page'
@app.route('/<u_name>')
def html(u_name):
    return render_template('index.html', name = u_name)
# @app.route('/<int:score>')
# def sc(score):
#     return render_template('index.html', name = score)

app.run(debug=True)