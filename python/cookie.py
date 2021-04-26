from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods= ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['username']
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('username',user)
    return resp
