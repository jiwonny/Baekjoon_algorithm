# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기

import sys

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    line = list(sys.stdin.readline().strip())
    board.append(line)

colors = ['W', 'B']

min_val = 999999

for i in range(N - 7):
    for j in range(M - 7):
        colors = ['B', 'W']
        for color in range(len(colors)):
            count = 0
            for p in range(i, i + 8):
                for q in range(j, j + 8):
                    if board[p][q] != colors[color % 2]:
                        count += 1
                    
                    color += 1
                color += 1
            
            min_val = min(count, min_val)
    
print(min_val)