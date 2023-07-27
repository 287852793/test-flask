#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 14:08
# @Author  : pyf
# @File    : app_redirect.py
# @Description : flask 重定向

from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return 'hello admin'


@app.route('/guest/<name>')
def hello_guest(name):
    return f'hello guest: {name}'


@app.route('/user/<name>')
def hello_user(name):
    """
    根据条件重定向到上面两个方法

    :param name:
    :return:
    """
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', name=name))


if __name__ == '__main__':
    app.run(debug=True)
