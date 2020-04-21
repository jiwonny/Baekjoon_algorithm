# https://www.acmicpc.net/problem/11399
# ATM

import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()
dp = [0] * N
for i in range(N):
    dp[i] = sum(lst[:i + 1])

print(sum(dp))