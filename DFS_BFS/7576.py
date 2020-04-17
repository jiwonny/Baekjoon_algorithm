# https://www.acmicpc.net/problem/7576
# 토마토

import sys
from collections import deque

def bfs(mat, ones, M, N):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    count = -1
    while ones:
        count += 1
        for _ in range(len(ones)):
            x, y = ones.popleft()
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < M and mat[nx][ny] == 0:
                    ones.append((nx, ny))
                    mat[nx][ny] = 1

    for b in mat:
        if 0 in b:
            return -1

    return count

M, N = map(int, sys.stdin.readline().split())
# 가로, 세로

mat = []
ones = deque()

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    mat.append(line)

    for j in range(M):
        if line[j] == 1:
            ones.append((i, j))
      

print(bfs(mat, ones, M, N))

