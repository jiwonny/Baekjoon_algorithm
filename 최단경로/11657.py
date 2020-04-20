# https://www.acmicpc.net/problem/11657
# 타임머신

# Using Bellman Ford Algorithm becasue of the negative weights
import sys

INF = sys.maxsize

def bellman(links, n, m):
    dist = [INF] * n
    dist[0] = 0 # starting point
    
    # if there's an update 'till the end of the nested for loop -> INF LOOP
    isLoop = False
    for i in range(n):
        for j in range(m):
            a, b, w = links[j]
            
            update_cost = dist[a - 1] + w
            if dist[a - 1] != INF and update_cost < dist[b - 1]:
                dist[b - 1] = update_cost
                if i == n - 1:
                    isLoop = True

    if isLoop:
        print(-1)
    else:
        for i in range(1, n):
            if dist[i] == INF:
                print(-1)
            else:
                print(dist[i])



N, M = map(int, sys.stdin.readline().split())

links = []
for _ in range(M):
    links.append(list(map(int, sys.stdin.readline().split())))

bellman(links, N, M)
    