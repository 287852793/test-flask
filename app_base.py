#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 10:33
# @Author  : pyf
# @File    : app_base.py.py
# @Description : 基本的 flask 服务

from flask import Flask

# 这里的 __name__ 如果是外部调用，则是文件名 app_base ，如果是自己调用，则是 __main__
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# 标准写法路径后面要加/
# 这种情况下，访问地址后面无论加不加/都能正常访问，如果这里后面不加/，如果访问加了/就会报错
@app.route('/python/')
def hello_python():
    return 'Hello, python!'


# 支持多种 methods
@app.route('/fun1/<int:param>', methods=['GET', 'POST'])
def fun1(param):
    return str(param) + '666'


if __name__ == '__main__':
    # 设置 debug=True 可以实现热更新
    app.run(debug=True)
