'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

answer: 233168
'''

def check_multi_3and5(number):
    if number % 3 == 0 or number % 5 == 0:
        return True
    
def answer1():
    numbers = []

    for i in range(1000):
        if check_multi_3and5(i):
            numbers.append(i)

    print(sum(numbers))

#######################################################

def sum_of_as(FirstTerm, diff, number_of_terms):
    return (FirstTerm + diff * number_of_terms) * number_of_terms // 2

def answer2():
    return sum_of_as(3, 3, 333) + sum_of_as(5, 5, 199) - sum_of_as(15, 15, 66)

if __name__ == '__main__':
    answer1()
    print(answer2())