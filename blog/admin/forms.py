from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError
from blog.models import User, Role
from blog import db

class pendaftaran(FlaskForm):
    username = StringField('Name', validators=[DataRequired(), length(min=2, max=20, message='Name Does Not Match System Provisions')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirmasi Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Daftar')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('E-mail Sudah di Daftarkan')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Password')
    submit = SubmitField('Log in')

    

class ArtikelForm(FlaskForm):
    judul = StringField('Judul', validators=[DataRequired()])
    kategori = SelectField('kategori', validators=[DataRequired()])
    content = TextAreaField('Konten', validators=[DataRequired()])
    thumbnail = FileField('Upload Gambar', validators=[DataRequired()])
    publish = BooleanField('Publish')
    submit = SubmitField('Submit')

class KategoriForm(FlaskForm):
    nama_kategori = StringField('Nama Kategori', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RoleForm(FlaskForm):
    nama = StringField('Nama Role',  validators=[DataRequired()])    
    submit = SubmitField('Submit')