'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sumof the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 + 28, 
which means that 28 is a perfect number. 

A numbers n is called deficient if the sum of its proper divisors is less than n and it is called abundant 
if this sum exceeds n. 

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis 
even though it is known that the  greatest number 
that cannot be expressed as the sum of two abundant numbers is less than this limit. 

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. 
answer: 4179871
'''

def sum_of_factors(n):
    rtn = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            rtn += i
    return rtn

def abundant(n):
    if sum_of_factors(n) > n:
        return True
    return False

def solution():
    abundant_list = [i for i in range(12, 28123) if abundant(i)]

    #non_abundant = [i for i in range(1, 28123) if not abundant(i)]

    abundant_pair = []
    for i in abundant_list:
        for j in abundant_list:
            _sum = i + j
            if _sum > 28123:
                break
            abundant_pair.append(_sum)

    target = set(range(1, 28124)) - set(abundant_pair)
    print(sum(target))

if __name__ == '__main__':
    solution()