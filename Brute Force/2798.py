# https://www.acmicpc.net/problem/2798
# 블랙잭

import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

maximum = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            val = cards[i] + cards[j] + cards[k]
            if val <= M:
                maximum = max(maximum, val)

print(maximum)