import os
import secrets
from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request
from blog import db, bcrypt, app
from blog.admin.forms import pendaftaran, LoginForm, ArtikelForm, KategoriForm
from blog.models import User, Artikel,  Kategori
from flask_login import login_user, login_required, logout_user, current_user
from PIL import Image
from .fungsi_gambar import simpan_gambar

admin = Blueprint('admin', __name__)


@admin.route('/registerasi', methods=['GET', 'POST'])
def res():
    if current_user.is_authenticated:
        return redirect(url_for('admin.user'))
    form = pendaftaran()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User.query.all()
        if not user:
             user = User(username=form.username.data, email=form.email.data, password=hash_password, role_id=1)
        else:
              user = User(username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash('Data Successfully Entered into the database', 'success')
        return redirect(url_for('admin.user'))
    return render_template('registerasi.html', form=form)
        
@admin.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.user'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page) if next_page else redirect(url_for('admin.user'))
         
        else:
            flash('Login Gagal.Check Your Email', 'danger')
    return render_template('login.html', form=form)
            
@admin.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('admin.login'))
        
    
@admin.route('/user')
@login_required
def user():
    user = User.query.all()
    return render_template('user.html', user=user)

@admin.route('/kategori', methods=['GET', 'POST'])
@login_required
def kategori():
    form = KategoriForm()
    if form.validate_on_submit():
        kategori = Kategori(nama=form.nama_kategori.data)
        db.session.add(kategori)
        db.session.commit()
        flash('Kategori Sukses di Tambahkan', 'success')
        return redirect(url_for('admin.artikel'))
    return render_template('kategori.html', form=form)
 





@admin.route('/artikel', methods=['GET','POST'])
@login_required
def artikel():
    form = ArtikelForm()
    form.kategori.choices = [(str(kategori.id), kategori.nama) for kategori in Kategori.query.all()]
    if form.validate_on_submit():
        gambar = simpan_gambar(form.thumbnail.data)
        artikel = Artikel(judul=form.judul.data, konten=form.content.data, thumbnail=gambar, publish=form.publish.data, user_id=current_user.id,  kategori_id=form.kategori.data)
        db.session.add(artikel)
        db.session.commit()
        flash('Data Berhasil di Tambahkan', 'success')
        return redirect(url_for('admin.artikel'))
    return render_template('artikel.html', form=form)



