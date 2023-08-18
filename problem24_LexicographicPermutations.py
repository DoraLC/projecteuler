'''
A permutation is an ordered arrangement of objects. For example, 3134 is one possible permutation oft he digits 1, 2, 3 and 4.
If all of the permutations are listed numberically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012 021 102 120 201 210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

answer: 2783915460
'''
digits = '0123456789'
test_dig = '012'

def permutation(str):
    if len(str) == 1:
        return [str]
    
    rtn = []
    tmp = str[0]
    target = permutation(str[1:])

    for each in target:
        for i in range(len(each) + 1):
            rtn.append(each[i:] + tmp + each[:i])

    return rtn

def solution(dig=digits, pos=1000000):
    tmp = permutation(dig)
    tmp.sort()
    print(tmp[pos - 1])

if __name__ == '__main__':
    solution()