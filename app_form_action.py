#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 14:44
# @Author  : pyf
# @File    : app_form_action.py
# @Description : 表单处理(将表单数据发送到模板中返回)

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    print(request.method)
    if request.method == 'POST':
        formdata = request.form
        return render_template('result.html', formdata=formdata)
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
