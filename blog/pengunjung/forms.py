from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError

class pendaftaran(FlaskForm):
    username = StringField('Name', validators=[DataRequired(), length(min=2, max=20, message='Name Does Not Match System Provisions')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirmasi Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Daftar')

