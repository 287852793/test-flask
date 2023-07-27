#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 15:38
# @Author  : pyf
# @File    : app_cookie.py
# @Description : cookie 操作

from flask import Flask, make_response, request

app = Flask(__name__)

cookie_key = 'cookie_key'
cookie_value = 'cookie_value'


@app.route('/set_cookie')
def set_cookie():
    resp = make_response("set cookie success")
    resp.set_cookie(cookie_key, cookie_value, max_age=3600)  # 单位：秒
    return resp


@app.route('/get_cookie')
def get_cookie():
    cookie = request.cookies.get(cookie_key)
    return cookie


@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response("delete cookie success")
    resp.delete_cookie(cookie_key)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
