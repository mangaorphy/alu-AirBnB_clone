#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_create(self):
        """Test creation of a new BaseModel instance."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_str(self):
        """Test the __str__ method."""
        my_model = BaseModel()
        expected_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_str)

    def test_to_dict(self):
        """Test the to_dict method."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        model_dict = my_model.to_dict()
        self.assertEqual(model_dict['name'], "My First Model")
        self.assertEqual(model_dict['my_number'], 89)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
