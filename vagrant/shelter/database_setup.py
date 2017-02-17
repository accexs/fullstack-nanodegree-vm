import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Date

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):

	__tablename__ = 'shelter'
	id = Column(Integer, primary_key=True)
	name = Column(String(100))
	adress = Column(String(500), nullable=True)
	city = Column(String(100))
	state = Column(String(100))
	zipCode = Column(Integer)
	website = Column(String(100))

class Puppy(Base):

	__tablename__ = 'puppy'
	id = Column(Integer, primary_key=True)
	name = Column(String(100))
	birthDate = Column(Date(), nullable=True)
	gender = Column(String(1), nullable=True)
	weight = Column(String(2), nullable=True)
	picture = Column(String(100), nullable=True)


engine = create_engine('sqlite:///shelter.db')

Base.metadata.create_all(engine)