from flask_wtf import FlaskForm
from wtforms import (PasswordField, StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, EmailField)
from wtforms.validators import InputRequired, Length, Regexp, Email, EqualTo


class CourseForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    description = TextAreaField('Course Description',
                                validators=[InputRequired(),
                                            Length(max=200)])
    price = IntegerField('Price', validators=[InputRequired()])
    level = RadioField('Level',
                       choices=['Beginner', 'Intermediate', 'Advanced'],
                       validators=[InputRequired()])
    available = BooleanField('Available', default='checked')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(),Length(min=4, max=20)])
    email = EmailField('Email', validators=[InputRequired(), Email(message='Invalid Email')])
    password = PasswordField('Password', validators=[InputRequired(),Length(min=6,message='Password must contain at least one number'),Regexp(r'^(?=.*\d)', message='Password must contain at least one letter and one number')])
    confirm_password = PasswordField('Confirm Password',validators=[InputRequired(),EqualTo('password', message='Passwords must match')])