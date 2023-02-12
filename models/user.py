#!/usr/bin/python3
"""
The 'user' module
Defines class 'User'
"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """ Class definition """
    email = ""
    pasword = ""
    firsr_name = ""
    last_name = ""
