#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 10:33
# @Author  : pyf
# @File    : app_base.py.py
# @Description : 基本的 flask 服务

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# 支持多种 methods
@app.route('/fun1/<int:param>', methods=['GET', 'POST'])
def fun1(param):
    return str(param) + '666'


if __name__ == '__main__':
    # 设置 debug=True 可以实现热更新
    app.run(debug=True)
