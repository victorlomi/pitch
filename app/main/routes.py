from flask import render_template
from app.main import bp
from app.main import forms

@bp.route('/')
def index():
    return render_template('index.html') 

@bp.route('/login')
def login():
    form = forms.LoginForm()
    return render_template('login.html', form=form)
