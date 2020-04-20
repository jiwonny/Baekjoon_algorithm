# https://www.acmicpc.net/problem/2178
# 미로 찾기

'''
BFS 의 특징은 각 정점을 최단경로로 방문한다는 것.
'''
import sys
from collections import deque

def bfs(N, M, ones):
    dist = [[0] * M for _ in range(N)]
    queue = deque()
    check = []

    queue.append(ones[0])

    while queue:
        node = queue.popleft()
        r, c = node
        
        if r == N - 1 and c == M - 1:
            return dist[N - 1][M - 1]
        
        if (r + 1, c) in ones and (r + 1, c) not in check:
            queue.append((r + 1, c))
            check.append((r + 1, c))
            dist[r + 1][c] = dist[r][c] + 1

        if (r - 1, c) in ones and (r - 1, c) not in check:
            queue.append((r - 1, c))
            check.append((r - 1, c))
            dist[r - 1][c] = dist[r][c] + 1

        if (r, c + 1) in ones and (r, c + 1) not in check:
            queue.append((r, c + 1))
            check.append((r, c + 1))
            dist[r][c + 1] = dist[r][c] + 1

        if (r, c - 1) in ones and (r, c - 1) not in check:
            queue.append((r, c - 1))
            check.append((r, c - 1))
            dist[r][c - 1] = dist[r][c] + 1

    return dist[N - 1][M - 1]


N, M = map(int, sys.stdin.readline().split())

mat = []
ones = []
for i in range(N):
    tmp = list(sys.stdin.readline().strip())
    line = list(map(int, tmp))
    mat.append(line)
    for j in range(len(line)):
        if line[j] == 1:
            ones.append((i, j))


print(bfs(N, M, ones) + 1)