import random
import unittest
import sys

def int_to_vec(n):
    v = []
    while (n > 0):
        v.append(n%2)
        n = n // 2
    if len(v) == 0:
        v = [0]
    else:
        v.reverse()
    return v
    
def vec_to_int(v):
    n = 0
    for bit in v:
        n = 2*n + bit
    return n

#------------------------------

def strip_zeros(x):
    i = 0
    while i+1 < len(x) and x[i] == 0:
        i = i + 1
    return x[i:]

#------------------------------

def num_add(x, y):
    z = [ 0 for i in range(max(len(x),len(y))+1) ]
    c = 0
    for i in range(1, len(z)+1):
        a = x[-i] if i <= len(x) else 0
        b = y[-i] if i <= len(y) else 0
        z[-i] = a + b + c
        if (z[-i] >= 2):
            c, z[-i] = 1, z[-i] - 2
        else:
            c = 0
    return z
    

#------------------------------

def num_sub(x, y):
    z = [ 0 for i in range(max(len(x),len(y))+1) ]
    c = 0
    for i in range(1, len(z)+1):
        a = x[-i] if i <= len(x) else 0
        b = y[-i] if i <= len(y) else 0
        z[-i] = a - b - c
        if (z[-i] < 0):
            c, z[-i] = 1, z[-i] + 2
        else:
            c = 0
    return z
    

#------------------------------

def num_cmp(x, y):
    c = 0
    same = True
    for i in range(1, max(len(x), len(y))+1):
        a = x[-i] if i <= len(x) else 0
        b = y[-i] if i <= len(y) else 0
        if a != b:
            same = False
        z = a - b - c
        if (z < 0):
            c = 1
        else:
            c = 0
    if c != 0:
        return -1
    if same:
        return 0
    return 1
    

#------------------------------

def num_mult(x, y):
    z = [ 0 ]
    y = y[:]
    for i in range(1, len(x)+1):
        if x[-i] == 1:
            z = num_add(z, y)
        y.append(0)
    return z
    
def num_mult2(x, y):
    if len(y) == 0:
        return [0]
    z = num_mult2(x, y[:-1])
    z.append(0)
    if y[-1] == 0:
        return z
    else:
        return num_add(x, z)
    

#------------------------------

def num_div(x, y):
    if len(x) == 0:
        return ([0], [0])
    (q, r) = num_div(x[:-1], y)
    q.append(0)
    r.append(0)
    if x[-1] == 1:
        r = num_add(r, [1])
    if num_cmp(r, y) >= 0:
        q, r = num_add(q, [1]), num_sub(r, y)
    return (q, r)
    
#------------------------------

