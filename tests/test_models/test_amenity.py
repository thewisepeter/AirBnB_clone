#!/usr/bin/python3
# Tests for class Amenity
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    def test_name_default_value(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_name_assignment(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_save_method(self):
        amenity = Amenity()
        initial_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, initial_updated_at)


if __name__ == '__main__':
    unittest.main()
