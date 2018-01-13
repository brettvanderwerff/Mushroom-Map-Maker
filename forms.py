'''A UserInput class is generated for downstream import and instantiation by the Mushroom map maker web app module.'''

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

'''
UserInput class built around flask-wtf will be used to generate a form to accept user input in the form of a mushroom
genus and species.'''
class UserInput(FlaskForm):
    genus_name = StringField('Genus name: ', validators=[DataRequired('Please enter a genus name.')])
    species_name = StringField('Species name: ', validators=[DataRequired('Please enter a species name.')])
    submit = SubmitField('Submit')