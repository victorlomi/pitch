from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.main import bp
from app import db
from app.models import User, Pitch
from app.main import forms

@bp.route('/')
def index():
    return render_template('index.html') 

@bp.route('/category/<category>')
def category(category):
    # retrieve all pitches in category
    pitches = Pitch().query.filter_by(category=category).all()
    return render_template('category.html', category=category, pitches=pitches)

@bp.route('/add-pitch')
def add_pitch():
    # go to login in page if user is not logged in
    if current_user.is_anonymous:
        return redirect(url_for('auth.login'))

    form = forms.AddForm()
    
    return render_template('add_pitch.html', form=form)
