from flask import Flask, render_template, redirect, url_for, flash, Blueprint


pengunjung = Blueprint('pengunjung', __name__)


@pengunjung.route('/')
def home():
    judul = 'Blog Us'
    return render_template('index.html', judul=judul)

@pengunjung.route('/about')
def about():
   return render_template('about.html')