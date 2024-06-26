from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    email= StringField("Email",validators=[DataRequired(),Email(),Length(min=2,max=20)])
    password=PasswordField("Password",validators=[DataRequired(),Length(min=2, max=20)])
    confirm_password=PasswordField("Confirm Password",validators=[DataRequired(),Length(min=2, max=20),EqualTo("password")])
    
    submit=SubmitField("Sign Up")
    
class LoginForm(FlaskForm):
    # userName = StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    email= StringField("Email",validators=[DataRequired(),Email(),Length(min=2,max=20)])
    password=PasswordField("Password",validators=[DataRequired(),Length(min=2, max=20)])
    remember= BooleanField("Remember Me")
    #confirm_password=PasswordField("Confirm Password",validators=[DataRequired(),Length(min=2, max=20),EqualTo("password")])
    
    submit=SubmitField("Login")