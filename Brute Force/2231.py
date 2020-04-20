# https://www.acmicpc.net/problem/2231
# 분해합

import sys

N = int(sys.stdin.readline())

answer = 0
for i in range(1, N):
    total = i
    for digit in str(i):
        total += int(digit)
    
    if total == N:
        answer = i
        break

print(answer)