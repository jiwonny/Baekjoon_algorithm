# https://www.acmicpc.net/problem/11047
# 동전 0 
import sys

N, K = map(int, sys.stdin.readline().split())

values = []

for _ in range(N):
    values.append(int(sys.stdin.readline()))

count = 0
for i in range(N - 1, -1, -1):
    if K == 0:
        break
    if values[i] > K:
        continue
    else:
        count += K // values[i]
        K = K % values[i]

print(count)        