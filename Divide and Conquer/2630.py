# https://www.acmicpc.net/problem/2630
# 색종이 만들기

import sys

blue = 0
white = 0

def check(mat, n, i, j):
    global blue
    global white

    a = mat[i][j]
    flag = True
    for r in range(i, i + n):
        for c in range(j, j + n):
            if a != mat[r][c]:
                flag = False
                break

    if flag == False:
        # print('더 나눠야 함', i, j)
        divide(mat, n, i, j)
    else:
        if a == 1:
            blue += 1
        else:
            white += 1

def divide(mat, n, i, j):
    if n >= 2:
        size = n // 2
        # print(n, size)
        check(mat, size, i, j)
        check(mat, size, i, j + size)
        check(mat, size, i + size, j)
        check(mat, size, i + size, j + size)

n = int(sys.stdin.readline())
mat = []
for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))

# 잘라서 하얀색 파란색 색종이의 개수.
check(mat, n, 0, 0)
print(white)
print(blue)
