'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 
3 + 3 + 5 + 4 + 4 + 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many would be used?

NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters and 155 (one hunderd and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

digit = {1: 'one', 
            2: 'two', 
            3: 'three', 
            4: 'four', 
            5: 'five', 
            6: 'six', 
            7: 'seven', 
            8: 'eight', 
            9: 'nine', 
            0: ''}

digits = {10: 'ten', 
               11: 'eleven', 
               12: 'twelve', 
               13: 'thirdteen', 
               14: 'fourteen', 
               15: 'fifteen', 
               16: 'sixteen', 
               17: 'seventeen', 
               18: 'eighteen', 
               19: 'nineteen', 
               20: 'twenty', 
               30: 'thirty', 
               40: 'forty', 
               50: 'fifty', 
               60: 'sixty', 
               70: 'seventy', 
               80: 'eighty', 
               90: 'ninety', 
               100: 'hunderd', 
               1000: 'thousand', 
               0: ''}

def numRepre(num):
    rtn = ''

    thou_dig = num // 1000
    hund_dig = num // 100
    ten_dig = num % 100
    dig = num % 10

    if thou_dig != 0:
        rtn += digit[thou_dig] + digits[1000]
    if hund_dig != 0 and hund_dig != 10:
        if thou_dig != 0:
            rtn += 'and'
        rtn += digit[hund_dig] + digits[100]
    if ten_dig >= 10:
        if hund_dig != 0 and hund_dig != 10:
            rtn += 'and'
        if ten_dig >= 20:
            rtn += digits[ten_dig // 10 * 10] + digit[dig]
        else:
            rtn += digits[ten_dig]
    if ten_dig // 10 == 0:
        if num % 100 < 10 and dig != 0 and num > 10:
            rtn += 'and'
        rtn += digit[dig]

    return rtn

def solution(start, end):
    tmp = 0
    for i in range(start, end + 1):
        tmp += len(numRepre(i))
    return tmp

