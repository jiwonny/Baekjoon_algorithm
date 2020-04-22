# https://www.acmicpc.net/problem/10816
# 숫자 카드2

import sys
from collections import Counter

def binarySearch(lst, key, low, high):
    if low >= high:
        return -1

    mid = (low + high) // 2
    if lst[mid] == key:
        return 1
    elif lst[mid] > key:
        return binarySearch(lst, key, low, mid)
    else:
        return binarySearch(lst, key, mid + 1, high)

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

a = Counter(A)
lst_cmp = list(sorted(list(a)))

answer = []
for i in range(M):
    t = binarySearch(lst_cmp, B[i], 0, 0)
    if t == 0:
        answer.append(0)
    else:
        answer.append(a[B[i]])


print(' '.join(map(str, answer)))