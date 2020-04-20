# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열

import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
rank = [0] * N
rank_rev = [0] * N

rank[0] = 1
rank_rev[0] = 1

for i in range(1, N):
    for j in range(i):
        # lst[i] 와 lst[j] 비교 
        if lst[i] > lst[j] and rank[i] < rank[j]:
            rank[i] = rank[j]
    
    rank[i] += 1


print(max(rank))