import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Apellido = Column(String(50))
    Email = Column(String(50))
    Contraseña = Column(String(250))
class Follower(Base):
    __tablename__='Follower'
    id = Column(Integer, primary_key=True)
    User_from_id =Column(Integer,ForeignKey('User.id'))
    User_to_id =Column(Integer,ForeignKey('User.id'))
    follower = relationship(User)
class Post(Base):
    __tablename__='Post'
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)

class Media(Base):
    __tablename__='Media'
    id = Column(Integer, primary_key=True)
    url = Column(String(50))
    post_id = Column(Integer, ForeignKey('Post.id'))
    User = relationship(User)
    Post = relationship(Post)

class Comment(Base):
    __tablename__= 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(50))
    author_id = Column(Integer, ForeignKey('User.id'))
    post_id = Column(Integer, ForeignKey('Post.id')) 
    commet = relationship(User)
    commets = relationship(Post)


# Draw from SQLAlchemy base

render_er(Base, 'diagram.png')
