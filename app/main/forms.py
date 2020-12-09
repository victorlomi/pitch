from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms import validators
from app.models import User

class AddForm(FlaskForm):
    body = TextAreaField('Body', [validators.optional(), validators.length(max=200)])
    category = SelectField('Category', choices=[('Pickup Lines', 'pickup'), ('Interview', 'interview'), ('Product', 'product'), ('Promotion', 'promotion')])
    submit = SubmitField('Submit')