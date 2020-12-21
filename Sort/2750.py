def bubble_sort(N, list):
	for i in range(N - 1):
		for j in range(0, N - i - 1):
			if list[j] > list[j + 1]:
				list[j], list[j + 1] = list[j + 1], list[j]
	
	return list

N = int(input())

list_to_sort = []
for _ in range(N):
	list_to_sort.append(int(input()))

result = bubble_sort(N, list_to_sort)
print('\n'.join(map(str, result)))
