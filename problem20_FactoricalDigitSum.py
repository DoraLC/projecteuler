'''
n! means n x (n - 1) x ... x 3 x 2 x 1. 

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, 
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. 

Find the sum of the digits in the number 100!. 

answer: 648
'''

def factorial(n, dict):
    if n in dict:
        return dict[n]
    if n == 0 or n == 1:
        return 1
    rtn = n * factorial(n - 1, dict)
    dict[n] = rtn
    return rtn

def sum_of_dig(n):
    arr = str(n)
    rtn = 0
    for each in arr:
        rtn += int(each)
    return rtn

if __name__ == '__main__':
    print(sum_of_dig(factorial(100, {})))