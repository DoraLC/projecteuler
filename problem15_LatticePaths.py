'''
Starting in the top left corner of a 2x2 grid, and only being able to move the right and down, 
there are exactly 6 routes to the bottom right corner. 

https://projecteuler.net/resources/images/0015.png?1678992052

How many such routes are there through a 20x20 grid?

answer: 137846528820
'''

'''class LatticPaths():
    def __init__(self, gridSize):
        self._gridSize = gridSize
        self._location = [0, 0]
        self._paths = [self.getLocation()]
        self._AllPaths = []

    def moveRight(self):
        self._location[0] += 1
        self._paths.append(self._location.copy())

    def moveDown(self):
        self._location[1] += 1
        self._paths.append(self._location.copy())
    
    def getLocation(self):
        return self._location.copy()
    
    def getPath(self):
        return self._paths
    
    def storePath(self, path):
        self._AllPaths.append(path.copy())

    def resetLocation(self):
        self._location = [0, 0]
    
    def getAllPaths(self):
        return self._AllPaths.copy()'''

import math

def nCr(n, r):
    return int(math.factorial(n)/(math.factorial(r) * (math.factorial(n - r))))

def solution(num):
    return nCr(num * 2, num)

print(solution(20))