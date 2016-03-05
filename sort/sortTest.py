import unittest
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
        sort.merge(l)
        self.assertEqual(l, [1, 2, 3])

    def testMergeSort2(self):
        l = [2, 3, 1, 7, 8, 1 , 8 , 8, 2, 1 ,7]
        sort.merge(l)
        self.assertEqual(l, [1, 1, 1, 2, 2, 3, 7, 7, 8, 8, 8])


if __name__ == '__main__':
    unittest.main()
