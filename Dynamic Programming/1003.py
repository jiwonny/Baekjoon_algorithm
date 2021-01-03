dp = {
	0: (1, 0),
	1: (0, 1)
}

T = int(input())
numbers = []
for _ in range(T):
	numbers.append(int(input()))

maximum = max(numbers)
for i in range(2, maximum + 1):
	dp[i] = (dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1])

for num in numbers:
	print(' '.join(map(str, dp[num])))