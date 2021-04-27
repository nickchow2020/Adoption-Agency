from flask_wtf import FlaskForm 
from wtforms import StringField,IntegerField,RadioField,BooleanField
from wtforms.validators import AnyOf,URL,Optional,NumberRange

class Newpet(FlaskForm):
    name = StringField("Pet Name")
    species = StringField("Species",validators=[AnyOf(values=["cat","dog","porcupine"],message="Only cat,dog,and porcupine allow")])
    url = StringField("Photo URL",validators=[URL(message="Please provide a valid URL"),Optional()])
    age = IntegerField("Age",validators=[NumberRange(min=0,max=30,message="Please Provide a age range between 0 - 30"),Optional()])
    note = StringField("notes")

class _Pet(FlaskForm):
    name = StringField("Pet Name")
    species = StringField("Species",validators=[AnyOf(values=["cat","dog","porcupine"],message="Only cat,dog,and porcupine allow")])
    photo_url = StringField("Photo URL",validators=[URL(message="Please provide a valid URL"),Optional()])
    age = IntegerField("Age",validators=[NumberRange(min=0,max=30,message="Please Provide a age range between 0 - 30"),Optional()])
    notes = StringField("notes")
    available = BooleanField("Available For Adopt")