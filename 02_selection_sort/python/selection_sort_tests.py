#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from selection_sort import selectionSort


class TestSelectionSort(unittest.TestCase):

    def test_selection_sort(self):
        descArr = selectionSort([3, 5, 6, 2, 10])
        self.assertEqual(descArr, [2, 3, 5, 6, 10])
        descArr = selectionSort([3, 3, 6, 2, 10])
        self.assertEqual(descArr, [2, 3, 3, 6, 10])
        descArr = selectionSort([3, -23, 6, 2, 10])
        self.assertEqual(descArr, [-23, 2, 3, 6, 10])


if __name__ == '__main__':
    unittest.main()
