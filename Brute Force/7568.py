# https://www.acmicpc.net/problem/7568
# 덩치

import sys

num = int(sys.stdin.readline())

inf = []
rank = [1] * num
for _ in range(num):
    inf.append(list(map(int, sys.stdin.readline().split())))
    
for i in range(num):
    for j in range(num):
        if i == j:
            continue

        if inf[j][0] > inf[i][0] and inf[j][1] > inf[i][1]:
            rank[i] += 1

print(' '.join(map(str, rank)))

