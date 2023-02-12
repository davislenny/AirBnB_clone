#!/usr/bin/python3
"""
The "review' module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class definition """
    place_id = ""
    user_id = ""
    text = ""
