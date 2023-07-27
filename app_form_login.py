#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 15:16
# @Author  : pyf
# @File    : app_form_login.py
# @Description : form login操作，结合 redirect & abort

from flask import Flask, redirect, abort, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    """
    默认页面为登录页

    :return:
    """
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == '123456':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))


@app.route('/ok')
def success():
    return 'login success'


if __name__ == '__main__':
    app.run(debug=True)
