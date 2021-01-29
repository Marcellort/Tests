from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import validates

base = declarative_base()


class Cateogry(base):
    __tablename__ = 'category'
    id = Column('id', Integer, nullable=False, primary_key=True)
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=200), nullable=True)

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError("Name isn't a String")
        if not name.strip():
            raise ValueError("Name can't receive an empty string")
        if len(name) > 100:
            raise ValueError("Name can´t receive a string more than 100 characters")
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError("Description isn't a String")
        if len(description) > 200:
            raise ValueError("Name can´t receive a string more than 100 characters")
        return description
