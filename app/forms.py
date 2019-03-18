from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed


class P_Form(FlaskForm):
    f_name = StringField('First Name', validators = [DataRequired()])
    l_name = StringField('Last Name', validators = [DataRequired()])
    gender = SelectField(u'Gender', choices=[('Male', 'Male'), ('Female', 'Female')])
    e_address = StringField('E-mail', validators = [DataRequired(), Email()])
    location = StringField('Location', validators = [DataRequired()])
    biography = TextAreaField('Biography', validators = [DataRequired()])
    photo = FileField ('Photo', validators = [FileRequired(), FileAllowed(['jpg','png'])])
