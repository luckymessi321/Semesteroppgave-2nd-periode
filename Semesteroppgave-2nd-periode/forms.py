# denne filen er limt inn fra en lærer sin presentasjon, men tilpasset til prosjektet mitt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

# oppretter 3 nye klasser; 'RegisterForm', 'LoginForm og 'LogoutForm'
class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Register")
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Log in")

class LogoutForm(FlaskForm):
    submit = SubmitField("Log out")
