# https://www.acmicpc.net/problem/1920
# 수 찾기.

# binary search

import sys

def binarySearch(A, key, low, high):
    if low >= high:
        return 0
    
    mid = (low + high) // 2
    if A[mid] == key:
        return 1
    elif A[mid] > key:
        return binarySearch(A, key, low, mid)
    else:
        return binarySearch(A, key, mid + 1, high)



N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

answer = []
for i in range(M):
    t = binarySearch(A, B[i], 0, N)
    answer.append(t)

print('\n'.join(map(str, answer)))
