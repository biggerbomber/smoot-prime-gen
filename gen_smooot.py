from Crypto.Util.number import getPrime,isPrime





def getSmootPrime(nbits,cutoffbits=10,ensure_dim=False):
    if nbits <=cutoffbits:
        return getPrime(nbits)

    while True:
        primes = [getPrime(cutoffbits) for _ in range(nbits//cutoffbits)]
        if nbits%cutoffbits>2:
            primes+=[getPrime(nbits%cutoffbits)] 
        tot = 2
        for p in primes:
            tot*=p
        if ensure_dim:
            nb = nbits - (tot).bit_length()
            tot = tot * pow(2,nb)
        if isPrime(tot+1):
            return tot+1

    

'''
EXAMPLE
import random as rnd
from sage.all import *
print(factor(getSmootPrime(512)-1))

p =  getSmootPrime(1512)

a = Mod(rnd.randint(3,p),p)

g = Mod(2,p)

b = pow(g,a,p)

print(a)
print(b.log(g))
'''

print(getSmootPrime(512).bit_length())
print(getSmootPrime(1512).bit_length())
print(getSmootPrime(12).bit_length())
print(getSmootPrime(12212).bit_length())
