#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):

    def test_save_and_reload(self):
        """Test saving and reloading BaseModel instances."""
        # Clear any existing file
        if os.path.exists('file.json'):
            os.remove('file.json')

        # Create a new BaseModel instance
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()  # Save to storage

        # Reload objects from file
        all_objs = storage.all()
        self.assertIn(f"BaseModel.{my_model.id}", all_objs)  # Check if object is in storage

        # Verify the values
        loaded_model = all_objs[f"BaseModel.{my_model.id}"]
        self.assertEqual(loaded_model.name, "My_First_Model")
        self.assertEqual(loaded_model.my_number, 89)

    def test_reload_empty(self):
        """Test reload method when file does not exist."""
        if os.path.exists('file.json'):
            os.remove('file.json')
        
        storage.reload()  # Should not raise an error

if __name__ == "__main__":
    unittest.main()
    