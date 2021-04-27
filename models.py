from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

def connect_db(arr):
    db.app = arr
    db.init_app(arr)

class Pet(db.Model):
    """Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    name = db.Column(db.Text,nullable=False,unique=True)

    species = db.Column(db.Text,nullable=False)

    photo_url = db.Column(db.Text,nullable=True)

    age = db.Column(db.Integer,nullable=True)

    notes = db.Column(db.Text,nullable=True)

    available = db.Column(db.Boolean,nullable=False,default=True)