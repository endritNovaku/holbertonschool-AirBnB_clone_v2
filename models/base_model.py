#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models
    Attributes: id, created_at, updated_at
    """
    id = Column(String(60), primary_key=True,
                nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        dictionary = self.__dict__.copy()
        dictionary.pop("_sa_instance_state", None)
        return '[{}] ({}) {}'.format(type(self).__name__, self.id, dictionary)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """To delete the current instance from the storage"""
        models.storage.delete(self)
