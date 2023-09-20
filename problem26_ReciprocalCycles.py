'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.1666666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for  which 1/d contains the longest recurring cycle in its decimal fraction part. 

answer: 983
'''

'''
def longDivi(numerator, denominator, rtn=''):
    if numerator % denominator == 0:
        rtn += str(numerator // denominator)
        return rtn
    else:
        numer_tmp = numerator * 10
        tmp = str(numer_tmp // denominator)
        if '0.' not in rtn:
            rtn += '0.'
        if numer_tmp < denominator:
            rtn += '0'
        if len(tmp) > 990:
            return rtn + tmp
        return longDivi(numer_tmp, denominator, rtn)
    
import re

def find_repeated_part(string):
    pattern = re.compile(r'(.+?)\1+')
    matches = pattern.finditer(string)

    repeated_part = None
    for match in matches:
        repeated_part = match.group(1)

    return repeated_part

def try_to_solve():
    tmp = 0, '', 0
    for i in range(1, 1000):
        dig_lenth = find_repeated_part(longDivi(1, i)) if find_repeated_part(longDivi(1, i)) else ''
        if len(dig_lenth) > tmp[0]:
            tmp = len(dig_lenth), dig_lenth, i
    print(tmp)
'''

def remainderSeq(dividend, divisor, remSeq=[]):
    tmp = remSeq.copy()
    rem = (dividend % divisor) * 10
    if rem in remSeq:
        return len(remSeq) - remSeq.index(rem)
    elif rem == 0:
        return 0
    else:
        tmp.append(rem)
        return remainderSeq(rem, divisor, tmp) 

if __name__ == '__main__':
    cycles, number = 0, 0
    for i in range(2, 1000):
        tmp = remainderSeq(1, i)
        if tmp > cycles:
            cycles, number = tmp, i
    print(number)