'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

answer: 1366
'''

def digitList(base, power):
    rtn = []
    tmp = str(base ** power)
    for each in tmp:
        rtn.append(int(each))
    return rtn.copy()

def sum_of_digits(base, power):
    tmp = digitList(base, power)
    rtn = 0
    for each in tmp:
        rtn += each
    return rtn

if __name__ == '__main__':
    print(sum_of_digits(2, 1000))