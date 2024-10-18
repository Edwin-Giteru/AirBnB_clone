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




