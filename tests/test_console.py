#!/usr/bin/python3
"""Unittest for console.py

"""
import unittest
from ..console import HBNBCommand
import os


class TestAirbnbClone_prompting(unittest.TestCase):
    """
    Unittests for testing the console.py file
    """

    @classmethod
    def setUpClass(cls):
        """Set up class method for the test cases"""
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method for the test cases
        Delete the file.json created
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
