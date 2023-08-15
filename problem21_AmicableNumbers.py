'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a!= b, 
then a and b are an amicable pair and each of a and b are called amicable numbers. 

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220

Evaluate the sum of all the amicable numbers under 10000. 

answer: 31626
'''

def sum_of_factors(n):
    rtn = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            rtn += i
    return rtn

def amicable(n, m):
    if sum_of_factors(n) == m and sum_of_factors(m) == n:
        return True
    return False

def amicablePairs(n):
    rtn = []
    tmp = [0]
    for i in range(1, n):
        tmp.append(sum_of_factors(i))
    for i in range(1, n):
        for j in range(1, i):
            if tmp[i] == j and tmp[j] == i:
                rtn.append([i, j])
    return rtn

def solution(n): 
    rtn = 0
    for each in amicablePairs(n):
        for i in each:
            rtn += i
    return rtn
print(solution(10000))