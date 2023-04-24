import unittest
from models.base import Base

"""This is a workaround relative path not working"""
# import os
# from importlib.machinery import SourceFileLoader
# # get the directory path and work my way backwards to the main parent directory
# test_models_dir = os.path.dirname(__file__)
# tests_dir = os.path.abspath(os.path.join(test_models_dir, os.pardir))
#
# # get the path for the module to be loaded and load it
# base_py_file_path = os.path.abspath(os.path.join(tests_dir, os.pardir, 'models/base.py'))
# Base = (SourceFileLoader("base", base_py_file_path).load_module()).Base


class TestBase(unittest.TestCase):

    def test_instance(self):
        b1 = Base()
        self.assertIsInstance(b1, Base)

    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(20)
        self.assertEqual(b1.id, b2.id - 1)  # add assertion here
        self.assertEqual(b3.id, 20)


if __name__ == '__main__':
    unittest.main()
