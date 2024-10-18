#!/usr/bin/python3
""" creating a class Review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
