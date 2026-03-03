import random
import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../ch01')
import numeric_operations as numops

def num_fast_mult(x, y):
    n = max(len(x), len(y))
    if n <= 3:
        return numops.num_mult(x, y)
    n2 = n//2
    xl, xr = x[:-n2], x[-n2:]
    yl, yr = y[:-n2], y[-n2:]
    p1 = num_fast_mult(xl, yl)
    p2 = num_fast_mult(xr, yr)
    p3 = num_fast_mult(numops.num_add(xl,xr), 
                       numops.num_add(yl,yr))
    p3 = numops.num_sub(p3, p1)
    p3 = numops.num_sub(p3, p2)
    p1.extend([0 for i in range(2*n2)])
    p3.extend([0 for i in range(n2)])
    return numops.num_add(p1, numops.num_add(p2, p3))
    

#------------------------------

class TestFastIntMult(unittest.TestCase):
    def test_num_fast_mult(self):
        self.assertEqual(numops.strip_zeros(num_fast_mult([1, 1, 0, 1], [1, 0, 1, 1])), [1, 0, 0, 0, 1, 1, 1, 1])
        self.assertEqual(numops.strip_zeros(num_fast_mult([1, 0, 1, 1], [1, 1, 0, 1])), [1, 0, 0, 0, 1, 1, 1, 1])
        self.assertEqual(numops.vec_to_int(num_fast_mult(numops.int_to_vec(9730), numops.int_to_vec(2542))), 9730*2542)
        for i in range(1000):
            a = random.randint(0, 100000)
            b = random.randint(0, 100000)
            x = numops.int_to_vec(a)
            y = numops.int_to_vec(b)
            z = num_fast_mult(x, y)
            self.assertEqual(numops.vec_to_int(z), a*b, "a*b failed: %d*%d != %d" %(a,b,a*b))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFastIntMult)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)