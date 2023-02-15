# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField as TextField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired

## login and registration

class LoginForm(FlaskForm):
    username = TextField    ('Username', id='username_login'   , validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login'        , validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username = TextField('Username'     , id='username_create' , validators=[DataRequired()])
    # email    = TextField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
    password = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])

class UpdateAccountForm(FlaskForm):
    password = TextField('Password' , id='password'      , validators=[DataRequired()])
    group = TextField('Group', id='group_update')
    token = TextField('Token', id='token', validators=[DataRequired()])
