#!/usr/bin/python3
""" 5-main """
import unittest
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

    from tests.test_models.test_rectangle import TestRectangle

    unittest.main()