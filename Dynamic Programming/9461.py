T = int(input())

numbers = []
for _ in range(T):
	numbers.append(int(input()))

answers = [0, 1, 1, 1, 2, 2, 3]

maximum = max(numbers)
for num in range(7, maximum + 1):
	answers.append(answers[num - 1] + answers[num - 5])

for num in numbers:
	print(answers[num])
