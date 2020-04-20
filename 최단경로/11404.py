# https://www.acmicpc.net/problem/11404
# 플로이드

'''
다익스트라 : 가장 적은 비용을 하나씩 선택하는 것.
플로이드 와샬 알고리즘 : """거쳐가는 정점""" 기준으로 알고리즘을 수행. DP 관점
DP[2, 3] = min(DP[2, 3], DP[2, 1] + DP[1, 3])
다익스트라 - 음의 가중치 사용하지 못하지만 플로이드 와샬은 가능.
벨만 포드도 음의 가중치 사용 가능
'''
import sys
from heapq import heappop, heappush

INF = sys.maxsize

class Graph:
    def __init__(self, n, m, links):
        self.n = n
        self.m = m
        self.links = links
        self.dist = [[INF] * n for _ in range(n)]
        
        for i in range(n):
            self.dist[i][i] = 0
            for p, c in links[i]:
                self.dist[i][p] = min(c, self.dist[i][p])
            
    def floydWarshall(self):
        N = self.n
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]

        for i in range(N):
            for j in range(N):
                if self.dist[i][j] >= INF:
                    self.dist[i][j] = 0

        self.printDistance()

    def printDistance(self):
        for i in range(self.n):
            print(' '.join(map(str, self.dist[i])))


        
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

links = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    links[a - 1].append([b - 1, c])

graph = Graph(n, m, links)
graph.floydWarshall()