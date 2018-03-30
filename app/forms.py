#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Name:forms
# Description:
# Author:luoweibo
# Date:2018/3/29 16:10
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
