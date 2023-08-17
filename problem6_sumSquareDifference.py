'''
The sum of the squars of the first ten narural numbers is, 

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is, 

(1 + 2 + ... + 10)^2 = 55^2 = 025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

answer: 25164150
'''

def sum_of_squares(n):
    rtn = 0
    for i in range(1, n + 1):
        rtn += i ** 2
    return rtn

def sum_of_squaresNumbers(n):
    rtn = 0
    for i in range(1, n + 1):
        rtn += i
    return rtn ** 2

def diff_sumSqrt_sumSqrtNum(n):
    return sum_of_squaresNumbers(n) - sum_of_squares(n)

if __name__ == '__main__':
    print(diff_sumSqrt_sumSqrtNum(100))