#!/usr/bin/python3
""" Unit test for City"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import os


class test_City(test_basemodel):
    """ City test class"""

    def __init__(self, *args, **kwargs):
        """ Initialize City test"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ State id test"""
        new = self.value()
        self.assertEqual(type(new.state_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_name(self):
        """ Name test"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))
