import math

def gcd(a, b) :
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("must be integer")
    if a < 0 or b < 0:
        raise ValueError("must be non-negative")


    if b == 0:
        return a
    else:
        c = a % b
        return gcd(b, c)



def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)

    g, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return (g, x, y)



def mod_inverse(e, phi):
    g, x, y = extended_gcd(e, phi)

    if g != 1:
        raise ValueError("inverse does not exist")
    
    d = x % phi

    return d


    

def rsa_keygen(p, q, e) :
    n = p * q
    phi = (p-1) * (q-1)

    if gcd(e, phi) != 1:
        raise ValueError("e and phi are not coprime")

    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key, phi


def  rsa_encrypt(m, public_key):
    e, n = public_key
    c = pow(m, e, n)
    return c

def rsa_decrypt(c, private_key):
    d, n = private_key
    m = pow(c, d, n)
    return m


def main():          # this is the test
    p = 61
    q = 53
    e = 17

    public_key, private_key, phi = rsa_keygen(p, q, e)
    n = p * q


    print("n = ", n)
    print("phi = ", phi)
    print("punlic key = ", public_key)
    print("private key = ", private_key)
    print()

    grades = [92, 7, 100]

    for g in grades:
        c = rsa_encrypt(g, public_key)
        m = rsa_decrypt(c, private_key)

        print("Grade: ", g)
        print("Encrypt: ", c)
        print("Decrypt: ", m)

        if m == g:
            print("Correct\n")
        else: 
            print("Error\n")

if __name__ == "__main__":
    main()
