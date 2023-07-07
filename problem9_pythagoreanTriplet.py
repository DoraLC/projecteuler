'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, 
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythargorean triple for which a + b + c = 1000.
Find the product a*b*c. 

answer: 31875000
'''

#check if @[a, b, c] is a Pythargorean triple
def check_triplet(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    return False

#find Pythargorean triple less than @n
def find_triplet_set(n):
    rtn = []
    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if check_triplet(i, j, k):
                    rtn.append([i, j, k])
    return rtn

def answer(numsum):
    for each in find_triplet_set(numsum // 2):
        if sum(each) == numsum:
            return [each, each[0] * each[1] * each[2]]
        
print(answer(1000))