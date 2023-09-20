'''
Euler disccovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that formula will produce 40 primes for the ocnsecutive integer values 0<= n <= 39. 
However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) is divisible by 41, and certainly when n = 41, 
41^2 + 41 + 41 is clearly divisible by 41. 

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. 
The product of the coefficients, -79 and 1601, is -126479. 

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| <= 1000

where |N| is the modules/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadraitc expression that produces the maximum number of 
primes for consevutive values of n, starting with n = 0. 

answer: -59231
'''

import math

def isPrime(num):
    n = abs(num)
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def funcOut(a, b, n):
    return n **2 + a * n + b

if __name__ == '__main__':
    tmp = 0, 0, 0
    for i in range(-1000, 1001):
        for j in range(-1000, 1001):
            for n in range(0, 1000):
                if not isPrime(funcOut(i, j, n)):
                    if tmp[0] < n:
                        tmp = n, i, j
                    break
    print('n^2 + {}n + {}'.format(tmp[1], tmp[2]))
    print(tmp[1] * tmp[2])