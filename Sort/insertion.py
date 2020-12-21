def insertion(list_to_sort):
	for i in range(1, len(list_to_sort)):
		key = list_to_sort[i]

		compare_idx = i - 1
		while compare_idx >= 0 and list_to_sort[compare_idx] > key:
			list_to_sort[compare_idx + 1] = list_to_sort[compare_idx]
			compare_idx -= 1
		
		list_to_sort[compare_idx + 1] = key

	return list_to_sort


N = int(input())
list_to_sort = []
for _ in range(N):
	list_to_sort.append(int(input()))

result = insertion(list_to_sort)
print(result)