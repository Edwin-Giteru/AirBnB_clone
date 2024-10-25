#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""
import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Unittests for testing the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.test_file = "test_file.json"
        FileStorage._FileStorage__file_path = self.test_file

    def tearDown(self):
        """Clean up test environment."""
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass

    def test_all_returns_dict(self):
        """Test that all() returns the __objects dictionary."""
        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """Test that new() adds an object to the __objects dictionary."""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.assertIn("BaseModel." + base_model.id, self.storage.all().keys())

    def test_save(self):
        """Test that save() serializes __objects to the JSON file."""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, "r") as f:
            self.assertIn("BaseModel." + base_model.id, f.read())

    def test_reload(self):
        """Test that reload() deserializes the JSON file to __objects."""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel." + base_model.id, self.storage.all().keys())

    def test_reload_with_no_file(self):
        """Test that reload() does nothing if file doesn't exist."""
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_with_empty_file(self):
        """Test that reload() does nothing if file is empty."""
        with open(self.test_file, "w") as f:
            f.write("")
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_save_reload_with_all_classes(self):
        """Test save() and reload() with all supported classes."""
        classes = [User, State, Place, City, Amenity, Review]
        for cls in classes:
            instance = cls()
            self.storage.new(instance)
        self.storage.save()
        self.storage.reload()
        for cls in classes:
            self.assertTrue(any(isinstance(obj, cls) for obj in self.storage.all().values()))

if __name__ == "__main__":
    unittest.main()
