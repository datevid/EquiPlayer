# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)

    @validates('email')
    def validate_email(self, key, email):
        # Realiza la validación del campo de correo electrónico
        if email is None or '@' not in email:
            raise ValueError('Email inválido')
        return email


class Player(db.Model):
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String)
    sizeplayer = db.Column(db.Integer)

    @validates('sizeplayer')
    def validate_sizeplayer(self, key, sizeplayer):
        # Realiza la validación del campo de tamaño del jugador
        if sizeplayer < 0:
            raise ValueError('Tamaño de jugador inválido')
        return sizeplayer