'''
By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
'''

'''
answer: 104743
'''

import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    count = 0
    number = 0

    while True:
        if isPrime(number):
            count += 1
            if count == 10001:
                print(number)
                break
        number += 1