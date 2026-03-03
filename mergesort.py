import random
import unittest
import sys

# Note: This version of merge is slow, because of the call
# to l.insert(0,...). That's deliberate, to prove a point

def merge(l1, l2):
    if len(l1) == 0:
        return l2[:]
    if len(l2) == 0:
        return l1[:]
    if l1[0] < l2[0]:
        l = merge(l1[1:], l2)
        l.insert(0, l1[0])
    else:
        l = merge(l1, l2[1:])
        l.insert(0, l2[0])
    return l
    
def split(l):
    n2 = len(l)//2
    return l[:n2], l[n2:]
    
def mergesort(l):
    if len(l) <= 1:
        return l
    l1, l2 = split(l)
    l1 = mergesort(l1)
    l2 = mergesort(l2)
    return merge(l1, l2)

#------------------------------

class TestMergeSort(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge([1,2,3,4,5], [6,7,8,9,10]), [1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(merge([1,3,6], [2,4,5,7]), [1,2,3,4,5,6,7])
        for i in range(1000):
            n1 = random.randint(0, 100)
            l1 = [random.randint(0, 100000) for i in range(n1)]
            l1.sort()
            n2 = random.randint(0, 100)
            l2 = [random.randint(0, 100000) for i in range(n2)]
            l2.sort()
            l = l1[:]
            l.extend(l2)
            l.sort()
            self.assertEqual(merge(l1, l2), l, "Merge fails: %s and %s" %(str(l1), str(l2)))
    def test_split(self):
        self.assertEqual(split([1,2,3,4,5,6,7,8,9,10]), ([1,2,3,4,5],[6,7,8,9,10]))
        for i in range(1000):
            n1 = random.randint(0, 100)
            l = [random.randint(0, 100000) for i in range(n1)]
            l1, l2 = split(l)
            self.assertTrue(abs(len(l1)-len(l2)) <= 1, "Split fails length test: %s and %s" %(str(l1), str(l2)))
            ll = l1[:]
            ll.extend(l2)
            self.assertEqual(ll, l, "Split fails concat test: %s and %s" %(str(l1), str(l2)))
    def test_mergesort(self):
        self.assertEqual(mergesort([6,2,5,1,9,10,7,3,8,4]), [1,2,3,4,5,6,7,8,9,10])
        for i in range(1000):
            n = random.randint(0, 100)
            l = [random.randint(0, 100000) for i in range(n)]
            ls = l[:]
            ls.sort()
            self.assertEqual(mergesort(l), ls, "Mergesort fails: %s" %(str(l)))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMergeSort)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)