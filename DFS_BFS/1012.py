# https://www.acmicpc.net/problem/1012
# 유기농 배추
# recursive depth 때문에 runtime error 남.

import sys
from collections import deque

class Field:
    def __init__(self, m, n, ones):
        self.m = m
        self.n = n 
        self.ones = ones

    def dfs(self, node, trace):
        trace += [node]
        r, c = node

        if (r + 1, c) in self.ones and (r + 1, c) not in trace:
            trace = self.dfs((r + 1, c), trace)
        
        if (r, c + 1) in self.ones and (r, c + 1) not in trace:
            trace = self.dfs((r, c + 1), trace)

        if (r - 1, c) in self.ones and (r - 1, c) not in trace:
            trace = self.dfs((r - 1, c), trace)

        if (r, c - 1) in self.ones and (r, c - 1) not in trace:
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
        return str(len(groups))


tcase = int(sys.stdin.readline())
for _ in range(tcase):
    m, n, k = map(int, sys.stdin.readline().split())
    ones = []
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        ones.append((a, b))

    field = Field(m, n, ones)
    print(field)

