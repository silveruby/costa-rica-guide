import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    # Serialize
    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'picture': self.picture
        }


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    item = relationship('Item', cascade="all, delete-orphan")

    # Serialize
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    image = Column(String(250))
    description = Column(String(1000))
    notes = Column(String(1000))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    comment = relationship('Comment', cascade="all, delete-orphan")

    # Serialize
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'notes': self.notes
        }


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    date = Column(Date, nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'))
    item = relationship(Item)
    user_id = Column(Integer, ForeignKey('user.id'))
    username = Column(String(250))
    user = relationship(User)

    # Serialize
    @property
    def serialize(self):
        return {
            'id': self.id,
            'text': self.text
        }

#engine = create_engine('sqlite:///rubyscostarica.db')
engine = create_engine('postgres://pdiklqkuhjdrnx:upgNacOIGqj7Wn45DtVJygSMB6@ec2-54-197-253-142.compute-1.amazonaws.com:5432/d28h82c038hd3s')

Base.metadata.create_all(engine)
