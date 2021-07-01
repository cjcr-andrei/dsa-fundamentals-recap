import unittest
from source.algorithms.sorting.merge_sort import *


class TestMergeSort(unittest.TestCase):
    def test_pathological_sorts(self):
        self.assertEqual(merge_sort([0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0])
        self.assertEqual(merge_sort([1, -1, 1, -1, 1, -1]), [-1, -1, -1, 1, 1, 1])
        self.assertEqual(merge_sort([2]), [2])
        self.assertEqual(merge_sort([]), [])

    def test_regular_sorts(self):
        self.assertEqual(merge_sort([9, 2, 5, 4, 3, 10, 8, -2]), [-2, 2, 3, 4, 5, 8, 9, 10])
        self.assertEqual(merge_sort([100, 4413, 5, 12, 9999, -10000]), [-10000, 5, 12, 100, 4413, 9999])

    def test_empty_merge(self):
        self.assertEqual(merge([], []), [])
        self.assertEqual(merge([], [2, 3]), [2, 3])
        self.assertEqual(merge([2, 3], []), [2, 3])

    def test_regular_merges(self):
        self.assertEqual(merge([3], [2]), [2, 3])
        self.assertEqual(merge([2, 5], [4]), [2, 4, 5])
        self.assertEqual(merge([0, 2, 5, 5], [-1, 1, 8, 10]), [-1, 0, 1, 2, 5, 5, 8, 10])


if __name__ == '__main__':
    unittest.main()
