# https://www.acmicpc.net/problem/2667
# 단지번호 붙이기

import sys
from collections import deque

class Houses:
    def __init__(self, n, mat, ones):
        self.n = n 
        self.mat = mat
        self.ones = ones

    def dfs(self, node, trace):
        trace += [node]
        r, c = node

        if (r + 1, c) in self.ones and (r + 1, c) not in trace:
            trace = self.dfs((r + 1, c), trace)
        
        if (r, c + 1) in self.ones and (r, c + 1) not in trace:
            # self.mat[r][c + 1] = - 1
            trace = self.dfs((r, c + 1), trace)

        if (r - 1, c) in self.ones and (r - 1, c) not in trace:
            # self.mat[r - 1][c] = - 1
            trace = self.dfs((r - 1, c), trace)

        if (r, c - 1) in self.ones and (r, c - 1) not in trace:
            # self.mat[r][c - 1] = - 1
            trace = self.dfs((r, c - 1), trace)
        
        return trace

    def getGroup(self):
        groups = []
        
        while self.ones:
            trace = self.dfs(self.ones[0], [])
            groups.append(len(trace))

            for item in trace:
                ones.remove(item)

        return groups

    def __str__(self):
        groups = self.getGroup()
        groups.sort()
        groups.insert(0, len(groups))
        return '\n'.join(map(str, groups))

n = int(sys.stdin.readline())

mat = []
ones = []
for i in range(n):
    tmp = list(sys.stdin.readline().strip())
    line = list(map(int, tmp))
    mat.append(line)

    for j in range(len(line)):
        if line[j] == 1:
            ones.append((i, j))


house = Houses(n, mat, ones)
print(house)





