from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.model):
    '''Pet'''
    __tablename__ = "pet"

    id = db.Column(db.integer, autoinrement=True, primary_key=True)
    name = db.Column(db.Text, required=True, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    available = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'Pet {self.id} {self.name} {self.species}' 