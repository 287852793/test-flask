#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 16:22
# @Author  : pyf
# @File    : app_flash.py
# @Description : 消息闪现，设定一个消息，并将其带入下一次的 request 中（感觉没什么卵用啊？）

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = '123456'


@app.route('/')
def index():
    """
    flash.html 作为本例主页，展示消息闪现
    :return:
    """
    return render_template('flash.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    errmsg = None

    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == '123456':
            flash('login success')
            flash('congratulations')
            return redirect(url_for('index'))
        else:
            errmsg = 'Invalid username or password, please try again.'
    return render_template('login.html', errmsg=errmsg)


if __name__ == '__main__':
    app.run(debug=True)
