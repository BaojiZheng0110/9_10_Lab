import random
import unittest
import sys
import numeric_operations as numops
import modular_operations as modops

#------------------------------
def random_bits(n):
    return [ 0 if random.random()<.5 else 1 for i in range(n) ]

def random_upto(x):
    while True:
        z = random_bits(len(x))
        if numops.num_cmp(z, x) < 0:
            return z

def random_fromto(lo, hi):
    while True:
        z = random_bits(len(hi))
        if numops.num_cmp(z, lo) >= 0 and numops.num_cmp(z, hi) < 0:
            return z

#------------------------------

def is_prime_fermat(p, k):
    if numops.num_cmp(p, [1]) < 1:
        return False
    p1 = numops.num_sub(p, [1])
    for i in range(k):
        a = random_fromto([1], p)
        if numops.num_cmp(modops.mod_num_pow(a, p1, p), [1]) != 0:
            return False
    return True
    
#------------------------------

def random_prime(x, k):
    if numops.num_cmp(x, [1]) < 1:
        raise ValueError("There are no primes less than 2")
    while True:
        p = random_fromto([1, 0], x)
        if is_prime_fermat(p, k):
            return p

def random_prime_bits(n, k):
    if n <= 1:
        raise ValueError("There are no primes less than 2")
    while True:
        p = random_bits(n)
        if numops.num_cmp(p, [1, 0]) == 1:
            if is_prime_fermat(p, k):
                return p

#------------------------------

class TestPrimeFunctions(unittest.TestCase):
    def test_random_bits(self):
        bits = random_bits(4)
        self.assertEqual(len(bits), 4)
        for b in bits:
            self.assertTrue(b == 0 or b == 1)
        for i in range(1000):
            n = random.randint(0, 100000)
            bits = random_bits(n)
            self.assertEqual(len(bits), n)
            for b in bits:
                self.assertTrue(b == 0 or b == 1)
    def test_random_upto(self):
        xv = random_upto([1, 0, 0])
        self.assertEqual(numops.num_cmp(xv, [1, 0, 0]), -1)
        for i in range(1000):
            n = random.randint(0, 100000)
            nv = numops.int_to_vec(n)
            xv = random_upto(nv)
            self.assertEqual(numops.num_cmp(xv, nv), -1)
    def test_random_fromto(self):
        xv = random_fromto([1, 0, 0], [1, 0, 1, 0])
        self.assertTrue(numops.num_cmp(xv, [1, 0, 0]) >= 0)
        self.assertEqual(numops.num_cmp(xv, [1, 0, 1, 0]), -1)
        for i in range(1000):
            lo = random.randint(0, 100000)
            hi = random.randint(0, 100000)
            if lo > hi:
                lo, hi = hi, lo
            lov = numops.int_to_vec(lo)
            hiv = numops.int_to_vec(hi)
            xv = random_fromto(lov, hiv)
            self.assertTrue(numops.num_cmp(xv, lov) >= 0)
            self.assertEqual(numops.num_cmp(xv, hiv), -1)
    def test_is_prime_fermat(self):
        self.assertTrue(is_prime_fermat([1, 0, 1, 1], 1))
        self.assertTrue(is_prime_fermat([1, 0, 1, 1], 10))
        self.assertTrue(is_prime_fermat([1, 0, 1], 10))
        trials = 0
        fails = 0
        for i in range(1000):
            n = random.randint(0, 100000)
            nv = numops.int_to_vec(n)
            prime = n >= 2 and all([n%a != 0 for a in range(2, n)])
            if prime:
                self.assertTrue(is_prime_fermat(nv, 10))
            else:
                trials = trials + 1
                if is_prime_fermat(nv, 10):
                    fails = fails + 1
        self.assertTrue(fails * 2**10 <= trials,
                        "Too many failures for fermat: %d out of %d" % (fails, trials))
        print(f"Trials: {trials}, Failures: {fails}")
    def test_random_prime(self):
        for i in range(1000):
            n = random.randint(0, 100000)
            nv = numops.int_to_vec(n)
            pv = random_prime(nv, 10)
            self.assertEqual(numops.num_cmp(pv, [1]), 1)
            self.assertEqual(numops.num_cmp(pv, nv), -1)
            self.assertTrue(is_prime_fermat(pv, 15))
    def test_random_prime_bits(self):
        for i in range(1000):
            n = random.randint(2, 75)
            pv = random_prime_bits(n, 10)
            self.assertEqual(len(pv), n)
            self.assertTrue(is_prime_fermat(pv, 15))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPrimeFunctions)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)
