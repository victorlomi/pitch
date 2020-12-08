from flask import render_template, flash, redirect
from app.main import bp
from app.main import forms

@bp.route('/')
def index():
    return render_template('index.html') 

@bp.route('/login', methods=['GET', 'POST'])
def login():
    # create instance of login form to be passed in to template
    form = forms.LoginForm()

    # handle post response from form
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}")

        # redirect to home - TODO - change to posts route
        return redirect('/') 

    return render_template('login.html', form=form)
