from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello', defaults={'name': 'Someone'}) #為參數加上預設值
@app.route('/hello/<name>')
def hello(name): #同一個 function 可套用多組路由
    return 'Hello, {}!'.format(name)

@app.route('/')
def main(name=None):
    # a = 'World'
    return render_template('index.html', name='World')


