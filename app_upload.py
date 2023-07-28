#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/28 8:52
# @Author  : pyf
# @File    : app_upload.py
# @Description : flask upload file test
import os.path

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename  # 将文件名转为安全的文件名

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload_files'


@app.route('/')
def index():
    """
    主页包含一个文件上传控件
    :return:
    """
    return render_template('upload.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        # 如果没有文件夹则创建
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return 'file upload success'
    else:
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
