# https://www.acmicpc.net/problem/10830
# 행렬 제곱

import sys

mat = []
dp = {}
c = 1000

def mul(n, a, b):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for p in range(n):
                res[i][p] = (res[i][p] + (a[i][j] % c) * (b[j][p] % c)) % c

    return res

def func(n, b):
    if b in dp.keys():
        return dp[b]

    k = b // 2

    temp = mul(n, func(n, k), func(n, b - k))
    # exit(0)
    dp[b] = temp
    
    return temp

n, b = map(int, sys.stdin.readline().split())

for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        mat[i][j] = mat[i][j] % c 

dp[0] = 1
dp[1] = mat

ans = func(n, b)

for row in ans:
    print(' '.join(map(str, row)))

