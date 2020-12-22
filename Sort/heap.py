def heapify(unsorted, index, heap_size):
	largest = index
	left_child = index * 2 + 1
	right_child = index * 2 + 2

	if left_child < heap_size and unsorted[left_child] > unsorted[largest]:
		largest = left_child

	if right_child < heap_size and unsorted[right_child] > unsorted[largest]:
		largest = right_child
	
	if largest != index:
		unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
		heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
	n = len(unsorted)
	for i in range(n // 2 - 1, -1, -1):
		heapify(unsorted, i, n)

	for i in range(n - 1, 0, -1):
		unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
		heapify(unsorted, 0, i)
	
	print(unsorted)

N = int(input())
lst = []
for _ in range(N):
	lst.append(int(input()))

heap_sort(lst)


