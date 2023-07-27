#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 10:55
# @Author  : pyf
# @File    : app_converter.py
# @Description : 自定义路由参数转换器

from werkzeug.routing import BaseConverter
from flask import Flask

app = Flask(__name__)


class MyRegexConverter(BaseConverter):
    """自定义转换器"""

    def __init__(self, url_map, regex):
        super(MyRegexConverter, self).__init__(url_map)
        # 正则转换器
        self.regex = regex

    def to_python(self, value: str):
        print('invoke to_python')
        return value


app.url_map.converters['re'] = MyRegexConverter

print(app.url_map.converters)


@app.route('/<re("\d123"):value>')
def fun1(value):
    print(value)
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
