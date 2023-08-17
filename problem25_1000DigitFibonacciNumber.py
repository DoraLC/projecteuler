'''
The Fibonacci sequence is defined by the recurrence relation:

F(n) = F(n - 1) + F(n - 2) were F(1) = F(2) = 1

Hence the first 12 terms will be:

F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
F(10) = 55
F(11) = 89
F(12) = 144

The 12th term, F(12) is the first term to contain three digits. 
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

def fibonacci(n, dict={1:1, 2:1}):
    if n in dict:
        return dict[n]
    dict[n] = fibonacci(n - 1, dict) + fibonacci(n - 2, dict)
    return dict[n]

def solution(deg=1000):
    n = 1
    while True:
        tmp = fibonacci(n)
        if tmp > 10 ** (deg - 1):
            return n
        n += 1

if __name__ == '__main__':
    print(solution())
