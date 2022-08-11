#!/usr/bin/python3
"""Defines unnittests for models/user.py."""
import os
import pep8
import models
import MySQLdb
import unittest
from datetime import datetime
from models.base_model import Base, BaseModel
from models.user import User
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker


class TestUser(unittest.TestCase):
    """Unittests for testing the User class"""

    @classmethod
    def setUpClass(cls):
        """User testing setup.
        Temporarily renames any existing file.json.
        Resets FileStorage objects dictionary.
        Creates FileStorage, DBStorage and User instances for testing.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.filestorage = FileStorage()
        cls.user = User(email="poppy@holberton.com", password="betty98")

        if type(models.storage) == DBStorage:
            cls.dbstorage = DBStorage()
            Base.metadata.create_all(cls.dbstorage._DBStorage__engine)
            Session = sessionmaker(bind=cls.dbstorage._DBStorage__engine)
            cls.dbstorage._DBStorage__session = Session()

    @classmethod
    def tearDownClass(cls):
        """User testing teardown.
        Restore original file.json.
        Delete the FileStorage, DBStorage and User test instances.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.user
        del cls.filestorage
        if type(models.storage) == DBStorage:
            cls.dbstorage._DBStorage__session.close()
            del cls.dbstorage

    def test_pep8(self):
        """Test pep8 styling"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/user.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attributes(self):
        usr = User(email="a", password="a")
        self.assertEqual(str, type(usr.id))
        self.assertEqual(datetime, type(usr.created_at))
        self.assertEqual(datetime, type(usr.updated_at))
        self.assertTrue(hasattr, (usr, "__tablename__"))
        self.assertTrue(hasattr, (usr, "email"))
        self.assertTrue(hasattr, (usr, "password"))
        self.assertTrue(hasattr, (usr, "first_name"))
        self.assertTrue(hasattr, (usr, "last_name"))
        self.assertTrue(hasattr, (usr, "places"))
        self.assertTrue(hasattr, (usr, "reviews"))

    def test_first_name(self):
        """Testing type of first_name"""
        User.first_name = "Arenc"
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        """Testing type of last_name"""

        User.last_name = "Palluqi"
        self.assertEqual(str, type(User.last_name))

    def test_docstring(self):
        """Testing if file has docstring or not"""
        self.assertIsNotNone(User.__doc__)


if __name__ == "__main__":
    unittest.main()
