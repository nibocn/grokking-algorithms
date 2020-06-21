import unittest
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        index = binary_search([1, 3, 7, 9, 12], 1)
        self.assertEqual(index, 0)
        index = binary_search([1, 3, 7, 9, 12], -1)
        self.assertEqual(index, None)
        index = binary_search([1, 3, 7, 9, 12], 12)
        self.assertEqual(index, 4)


if __name__ == '__main__':
    unittest.main()
