import random
import unittest
import sys
import numeric_operations as numops
import modular_operations as modops
import primes

#------------------------------

def gen_keys(n):
    p = primes.random_prime_bits(n, 10)
    q = primes.random_prime_bits(n, 10)
    pq = numops.num_mult(p, q)
    p1q1 = numops.num_mult(numops.num_sub(p, [1]), 
                           numops.num_sub(q, [1]))
    e = [1, 1]
    while True:
        try:
            d = modops.mod_num_inv(e, p1q1)
            return ((pq, e), d)
        except ZeroDivisionError:
            e = numops.num_add(e, [1, 0])

#------------------------------

def rsa_encode(m, pubkey):
    N, e = pubkey
    return modops.mod_num_pow(m, e, N)

def rsa_decode(em, pubkey, privkey):
    N, e = pubkey
    d = privkey
    return modops.mod_num_pow(em, d, N)

#------------------------------

class TestRsaFunctions(unittest.TestCase):
    def setUp(self):
        (self.pubkey, self.privkey) = gen_keys(20)
    def test_rsa_encode_decode(self):
        n = numops.int_to_vec(55)
        e = numops.int_to_vec(3)
        d = numops.int_to_vec(27)
        em = rsa_encode(numops.int_to_vec(13), (n, e))
        self.assertEqual(numops.strip_zeros(em), numops.int_to_vec(52))
        m = rsa_decode(em, (n, e), d)
        self.assertEqual(numops.strip_zeros(m), numops.int_to_vec(13))
        for i in range(1000):
            m = random.randint(0, 100000) % numops.vec_to_int(self.pubkey[0])
            mv = numops.int_to_vec(m)
            emv = rsa_encode(mv, self.pubkey)
            demv = rsa_decode(emv, self.pubkey, self.privkey)
            self.assertEqual(numops.strip_zeros(mv), numops.strip_zeros(demv))
                       

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRsaFunctions)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)
