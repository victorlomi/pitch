from flask import render_template, redirect, url_for, flash
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

    if pitches:
        pitches.reverse()
    return render_template('category.html', category=category, pitches=pitches)

@bp.route('/add-pitch', methods=['GET', 'POST'])
def add_pitch():
    # go to login in page if user is not logged in
    if current_user.is_anonymous:
        return redirect(url_for('auth.login'))

    form = forms.AddForm()

    if form.validate_on_submit():
        pitch = Pitch(author=current_user, body=form.body.data, category=form.category.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index')) 
    
    return render_template('add_pitch.html', form=form)

@bp.route('/user/<user>')
def user(user):
    # go to login in page if user is not logged in
    if current_user.is_anonymous:
        return redirect(url_for('auth.login'))

    user = User.query.filter_by(username=user).first()
    pitches = Pitch.query.filter_by(author=user).all()
    return render_template('user.html', user=user, pitches=pitches)

@bp.route('/comments/<pitch>')
def comments(pitch):
    # go to login in page if user is not logged in
    if current_user.is_anonymous:
        return redirect(url_for('auth.login'))
   
    return render_template('comments.html', pitch=pitch)
