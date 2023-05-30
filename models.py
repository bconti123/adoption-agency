from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://st4.depositphotos.com/14953852/22772/v/450/depositphotos_227725120-stock-illustration-image-available-icon-flat-vector.jpg"
def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    '''Pet'''
    __tablename__ = "pet"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f'Pet {self.id} {self.name} {self.species}' 