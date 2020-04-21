# https://www.acmicpc.net/problem/1931
# 회의실 배정

import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

B = list(sorted(lst, key = lambda x: [x[1], x[0]]))

start = 0
count = 0
for item in B:
    if item[0] >= start:
        start = item[1]
        count += 1
        
print(count)
