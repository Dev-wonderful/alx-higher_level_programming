import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(20)
        self.assertEqual(b1.id, b2.id - 1)  # add assertion here
        self.assertEqual(b3.id, 20)


if __name__ == '__main__':
    unittest.main()
