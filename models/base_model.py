#!/usr/bin/python3

''' A class that defines all common attributes/methods for other classes'''
import uuid
from datetime import datetime
import models


class BaseModel:

    def __init__(self, *args, **kwargs):

        if kwargs:
            for key,value in kwargs.items():
                if key == '__class__':
                    continue

                elif key == 'created_at' or key == 'update_at':
                    setattr(self,key,datetime.strftime
                            (value,'%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self,key,value)
            self.id = str(uuid.uuid4())
        else:
           self.id = str(uuid.uuid4())
           self.created_at = datetime.now()
           self.updated_at = datetime.now()

           models.storage.new(self)

    def __str__(self):

        return '[{}] ({}) {}'.format(self.__class__.__name__,self.id,self.__dict__)

    def save(self):
        '''updates the 'updated_at' attribute with the
        current datetime to the JSON file'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary representation of the obj'''
        result = self.__dict__.copy()

        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()

        return result

    @classmethod
    def from_dict(cls, data):
        """
        Recreates a BaseModel instance from a dictionary representation.
        """
        if '__class__' in data:
            class_name = data['__class__']
            if class_name == cls.__name__:
                if 'created_at' in data:
                    data['created_at'] = data['created_at']

                if 'updated_at' in data:
                    data['updated_at'] = data['updated_at']

                return cls(**data)
        return None

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        class_name = self.__class__.__name__
    
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    
    def __iter__(self):
        self.attribute_values = list(self.__dict__.values())
        self._index = 0
        return self
    
    def __next__(self):
        if not hasattr(self, '_index'):
            raise StopIteration

        if self._index < len(self.attribute_values):
            result = self.attribute_values[self._index]
            self._index += 1

            # Check if the attribute is a datetime object and format it
            if isinstance(result, datetime):
                result = result.isoformat()

            return result
        else:
            raise StopIteration


