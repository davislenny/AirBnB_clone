#!/usr/bin/python3
""" FileStorage autoinit """
from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
