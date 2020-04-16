import sys
from heapq import heappop, heappush

INF = sys.maxsize

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

weight = [[] for _ in range(V)]

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    weight[u - 1].append([v - 1, w])


def dijkstra(v, e, k, weight):
    dist = [INF] * v
    dist[k - 1] = 0

    q = []
    heappush(q, [0, k - 1])

    while q:
        cost, pos = heappop(q)

        for p, c in weight[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(q, [c, p])

    return dist


answers = dijkstra(V, E, K, weight)

for answer in answers:
    if answer == INF:
        print('INF')
    else:
        print(answer)