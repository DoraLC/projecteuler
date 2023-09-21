'''
Surprisingly there are only three numbers that cna be written was the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not sum it if not included. 

The sum of these numbers is 1638 + 8208 + 9474 = 19316. 

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits. 

answer: 443839
'''

def sumPow(power):
    rtn = []
    for i in range(2, 1000000):
        Sum = 0
        tmp = str(i)
        for each in tmp:
            Sum += int(each) ** power
        if Sum == i:
            rtn.append(i)
    return rtn

if __name__ == '__main__':
    print(sum(sumPow(5)))