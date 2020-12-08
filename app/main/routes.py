from flask import render_template
from app.main import bp
from app import db
from app.models import User, Pitch

@bp.route('/')
def index():
    return render_template('index.html') 

@bp.route('/category/<category>')
def category(category):
    # retrieve all pitches in category
    pitches = Pitch().query.all()
    return render_template('category.html', category=category)
