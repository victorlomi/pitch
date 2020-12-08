from flask import render_template
from app.main import bp
from app.main import forms

@bp.route('/')
def index():
    return 'welcome to pitch!'

@bp.route('/login')
def login():
    form = forms.LoginForm()
    return render_template('login.html', form=form)
