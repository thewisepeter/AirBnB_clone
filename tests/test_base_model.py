#!/usr/bin/python3
# test module for the class BaseModel
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    # Test for the BaseModel class instantiation

    def test_base_model_attributes(self):
        """ test the attributes of the BaseModel Class"""

        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, "id"))
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_base_model_save(self):
        """Test the save method of the BaseModel class"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, old_updated_at)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_base_model_to_dict(self):
        """Test the to_dict method of the BaseModel class"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["created_at"], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.updated_at.isoformat())
        self.assertEqual(my_model_dict["name"], "My First Model")
        self.assertEqual(my_model_dict["my_number"], 89)
        self.assertEqual(my_model_dict["__class__"], "BaseModel")

    def test_TwoInstance(self):
        """ Test to compare 2 instances of BaseModel """
        my_model_1 = BaseModel()
        my_model_2 = BaseModel()
        self.assertNotEqual(my_model_1.id, my_model_2.id)

if __name__ == "__main__":
    unittest.main()
