from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email
from wtforms import StringField

class SubscribeForm(FlaskForm):
    email           = StringField('Email', [InputRequired(), Email()])
    firstname       = StringField('Firstname', [InputRequired()])
    lastname        = StringField('Lastname', [InputRequired()])
    zipcode         = StringField('Zipcode', [InputRequired()])