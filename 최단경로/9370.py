# https://www.acmicpc.net/problem/9370
# 미확인 도착지

import sys
from heapq import heappop, heappush

INF = sys.maxsize

def dijkstra(start, n, roads):
    q = []
    dist = [INF] * n
    dist[start] = 0
    heappush(q, [start, 0])

    while q:
        pos, cost = heappop(q)

        for p, c in roads[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(q, [p, c])

    return dist

def getAnswer(start, n, roads, g, h, check):
    '''
    case1 : s -> g -> h -> n
    case2 : s -> h -> g -> n
    '''
    cost1 = dijkstra(start, n, roads)
    cost2 = dijkstra(g, n, roads)
    cost3 = dijkstra(h, n, roads)

    check.sort()
    for val in check:
        result1 = cost1[g] + cost2[h] + cost3[val - 1]
        result2 = cost1[h] + cost3[g] + cost2[val - 1]
        if cost1[val - 1] == min(result1, result2):
            print(val, end = ' ')

def main():
    tcase = int(sys.stdin.readline())

    for _ in range(tcase):
        n, m, t = map(int, sys.stdin.readline().split()) # 교차로, 도로, 목적지
        s, g, h = map(int, sys.stdin.readline().split())

        roads = [[] for _ in range(n)]

        for _ in range(m):
            a, b, d = map(int, sys.stdin.readline().split())
            roads[a - 1].append([b - 1, d])
            roads[b - 1].append([a - 1, d])

        check = []
        for _ in range(t):
            check.append(int(sys.stdin.readline()))
                
        getAnswer(s - 1, n, roads, g - 1, h - 1, check)
        
        print()

main()