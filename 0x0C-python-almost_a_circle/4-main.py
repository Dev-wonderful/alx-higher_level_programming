#!/usr/bin/python3
""" 4-main """
import unittest
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

    from tests.test_models.test_rectangle import TestRectangle

    unittest.main()