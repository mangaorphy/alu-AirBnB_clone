#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time

class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        """Test that a BaseModel instance is created correctly."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_id_is_string(self):
        """Test that the id is a string."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_initialization(self):
        """Test that updated_at is initialized correctly."""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test that save() updates the updated_at attribute."""
        model = BaseModel()
        old_updated_at = model.updated_at
        time.sleep(1)  # Wait for a second to ensure the timestamp changes
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict(self):
        """Test that to_dict() returns a dictionary representation of the instance."""
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 42
        model_dict = model.to_dict()
        
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], "Test Model")
        self.assertEqual(model_dict['my_number'], 42)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertIsInstance(model_dict['id'], str)

    def test_str_method(self):
        """Test the __str__ method."""
        model = BaseModel()
        self.assertEqual(str(model), f"[BaseModel] ({model.id}) {model.__dict__}")

if __name__ == "__main__":
    unittest.main()