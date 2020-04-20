# https://www.acmicpc.net/problem/9251
# LCS

import sys
A = [0]
B = [0]

A.extend(list(sys.stdin.readline().strip()))
B.extend(list(sys.stdin.readline().strip()))
# print(A)
len_A, len_B = len(A) - 1, len(B) - 1
dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]

for i in range(1, len_A + 1):
    for j in range(1, len_B + 1):
        if B[j] == A[i]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max(dp[len_A]))