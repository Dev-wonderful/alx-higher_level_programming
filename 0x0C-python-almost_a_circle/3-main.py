#!/usr/bin/python3
""" 3-main """
import unittest
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

    from tests.test_models.test_rectangle import TestRectangle

    unittest.main()
