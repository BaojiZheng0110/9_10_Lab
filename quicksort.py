import random
import unittest
import sys
from median import split
    
def quicksort(l):
    if len(l) <= 1:
        return l
    l1, l0, l2 = split(l, random.choice(l))
    l1 = quicksort(l1)
    l2 = quicksort(l2)
    l1.extend(l0)
    l1.extend(l2)
    return l1

#------------------------------

class TestQuickSort(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort([6,2,5,1,9,10,7,3,8,4]), [1,2,3,4,5,6,7,8,9,10])
        for i in range(1000):
            n = random.randint(0, 100)
            l = [random.randint(0, 100000) for i in range(n)]
            ls = l[:]
            ls.sort()
            self.assertEqual(quicksort(l), ls, "Quicksort fails: %s" %(str(l)))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQuickSort)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)