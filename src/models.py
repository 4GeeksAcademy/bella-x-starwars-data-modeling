import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer,primary_key=True)
    name = Column(String(250), nullable=True)
    gender = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    hair_color = Column(String(250), nullable=True)
    height = Column(String(250), nullable=True)
    skin_color = Column(String(250), nullable=True)
    mass = Column(String(250), nullable=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer,primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=True)
    mass = Column(String(250), nullable=True)
    population = Column(String(250), nullable=True)
    gravity = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)
    rotation_period = Column(String(250), nullable=True)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer,primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    cost_in_credits = Column(String(250), nullable=True)
    length = Column(String(250), nullable=True)
    max_speed = Column(String(250), nullable=True)
    cargo_capacity = Column(String(250), nullable=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)    
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
