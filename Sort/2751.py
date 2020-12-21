import sys
MAX_VALUE = sys.maxsize

def merge(list_to_sort, p, q, r):
	list_A = list_to_sort[p:q + 1]
	list_B = list_to_sort[q + 1:r + 1]

	list_A.append(MAX_VALUE)
	list_B.append(MAX_VALUE)

	index_A = 0
	index_B = 0

	for i in range(p, r + 1):
		if list_A[index_A] <= list_B[index_B]:
			list_to_sort[i] = list_A[index_A]
			index_A += 1
		else:
			list_to_sort[i] = list_B[index_B]
			index_B += 1

def merge_sort(list_to_sort, p, r):
	if p < r:
		q = (p + r) // 2
		merge_sort(list_to_sort, p, q)
		merge_sort(list_to_sort, q + 1, r)
		merge(list_to_sort, p, q, r) 
	return list_to_sort

N = int(input())
list_to_sort = []

for _ in range(N):
	list_to_sort.append(int(input()))

result = merge_sort(list_to_sort, 0, len(list_to_sort) - 1)
print(result)
