#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 15:47
# @Author  : pyf
# @File    : app_session.py
# @Description : session 操作

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '123456'


@app.route('/')
def index():
    if 'username' in session:
        user = session['username']
        return f'当前用户：{user}，<br> <a href="/logout">点击这里注销</a>'
    else:
        return f'您暂未登录，<a href="/login">点击这里登录</a>'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # 这里处理登录请求操作, 设置 session 参数
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        # 这里重定向到登录页面
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
