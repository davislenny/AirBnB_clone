#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''testing file storage'''

    @classmethod
    def setUpClass(cls):
        cls.rev1 = Review()
        cls.rev1.place_id = "Helcat"
        cls.rev1.user_id = "epegxt"
        cls.rev1.text = "5*"

    @classmethod
    def teardown(cls):
        del cls.rev1

    def teardown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_all(self):
        """
        Tests method: all (returns dictionary <class>.<id> : <obj instance>)
        """
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)

    def test_new(self):
        """
        Tests method: new (saves new object into dictionary)
        """
        _instance = FileStorage()
        _dic = _instance.all()
        alx = User()
        alx.id = 103040
        alx.name = "alx"
        _instance.new(alx)
        key = alx.__class__.__name__ + "." + str(alx.id)
        self.assertIsNotNone(_dic[key])

    def test_reload(self):
        """
        Tests method: reload (reloads objects from string file)
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except Exception:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)

    def test_save(self):
        """ Tests that a file gets created with the name file.json """
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_reload(self):
        """ Reload without file """
        try:
            self.storage.reload()
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)
