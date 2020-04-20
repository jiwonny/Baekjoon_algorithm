# https://www.acmicpc.net/problem/2565
# 전깃줄

import sys

N = int(sys.stdin.readline())
lst = []
rank = [0] * N
rank[0] = 1

for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort(key = lambda x : x[0])

for i in range(1, N):
    for j in range(i):
        if lst[i][1] >= lst[j][1] and rank[i] <= rank[j]:
            rank[i] = rank[j]
        
    rank[i] += 1

print(N - max(rank))