# https://www.acmicpc.net/problem/2606
# 바이러스
import sys
from collections import deque


def dfs(node, links, trace):
    trace += [node]

    for search_node in links[node]:
        if search_node not in trace:
            trace = dfs(search_node, links, trace)

    return trace

def bfs(start, links):
    queue = deque()
    queue.append(start)
    trace = []
    trace.append(start)

    while queue:
        node = queue.popleft()
        
        for search_node in links[node]:
            if search_node not in trace:
                trace.append(search_node)
                queue.append(search_node)
    
    return trace


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
links = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    links[a - 1].append(b - 1)
    links[b - 1].append(a - 1) # 양방향인 경우 빼먹지 말고 꼭 넣기


# answer = len(dfs(0, links, [])) - 1
answer = len(bfs(0, links)) - 1
print(answer)