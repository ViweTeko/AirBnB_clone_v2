#!/usr/bin/python3
""" Unit test for Place"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os


class test_Place(test_basemodel):
    """ Place test class"""

    def __init__(self, *args, **kwargs):
        """ Initialize Place test"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ City id test"""
        new = self.value()
        self.assertEqual(type(new.city_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_user_id(self):
        """ User id test"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_name(self):
        """ Name test"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_description(self):
        """ Description test"""
        new = self.value()
        self.assertEqual(type(new.description), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_number_rooms(self):
        """ Num Rooms test"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_number_bathrooms(self):
        """ Num bathrooms test"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_max_guest(self):
        """ Max Guest Test"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_price_by_night(self):
        """ Price by Night test"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_latitude(self):
        """ Latitude test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_longitude(self):
        """ Longitude test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_amenity_ids(self):
        """ Amenity id test"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))
