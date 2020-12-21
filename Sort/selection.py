def selection(list_to_sort):
	for i in range(len(list_to_sort)):
		min_idx = i
		for compare_idx in range(i + 1, len(list_to_sort)):
			if list_to_sort[compare_idx] < list_to_sort[min_idx]:
				min_idx = compare_idx
		
		list_to_sort[min_idx], list_to_sort[i] = list_to_sort[i], list_to_sort[min_idx]
	return list_to_sort

N = int(input())
list_to_sort = []
for _ in range(N):
	list_to_sort.append(int(input()))

result = selection(list_to_sort)
print(result)