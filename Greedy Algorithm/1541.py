# https://www.acmicpc.net/problem/1541
# 잃어버린 괄호

import sys

A = sys.stdin.readline().strip().split('-')

num = []
for item in A:
    count = 0
    elements = item.split('+')
    for e in elements:
        count += int(e)
    
    num.append(count)

total = num[0]
for i in range(1, len(num)):
    total -= num[i]

print(total)