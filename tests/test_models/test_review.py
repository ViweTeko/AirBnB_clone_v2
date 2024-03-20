#!/usr/bin/python3
""" Unit test for Reviews"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import os


class test_review(test_basemodel):
    """ Reviews test"""

    def __init__(self, *args, **kwargs):
        """ Initialize Review"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Place id test"""
        new = self.value()
        self.assertEqual(type(new.place_id), strif
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_user_id(self):
        """ User id test"""
        new = self.value()
        self.assertEqual(type(new.user_id), strif
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_text(self):
        """ Text test"""
        new = self.value()
        self.assertEqual(type(new.text), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))
