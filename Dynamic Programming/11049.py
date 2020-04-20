# https://www.acmicpc.net/problem/11049
# 행렬 곱셈 순서

import sys

n = int(sys.stdin.readline())
mat = []

for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * (n) for _ in range(n)]

for i in range(1, n):
    for j in range(0, n - i):
        row = j
        col = i + j

        if i == 1:
            dp[row][col] = mat[row][0] * mat[row][1] * mat[col][1]
        else:
            dp[row][col] = 2 ** 31
            for k in range(row, col):
                dp[row][col] = min(dp[row][col], dp[row][k] + dp[k + 1][col] + mat[row][0] * mat[k][1] * mat[col][1])

print(dp[0][-1])