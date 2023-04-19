import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rect_arg(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(3, 5)
        r3 = Rectangle
        self.assertEqual(r1.id, r2.id - 1)
        self.assertRaises(TypeError, r3, "t", 2)
        self.assertRaises(TypeError, r3, 1, "t")
        self.assertRaises(TypeError, r3, 1, 2, "t")
        self.assertRaises(TypeError, r3, 1, 2, 3, "t")
        self.assertRaises(ValueError, r3, 0, 2)
        self.assertRaises(ValueError, r3, 1, 0)
        self.assertRaises(ValueError, r3, 1, 2, -1)
        self.assertRaises(ValueError, r3, 1, 2, 3, -1)


if __name__ == '__main__':
    unittest.main()
