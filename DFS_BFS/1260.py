# https://www.acmicpc.net/problem/1260
# DFS & BFS
import sys
from collections import deque

class Search:
    def __init__(self, links, N, M, V):
        self.links = links
        self.N = N
        self.M = M
        self.V = V

    def dfs(self, node, trace):
        trace += [node]

        for search_node in self.links[node]:
            if search_node not in trace:
                trace = self.dfs(search_node, trace)
        
        return trace

    def bfs(self):
        trace = []
        queue = deque()
        queue.append(self.V)
        trace.append(self.V)

        while queue:
            node = queue.popleft()
            
            for search_node in self.links[node]:
                if search_node not in trace:
                    queue.append(search_node)
                    trace.append(search_node)

        return trace


N, M, V = map(int, sys.stdin.readline().split())
links = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    links[a].append(b)
    links[b].append(a)


for link in links:
    link.sort()

search = Search(links, N, M, V)

dfs_res = search.dfs(V, [])
bfs_res = search.bfs()
print(' '.join(map(str, dfs_res)))
print(' '.join(map(str, bfs_res)))
