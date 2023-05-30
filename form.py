from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Optional, NumberRange, EqualTo
specific = 'cat' or 'dog' or 'porcupine'
class AddPetForm(FlaskForm):
    '''Form for adding pets.'''
    name = StringField("Pet Name: ", validators=[InputRequired()])
    species = StringField("Species Name: ", validators=[InputRequired()])
    photo_url = StringField("Photo URL: ", validators=[Optional()])
    age = IntegerField("Age: ", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Note: ", validators=[Optional()])
    available = BooleanField("Is available?: ", validators=[Optional()])
