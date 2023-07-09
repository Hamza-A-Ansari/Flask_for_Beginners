# Show count of the visits of webite through cookies
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/')
def mainpage():
    count = int(request.cookies.get('visit_count',0))
    count+=1
    msg=f'You visited this page {str(count)} time(s)'
    resp = make_response(msg)
    resp.set_cookie('visit_count',str(count))
    return resp

app.run(debug=True)