'''
2520 is the smallest number that can be divided by each of then numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

answer: 232792560
'''
#find the smallest number that can be divided by each of then numbers from 1 to @number
def smallestMultiple(number):
    q = 11
    while True:
        done = True
        for i in range(number, 3, -1):
            if q % i > 0:
                done = False
                break
        if done:
            return q
        q += 1

if __name__ == '__main__':
    print(smallestMultiple(20))