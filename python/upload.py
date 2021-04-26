from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

app.config['PYTHON'] = os.getcwd()+'/media/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 限制大小16MB


@app.route('/')
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['PYTHON'], secure_filename(f.filename)))
        return 'file uploaded successfully'