'''
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its aplhabetical position in the list to obtain a name socre. 

For example, when the list is sorted into aplhabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714. 

What is the total of all the name scores in the file?
answer: 871198282
'''
import string

names = open('0022_names.txt', 'r')
alphabit = list(string.ascii_uppercase)
letter_score = {}
for i in range(0, len(alphabit)):
    letter_score[alphabit[i]] = i + 1
letter_score['"'] = 0

def worth(name):
    rtn = 0
    for letter in name:
        rtn += letter_score[letter]
    return rtn

names_list = names.read().split(',')
names.close()
names_list.sort()

def solution(names):
    rtn = 0
    for i in range(len(names)):
        rtn += worth(names[i]) * (i + 1)
    return rtn

print(solution(names_list))