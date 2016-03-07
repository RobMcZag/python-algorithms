import unittest
import random
import sort

class SortTest(unittest.TestCase):

    def testLessOnStrings(self):
        self.assertEqual(True, "a" < "b")

    def testSwapOnNonEmptyList(self):
        l = [1, 2, 3]
        sort.swap(l, 1, 2)
        self.assertEqual(l, [1, 3, 2])

    def testSwapOnNonEmptyListOfStrings(self):
        l = ["a", "b", "c"]
        sort.swap(l, 1, 2)
        self.assertEqual(l, ["a", "c", "b"])

    def testInsertionSort(self):
        l = [2, 3, 1]
        sort.insertion(l)
        self.assertEqual(l, [1, 2, 3])

    def testMergeSort(self):
        l = [2, 3, 1]
        sort.mergesort(l)
        self.assertEqual(l, [1, 2, 3])

    def testMergeSort2(self):
        l = [2, 3, 1, 7, 8, 1 , 8 , 8, 2, 1 ,7]
        sort.mergesort(l)
        self.assertEqual(l, [1, 1, 1, 2, 2, 3, 7, 7, 8, 8, 8])

    def testMergeSort3(self):
        ol = range(-50, 50)
        l = sorted(ol)
        sort.mergesort(l)
        self.assertEqual(l, ol)

    def testMergeSortWithManyDuplicates(self):
        ol = range(-50, 50)
        ol.extend(ol)
        l = ol[:]
        sort.mergesort(l)
        self.assertEqual(l, sorted(ol))

    def testQuickSort(self):
        l = [2, 3, 1]
        sort.quicksort(l)
        self.assertEqual(l, [1, 2, 3])

    def testQuickSort2(self):
        l = [2, 3, 1, 7, 8, 1 , 8 , 8, 2, 1 ,7]
        sort.quicksort(l)
        self.assertEqual(l, [1, 1, 1, 2, 2, 3, 7, 7, 8, 8, 8])

    def testQuickSort3(self):
        ol = range(-50, 50)
        l = sorted(ol)
        sort.quicksort(l)
        self.assertEqual(l, ol)

    def testQuickSortWithManyDuplicates(self):
        ol = range(-50, 50)
        ol.extend(ol)
        l = ol[:]
        sort.quicksort(l)
        self.assertEqual(l, sorted(ol))

if __name__ == '__main__':
    unittest.main()
