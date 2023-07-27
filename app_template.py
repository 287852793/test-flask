#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 11:50
# @Author  : pyf
# @File    : app_template.py
# @Description : flask 模板, 可返回 html 文件

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    param_int = 123
    param_str = "something"
    param_arr = [5, 4, 3, 2, 1]
    param_obj = {
        'name': 'pyf',
        'age': 35
    }
    return render_template('index.html',
                           param_int=param_int,
                           param_str=param_str,
                           param_arr=param_arr,
                           param_obj=param_obj
                           )


if __name__ == '__main__':
    app.run(debug=True)
