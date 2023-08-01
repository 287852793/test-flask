#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/1 10:34
# @Author  : pyf
# @File    : app_form_wtf.py
# @Description : 利用 flask 自带的 wtform 控件构建表单

from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
# wtforms 新版本取消了 TextField，改为了 StringField
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, RadioField, SelectField
from wtforms import validators

app = Flask(__name__)
app.secret_key = '123456'


@app.route('/', methods=['POST', 'GET'])
def index():
    wtform = ContactForm()

    if request.method == 'POST':
        if not wtform.validate():
            flash('Please Check Your Infos.')
            return render_template('wtform.html', form=wtform)
        else:
            return 'submit success'
    else:
        return render_template('wtform.html', form=wtform)


class ContactForm(FlaskForm):
    """
    自定义表单
    """
    name_field = StringField("Name", [validators.InputRequired("Please enter your name.")])
    gender_field = RadioField("Gender", choices=[('M', 'Male'), ('F', 'Female')])
    address_field = TextAreaField("Address")
    email_field = StringField("Email", [validators.InputRequired("Please enter your email."),
                                        validators.Email("Please enter a valid email address.")])
    age_field = IntegerField("Age", [validators.NumberRange(0, 120, "Please enter a valid age.")])
    language_field = SelectField("Language", choices=[('cpp', 'C++'), ('py', 'python'), ('java', 'Java')])
    submit_field = SubmitField("Submit")


if __name__ == '__main__':
    app.run(debug=True)
