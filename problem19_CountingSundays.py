'''
You are given the following information, but you may prefer to do some research for youself. 
- 1 Jan 1900 was a Monday. 
- Thirty days has September, 
    April, June and November. 
    All the rest have thirty-one, 
    Saving February alone, 
    Which has twenty-eight, rain or shine. 
    And on leap years, twenty-nine. 
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400. 

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

answer: 171
'''

def isLeapYr(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            if year % 100 == 0 and year % 400 == 0:
                return True
    return False

def months(leapYr):
    if leapYr:
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

times = 0
week = 1
for year in range(1901, 2001):
    for month in months(isLeapYr(year)):
        if (month - week) % 7 == 0:
            times += 1
        week += month % 7
    
print(times)