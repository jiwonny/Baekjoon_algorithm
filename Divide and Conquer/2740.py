# https://www.acmicpc.net/problem/2740
# 행렬 곱셈

import sys

def mul(X, Y, N, M, K):
    mat = [[0] * K for _ in range(N)]
    for i in range(N):
        for j in range(K):
            for p in range(M):
                mat[i][j] += X[i][p] * Y[p][j]

    return mat


N, M = map(int, sys.stdin.readline().split())
A = []
B = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

M, K = map(int, sys.stdin.readline().split())
for _ in range(M):
    B.append(list(map(int, sys.stdin.readline().split())))

answer = mul(A, B, N, M, K)

for row in answer:
    print(' '.join(map(str, row)))