# https://www.acmicpc.net/problem/7579
# 토마토 3차원

import sys
from collections import deque

def bfs(mat, ones, M, N, H):
    dx = [0, 0, 0, 0, 1, -1]
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 1, -1, 0, 0]
    
    count = -1
    while ones:
        count += 1
        for _ in range(len(ones)):
            x, y, z = ones.popleft()
        
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]

                if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and mat[nz][nx][ny] == 0:
                    ones.append((nx, ny, nz))
                    mat[nz][nx][ny] = 1

    for plane in mat:
        for line in plane: 
            if 0 in line:
                return -1

    return count

M, N, H = map(int, sys.stdin.readline().split())
# 가로, 세로

mat = []
ones = deque()
for i in range(H):
    plane = []
    for j in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        plane.append(line)

        for k in range(M):
            if line[k] == 1:
                ones.append((j, k, i))
    mat.append(plane)
      

print(bfs(mat, ones, M, N, H))

