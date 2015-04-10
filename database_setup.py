""" This should not change from project to project.
Import all modules needed
Create instance of declarative base at the beginning.
Create or connect the database and add tables and columns at the end of the file.
"""
import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()
## Add code below here ##

"""
This class code is the representation of a table with in a python class.
This extends the Base class we just created.
All of the code for our table and mapper goes here.
"""
class Restaurant(Base):
    """ Inside each class create a representation of our table in the database. __tablename__ = 'some_table' """
    __tablename__ = 'restaurant'
    """ The mapper code maps Python objects to columns in the database.  columnName = Column(attributes, ...)
        examples:
        String(250)
        Integer
        relationship(Class)
        nullable = False
        primary_key = True
        ForeignKey('some_table.id')
    """
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

class MenuItem(Base):
    """ Inside each class create a representation of our table in the database. __tablename__ = 'some_table' """
    __tablename__ = 'menu_item'
    """ The mapper code maps Python objects to columns in the database.  columnName = Column(attributes, ...) """
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    # restaurant_id tell the database to look to the Restaurant table for the id
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    # restaurant creates the connection between the MenuItem table and the Restaurant table
    restaurant = relationship(Restaurant)

## Last lines - No more code here ##
engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)