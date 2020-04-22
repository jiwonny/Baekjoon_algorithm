# https://www.acmicpc.net/problem/1654
# 랜선 자르기

import sys

K, N = map(int, sys.stdin.readline().split())

lst = []
for _ in range(K):
    lst.append(int(sys.stdin.readline()))

lst.sort()
low = 1
high = lst[-1]

while low <= high:
    mid = (low + high) // 2
    
    count = 0
    for i in range(len(lst)):
        count += lst[i] // mid
    
    if count < N: # 더 작은 수로 나눠야함.
        high = mid - 1
    elif count >= N:
        low = mid + 1

print(high)