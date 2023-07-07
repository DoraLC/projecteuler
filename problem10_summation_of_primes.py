'''
The sum of the primes below 10 is 2 + 3 + 5 +7 = 17
Find the sum of all the primes below two million. 

answer: 142913828922
'''

import math

#check if @number is prime or not
def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

def sum_of_primes(n):
    rtn = 0
    for i in range(1, n):
        if isPrime(i):
            rtn += i
    return rtn

print(sum_of_primes(2000000))