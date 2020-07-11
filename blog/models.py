from blog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_profile = db.Column(db.String(60), default='default.jpg')
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False,  default=3)   
    post = db.relationship('Artikel', backref='author', lazy=True)

class Artikel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(255), nullable=False)    
    konten = db.Column(db.Text, nullable=False)
    thumbnail = db.Column(db.String(255), nullable=False)        
    publish = db.Column(db.Boolean, nullable=False, default=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)   
    kategori_id = db.Column(db.Integer, db.ForeignKey('kategori.id'), nullable=False)

class Kategori(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     nama = db.Column(db.String(30), nullable=False)   
     artikel = db.relationship('Artikel', backref='category', lazy=True)

class Role(db.Model):
         id = db.Column(db.Integer, primary_key=True)
         jabatan = db.Column(db.String(20), nullable=False)
         user = db.relationship('User', backref='Level', lazy=True)