# denne filen er limt inn fra en lærer sin presentasjon, men tilpasset til prosjektet mitt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

# oppretter 2 nye klasser; 'RegisterForm' og 'LoginForm
class RegisterForm(FlaskForm):
    username = StringField("Brukernavn", validators=[InputRequired()])
    password = PasswordField("Passord", validators=[InputRequired()])
    submit = SubmitField("Registrer")
class LoginForm(FlaskForm):
    username = StringField("Brukernavn", validators=[InputRequired()])
    password = PasswordField("Passord", validators=[InputRequired()])
    submit = SubmitField("Logg inn")

