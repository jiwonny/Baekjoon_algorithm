# 수 정렬 - insertion sort

import sys

def insertion(lst):
    for i in range(1, len(lst)):
        key = lst[i]

        j =  i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key    

    return lst
        
def selection(lst):
    for i in range(len(lst), 0, -1):
        max_idx = 0
        for j in range(i):
            if lst[j] > lst[max_idx]:
                max_idx = j

        lst[j], lst[max_idx] = lst[max_idx], lst[j]

    return lst


def merge(lst, p, q, r):
    max_val = sys.maxsize
    A = []
    B = []
    A += lst[p : q + 1]
    B += lst[q + 1 : r + 1]
    A.append(max_val)
    B.append(max_val)

    i = 0
    j = 0

    for k in range(p, r + 1):
        if A[i] <= B[j]:
            lst[k] = A[i]
            i = i + 1
        else:
            lst[k] = B[j]
            j = j + 1



def mergeSort(lst, p, r):
    if p < r:
        q = int((p + r) / 2)
        mergeSort(lst, p, q)
        mergeSort(lst, q + 1, r)
        merge(lst, p, q, r)
    
    return lst

lst = list(map(int, sys.stdin.readline().split()))
# answer = insertion(lst)
# answer = selection(lst)
answer = mergeSort(lst, 0, len(lst) - 1)
print(answer)

