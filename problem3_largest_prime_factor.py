'''
The prime factors of 13195 are 5, 7, 13 and 29. 
What is the largest prime factor the number 600851475143?

answer: 6857
'''

import math

#check if number is prime or not
def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

#retunr all prime factors of number
def prime_factors(number):
    tmp = []
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            if isPrime(i):
                tmp.append(i)
    return tmp

#return the largest prime factor of number
def largest_prime_factor(number):
    n = prime_factors(number)
    return n[len(n) - 1]

#check example
print(largest_prime_factor(13195))

print(largest_prime_factor(600851475143))