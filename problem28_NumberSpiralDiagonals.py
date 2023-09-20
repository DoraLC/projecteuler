'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101. 
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

answer: 669171001
'''

def diaSeq(size):
    rtn = []
    for i in range(1, size + 1, 2):
        if i == 1:
            rtn.append([i])
        else:
            rtn.append([i**2, i**2 - (i - 1), i**2 - 2* (i - 1), i**2 - 3 * (i - 1)])
    return rtn

if __name__ == '__main__':
    ans = 0
    for each in diaSeq(1001):
        ans += sum(each)
    print(ans)