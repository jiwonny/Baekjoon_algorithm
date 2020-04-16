# https://www.acmicpc.net/problem/1956
# 운동
import sys
from heapq import heappop, heappush

INF = float('INF')

def floyd(V, links):
    dist = [[INF] * V for _ in range(V)]
    for a, b, w in links:
        dist[a][b] = w
    for i in range(V):
        dist[i][i] = 0
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


V, E = map(int, sys.stdin.readline().split())
links = []

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    links.append([a - 1, b - 1, c])

mat = floyd(V, links)
min_val = INF

for i in range(V):
    for j in range(V):
        if i == j:
            continue
        min_val = min(min_val, mat[i][j] + mat[j][i])

if min_val == INF:
    print(-1)
else:
    print(min_val)