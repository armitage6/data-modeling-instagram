import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    las_name = Column(String(40), nullable=False)
    gmail = Column(String(100), nullable=False)
    first_name = Column(String(40), nullable=False)
    profile = relationship("profile", back_populates="user", uselist=False)
    contacts = relationship("contacts")



class Profile(Base):
    __tablename__ = 'profile'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250))
    post = Column(String(250)) 
    followers = Column(String(250))
    followear  = Column(String(250))  
    post  = Column(String(250))   
    history  = Column(String(250))   
    user_id = Column(Integer, ForeignKey("user.id")) 
    user = relationship("user", back_populates="profile")
    post = relationship("post")



class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_name = Column(String(80))
    date = Column(String(20))
    comment = Column(String(250))
    favorite = Column(String(250))
    send = Column(String(250))
    like = Column(String(250))
    profile_id = Column(Integer, ForeignKey("profile.id"))

    
   

    def to_dict(self):
        return {}




class Contacts(Base):
    __tablename__ = 'contacts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    search = Column(String(250))  
    active = Column(String(250))   
    user_id = Column(Integer, ForeignKey("user.id"))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
