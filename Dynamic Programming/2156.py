# https://www.acmicpc.net/problem/2156
# 포도주 시식

import sys

n = int(sys.stdin.readline())
wine = []
dp = [0] * (n)
for _ in range(n):
    wine.append(int(sys.stdin.readline()))

dp[0] = wine[0]

for i in range(1, n):
    if i == 1:
        dp[i] = wine[1] + dp[0]
    elif i == 2:
        dp[i] = max(wine[2] + wine[0], wine[1] + wine[2], wine[0] + wine[1])
    else:
        dp[i] = max(wine[i] + wine[i - 1] + dp[i - 3], wine[i] + dp[i - 2], dp[i - 1])
    
print(dp[n - 1])