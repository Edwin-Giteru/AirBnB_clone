#!/usr/bin/python3
""" writing a class user that inherits from BaseModel"""
from models.base_model import BaseModel
import models


class User(BaseModel):
    """Defines the User Class that inherits from BaseModel"""
    def __init__(self, email="", password="", first_name="", last_name=""):

        """Initializes user objects"""
        super().__init__()
                              
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name  = last_name

    def __str__(self):
        return "User(email={},password={}, first_name={},last_name={})".format(
                self.email, self.password, self.first_name, self.last_name)

    @classmethod
    def all(cls):
        """Retrieve all instances of this class from storage"""
        all_objects = storage.all()
        return [obj for obj in all_objects.values() if isinstance(obj, cls)]
