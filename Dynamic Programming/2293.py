# https://www.acmicpc.net/problem/2293
# 동전1

import sys

n, k  = map(int, sys.stdin.readline().split())
lst = []
dp = [0] * (k + 1)
dp[0] = 1

for _ in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()

for i in range(n):
    for j in range(1, k + 1):
        if lst[i] <= j:
            dp[j] += dp[j - lst[i]]

print(dp[-1])