N = int(input())
lst = []
count_dict = dict()
for _ in range(N):
	num = int(input())
	lst.append(num)
	if num not in count_dict:
		count_dict[num] = 1
	else:
		count_dict[num] += 1

if N == 1:
	average = lst[0]
	mid = lst[0]
	freq = lst[0]
	diff = 0
else:
	lst = sorted(lst)
	
	average = sum(lst) / N
	mid = lst[N // 2]
	
	count_dict = sorted(count_dict.items(), key = lambda x : x[1], reverse = True)
	if count_dict[0][1] == count_dict[1][1]:
		freq = count_dict[1][0]
	else:
		freq = count_dict[0][0]
	
	diff = lst[-1] - lst[0]

print("%.0f" % average)
print(mid)
print(freq)
print(diff)
