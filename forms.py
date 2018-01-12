from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserInput(FlaskForm):
    genus_name = StringField('Genus name: ', validators=[DataRequired('Please enter a genus name')])
    species_name = StringField('Species name: ', validators=[DataRequired('Please enter a species name')])
    submit = SubmitField('Sign In')