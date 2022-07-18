from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequiered, Email, Lenght

class SignupForm(FlaskForm):
    name=StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password=PasswordField('Password', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired(), Email()])
    submit=submitField('Registrar')
