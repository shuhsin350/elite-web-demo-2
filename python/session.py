from flask import Flask, session, request, render_template, redirect, url_for
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return '登入名稱:'+username+'<br>'+"<b><a href='/logout'>點此登出</a></b>"
    return "您尚未登入<br><a href='/login'>"+"點此登入</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    print(session)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    print(session)
    return redirect(url_for('index'))