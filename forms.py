from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired("Please enter your first name")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter your last name")])
    email = StringField('Email', validators=[DataRequired( "please enter your email"), Email("Plase enter a valid email address")])
    password = PasswordField('password', validators=[DataRequired("Please enter your password"), Length(min=6)])
    submit = SubmitField('Sign up')

class Login(Form):
    email = StringField('Email', validators=[DataRequired( "please enter your email"), Email("Plase enter a valid email address")])
    password = PasswordField('password', validators=[DataRequired("Please enter your password")])
    submit = SubmitField('Sign in')
