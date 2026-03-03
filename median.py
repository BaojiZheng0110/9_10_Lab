import random
import unittest
import sys
    
def split(l, x):
    l1 = []
    l2 = []
    l0 = []
    for y in l:
        if y < x:
            l1.append(y)
        elif y > x:
            l2.append(y)
        else:
            l0.append(y)
    return l1, l0, l2
    
def select(l, k):
    if len(l) == 0:
        return None
    if len(l) == 1:
        if k == 0:
            return l[0]
        else:
            return None
    l1, l0, l2 = split(l, random.choice(l))
    if len(l1) > k:
        return select(l1, k)
    if len(l1)+len(l0) > k:
        return l0[0]
    return select(l2, k-len(l1)-len(l0))

def median(l):
    return select(l, len(l)//2)    

#------------------------------

class TestMedian(unittest.TestCase):
    def test_split(self):
        self.assertEqual(split([1,3,2,5,6], 2), ([1], [2], [3,5,6]))
        for i in range(1000):
            n = random.randint(0, 100)
            l = [random.randint(0, 100000) for i in range(n)]
            x = random.randint(0, 100000)
            l1, l0, l2 = split(l, x)
            if len(l1) > 0:
                self.assertTrue(max(l1) < x, "Split fails on %d against %s" % (x, str(l)))            
            if len(l0) > 0:
                self.assertTrue(min(l0) == x, "Split fails on %d against %s" % (x, str(l)))            
                self.assertTrue(max(l0) == x, "Split fails on %d against %s" % (x, str(l)))            
            if len(l2) > 0:
                self.assertTrue(min(l2) > x, "Split fails on %d against %s" % (x, str(l)))            
    def test_select(self):
        self.assertEqual(select([1,3,2,5,6], 3), 5)
        for i in range(1000):
            n = random.randint(1, 100)
            l = [random.randint(0, 100000) for i in range(n)]
            k = random.randint(0, n-1)
            lsort = l[:]
            lsort.sort()
            sel = lsort[k]
            self.assertEqual(select(l,k), sel, "Select fails on %d out of %s" % (k, str(l)))            
    def test_median(self):
        self.assertEqual(median([1,3,2,5,6]), 3)
        for i in range(1000):
            n = random.randint(1, 100)
            l = [random.randint(0, 100000) for i in range(n)]
            lsort = l[:]
            lsort.sort()
            med = lsort[len(l)//2]
            self.assertEqual(median(l), med, "Median fails on %s" % (str(l)))            

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMedian)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)