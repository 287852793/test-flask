#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/1 14:04
# @Author  : pyf
# @File    : app_sijax.py
# @Description : flask sijax 处理异步请求 (Simple Ajax)，感觉没啥卵用

import os
from flask import Flask, g, render_template
import flask_sijax

app = Flask(__name__)

# os.path.dirname(__file__) 为当前文件绝对路径
path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
if not os.path.exists(path):
    os.makedirs(path)

app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'

flask_sijax.Sijax(app)


@app.route('/')
def index():
    return "Hello World! <br/> <a href='/sijax'>test sijax</a>"


@flask_sijax.route(app, '/sijax')
def sijax():
    """

    :return:
    """

    def hello_handler(obj_response, hello_from, hello_to):
        """
        异步请求处理
        :param response:
        :param hello_from:
        :param hello_to:
        :return:
        """
        obj_response.alert(f'Hello from {hello_from} to {hello_to}')
        obj_response.css('a', 'color', 'green')

    def goodbye_handler(obj_response):
        """
        异步请求处理
        :param response:
        :return:
        """
        obj_response.alert(f'goodbye')
        obj_response.css('a', 'color', 'red')

    if g.sijax.is_sijax_request:
        g.sijax.register_callback('say_hello', hello_handler)
        g.sijax.register_callback('say_goodbye', goodbye_handler)
        return g.sijax.process_request()
    else:
        return render_template('sijax.html')


if __name__ == '__main__':
    app.run(debug=True)