class TestNumericFunctions(unittest.TestCase):
    def test_int_vec_conversions(self):
        self.assertEqual(int_to_vec(6), [1, 1, 0])
        self.assertEqual(int_to_vec(18), [1, 0, 0, 1, 0])
        self.assertEqual(vec_to_int([1, 1, 0]), 6)
        self.assertEqual(vec_to_int([1, 0, 0, 1, 0]), 18)
        for i in range(1000):
            n = random.randint(0, 100000)
            v = int_to_vec(n)
            self.assertEqual(vec_to_int(v), n)
            
    def test_strip_zeros(self):
        self.assertEqual(strip_zeros([1, 1, 0]), [1, 1, 0])
        self.assertEqual(strip_zeros([0, 1, 1, 0]), [1, 1, 0])
        self.assertEqual(strip_zeros([0, 0, 1, 1, 0]), [1, 1, 0])
        self.assertEqual(strip_zeros([0]), [0])
        self.assertEqual(strip_zeros([0, 0]), [0])
        self.assertEqual(strip_zeros([0, 0, 0]), [0])
    
    def test_num_add(self):
        self.assertEqual(strip_zeros(num_add([1, 1, 0], [1, 0, 0, 1, 0])), [1, 1, 0, 0, 0])
        self.assertEqual(strip_zeros(num_add([1, 0, 0, 1, 0], [1, 1, 0])), [1, 1, 0, 0, 0])
        for i in range(1000):
            a = random.randint(0, 100000)
            b = random.randint(0, 100000)
            x = int_to_vec(a)
            y = int_to_vec(b)
            z = num_add(x, y)
            self.assertEqual(vec_to_int(z), a+b)
    def test_num_sub(self):
        self.assertEqual(strip_zeros(num_sub([1, 0, 0, 1, 0], [1, 1, 0])), [1, 1, 0, 0])
        self.assertEqual(strip_zeros(num_sub([1, 1, 0], [1, 1, 0])), [0])
        for i in range(1000):
            a = random.randint(0, 100000)
            b = random.randint(0, 100000)
            if a < b:
                (a, b) = (b, a)
            x = int_to_vec(a)
            y = int_to_vec(b)
            z = num_sub(x, y)
            self.assertEqual(vec_to_int(z), a-b)
    def test_num_cmp(self):
        self.assertEqual(num_cmp([1, 0, 0, 1, 0], [1, 1, 0]), 1)
        self.assertEqual(num_cmp([1, 1, 0], [1, 0, 0, 1, 0]), -1)
        self.assertEqual(num_cmp([1, 1, 0], [1, 1, 0]), 0)
        self.assertEqual(num_cmp([1, 1, 0], [0, 0, 1, 1, 0]), 0)
        for i in range(1000):
            a = random.randint(0, 100000)
            b = random.randint(0, 100000)
            x = int_to_vec(a)
            y = int_to_vec(b)
            if a < b:
                cmp = -1
            elif a > b:
                cmp = 1
            else:
                cmp = 0
            self.assertEqual(num_cmp(x, y), cmp)
    def test_num_mult(self):
        self.assertEqual(strip_zeros(num_mult([1, 1, 0, 1], [1, 0, 1, 1])), [1, 0, 0, 0, 1, 1, 1, 1])
        self.assertEqual(strip_zeros(num_mult([1, 0, 1, 1], [1, 1, 0, 1])), [1, 0, 0, 0, 1, 1, 1, 1])
        for i in range(1000):
            a = random.randint(0, 100000)
            b = random.randint(0, 100000)
            x = int_to_vec(a)
            y = int_to_vec(b)
            z = num_mult(x, y)
            self.assertEqual(vec_to_int(z), a*b)
    def test_num_mult2(self):
        self.assertEqual(strip_zeros(num_mult2([1, 1, 0, 1], [1, 0, 1, 1])), [1, 0, 0, 0, 1, 1, 1, 1])
        self.assertEqual(strip_zeros(num_mult2([1, 0, 1, 1], [1, 1, 0, 1])), [1, 0, 0, 0, 1, 1, 1, 1])
        for i in range(1000):
            a = random.randint(0, 100000)
            b = random.randint(0, 100000)
            x = int_to_vec(a)
            y = int_to_vec(b)
            z = num_mult2(x, y)
            self.assertEqual(vec_to_int(z), a*b)
    def test_num_div(self):
        (q, r) = num_div([1, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 1])
        self.assertEqual((strip_zeros(q), strip_zeros(r)), ([1, 0, 1, 1], [0]))
        (q, r) = num_div([1, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 1])
        self.assertEqual((strip_zeros(q), strip_zeros(r)), ([1, 0, 1, 1], [0]))
        (q, r) = num_div([1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 1, 0])
        self.assertEqual((strip_zeros(q), strip_zeros(r)), ([1, 1, 1, 0], [1, 1]))
        for i in range(1000):
            a = random.randint(0, 100000)
            b = random.randint(0, 100000)
            x = int_to_vec(a)
            y = int_to_vec(b)
            (q, r) = num_div(x, y)
            self.assertEqual((vec_to_int(q), vec_to_int(r)), (a//b, a%b))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNumericFunctions)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)