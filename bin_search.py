import random
import unittest
import sys

def bin_search(l, k):
    if len(l) == 0:
        return None
    m = len(l)//2
    if l[m] == k:
        return m
    elif l[m] < k:
        idx = bin_search(l[(m+1):], k)
        if idx is None:
            return None
        return m+1+idx
    else:
        return bin_search(l[:m], k)
    
#------------------------------

class TestBinSearch(unittest.TestCase):
    def test_bin_search(self):
        self.assertEqual(bin_search([1,2,3,4,5,6,7,8,9,10], 4), 3)
        self.assertEqual(bin_search([1,2,3,5,6,7,8,9,10], 4), None)
        for i in range(1000):
            n = random.randint(0, 100)
            l = [random.randint(0, 100000)]
            for j in range(n):
                 l.append(random.randint(l[-1], l[-1]+100000))
            k = random.randint(0, n)
            self.assertEqual(bin_search(l, l[k]), k, "Binary search failed: %d in %s" %(l[k], str(l)))
            k = random.randint(0, l[-1]+100000)
            ik = bin_search(l, k)
            if k in l:
                self.assertEqual(l[ik], k, "Binary search failed: %d in %s" %(k, str(l)))
            else:
                self.assertEqual(ik, None, "Binary search failed: %d not in %s" %(k, str(l)))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBinSearch)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)