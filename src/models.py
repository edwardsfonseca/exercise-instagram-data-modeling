import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

""" class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person) """


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(50),ForeignKey('fvplanets.Nombre'))
    Apellido = Column(String(50))
    Email = Column(String(50))
    Correo = Column(String(50))
    Contraseña = Column(String(250))


class Personajes(Base):
    __tablename__ = 'personajes'
    personaje = Column(Integer, primary_key=True)
    Nombre = Column(String(50),ForeignKey('fvpeople.IdPeople'))
    Genero = Column(String(250))
    Mundo_natal = Column(String(50), ForeignKey('planetas.id_planetas'))
    Color_Ojos = Column(String(50))
    Raza = Column(String(250))
    rel=relationship(FvPeople)
class Planetas(Base):
    __tablename__ = 'planetas'
    id_planetas = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Poblacion = Column(Integer, primary_key=True)
    Clima = Column(String(250))
    Terreno = Column(String(250))
    rel = relationship(Personajes)
class FvPeople(Base):
    __tablename__ = 'fvpeople'
    IdPeople = Column(Integer, primary_key=True )
    Nombre = Column(String(50),ForeignKey('personajes.Nombre'))
    rel=relationship(Usuario)
    people=relationship(Personajes)

class FvPlanets(Base):
    __tablename__ = 'fvplanets'
    IdPlanets = Column(Integer, primary_key=True)
    Nombre = Column(String(50),ForeignKey('planetas.id_planetas'))
    rel=relationship(Usuario)
    planetas=relationship(Planetas)

# Draw from SQLAlchemy base

render_er(Base, 'diagram.png')
