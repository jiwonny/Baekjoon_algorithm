# https://www.acmicpc.net/problem/1504
# 특정한 최단경로

import sys
from heapq import heappop, heappush

INF = sys.maxsize

N, E = map(int, sys.stdin.readline().split())
links = [[] for _ in range(N)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    links[a - 1].append([b - 1, c])
    links[b - 1].append([a - 1, c])

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start, N, links):
    dist = [INF] * N
    dist[start] = 0
    q = []
    heappush(q, [start, 0])

    while q:
        pos, cost = heappop(q)

        for p, c in links[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(q, [p, c])

    return dist

dis1 = dijkstra(0, N, links)
dis2 = dijkstra(v1 - 1, N, links)
dis3 = dijkstra(v2 - 1, N, links)

result1 = dis1[v1 - 1] + dis2[v2 - 1] + dis3[N - 1]
result2 = dis1[v2 - 1] + dis2[v2 - 1] + dis2[N - 1]

if result2 >= INF and result1 >= INF:
    print(-1)
else:
    print(min(result1,result2))
