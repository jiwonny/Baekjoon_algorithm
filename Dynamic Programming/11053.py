N = int(input())
numbers = list(map(int, input().split()))

ranks = []
for i in range(N):
	if i == 0:
		ranks.append(1)
		continue
	
	ranks.append(0)
	for j in range(i):
		if numbers[j] < numbers[i] and ranks[j] > ranks[i]:
			ranks[i] = ranks[j]

	ranks[i] += 1

print(max(ranks))