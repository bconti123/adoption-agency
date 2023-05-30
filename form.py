from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, NumberRange, Length, URL
specific = 'cat' or 'dog' or 'porcupine'
class AddPetForm(FlaskForm):
    '''Form for adding pets.'''
    name = StringField("Pet Name: ", validators=[InputRequired(message="Field cannot be blank")])
    species = SelectField("Species: ", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL: ", validators=[Optional(), URL()])
    age = IntegerField("Age: ", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes: ", validators=[Optional(), Length(min=10)])
    available = BooleanField("Is available?: ", validators=[Optional()])

class EditPetForm(FlaskForm):
    '''Form for editing pets.'''
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes: ", validators=[Optional(), Length(min=10)])
    available = BooleanField("Is available?: ")