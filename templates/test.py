from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 顯示表單
    return render_template('form.html')


@app.route('/', methods=['POST'])
def process():
    # 處理圖片
    return 'Process'



