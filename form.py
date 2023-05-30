from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    '''Form for adding pets.'''

    name = StringField("Pet Name: ", validators=[InputRequired()])
    species = StringField("Species Name: ", validators=[InputRequired()])
    photo_url = StringField("Photo URL: ", validators=[Optional()])
    age = StringField("Age: ", validators=[Optional()])
    notes = StringField("Note: ", validators=[Optional()])
    available = BooleanField("Is available?: ", validators=[Optional()])
