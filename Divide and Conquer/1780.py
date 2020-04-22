# https://www.acmicpc.net/problem/1780
# 종이의 개수

import sys

minus = 0
zero = 0
one = 0

def check(mat, n, i, j):
    global minus, zero, one
    first = mat[i][j]
    flag = True
    for r in range(i, i + n):
        for c in range(j, j + n):
            if first != mat[r][c]:
                flag = False
                break

    if flag == False:
        divide(mat, n, i, j)
    else:
        if first == -1:
            minus += 1
        elif first == 1:
            one += 1
        else:
            zero += 1
        

def divide(mat, n, i, j):
    if n >= 3:
        s = n // 3
        dx = [0, s, 2*s]
        dy = [0, s, 2*s]
        for p in range(3):
            for q in range(3):
                check(mat, s, i + dx[p], j + dy[q])


N = int(sys.stdin.readline())
mat = []
for _ in range(N):  
    mat.append(list(map(int, sys.stdin.readline().split())))

check(mat, N, 0, 0)
print(minus)
print(zero)
print(one)