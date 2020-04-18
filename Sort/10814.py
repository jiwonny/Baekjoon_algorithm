# https://www.acmicpc.net/problem/10814
# 나이순 정렬

import sys

N = int(sys.stdin.readline())

lst = []

for _ in range(N):
    line = sys.stdin.readline().split()
    lst.append([int(line[0]), line[1]])

lst.sort(key = lambda x: x[0])
    
for line in lst:
    print(' '.join(map(str, line)))
