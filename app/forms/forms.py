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
    

    username = StringField('Username', validators=[InputRequired(), Length(min=1, max=10)])
    email = EmailField('Email', validators=[InputRequired(), Email(), KeyError('Invalid EMail')])
    password = PasswordField('Password', validators=[InputRequired(), Regexp(), KeyError('Password Must contain at least one character')])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo(), KeyError('Password Must match')])  