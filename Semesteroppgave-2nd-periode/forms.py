# denne filen er limt inn fra en lærer sin presentasjon, men tilpasset til prosjektet mitt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

# oppretter 5 nye klasser; 'RegisterForm', 'LoginForm', 'LogoutForm', 'EditForm', 'DeleteForm'
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

class EditForm(FlaskForm):
    username1 = StringField("Username", validators=[InputRequired()])
    password1 = PasswordField("Password", validators=[InputRequired()])
    editUsername = StringField("Username", validators=[InputRequired()])
    editPassword = PasswordField("Password", validators=[InputRequired()])
    submitEdit = SubmitField("Save changes to user")


class DeleteForm(FlaskForm):
    username2 = StringField("Username", validators=[InputRequired()])
    password2 = PasswordField("Password", validators=[InputRequired()])
    submitDelete = SubmitField("Delete current user")
