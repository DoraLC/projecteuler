'''
A palindromic number reads the same both ways. The largest palindrome made from the prodect of two 2-digit number is

9009 = 91 * 99

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def checkPalindromic(number):
    tmp = [int(n) for n in str(number)]
    for i in range(0, len(tmp) // 2):
        if tmp[i] != tmp[len(tmp) - i - 1]:
            return False
    return True

def findLargestPalindromic(digit):
    n = 10 ** digit - 1
    tmp = 0
    for i in range(n, 1, -1):
        for j in range(1, i):
            k = i * j
            if checkPalindromic(k) and k > tmp:
                tmp = k
    return tmp

print(findLargestPalindromic(3))