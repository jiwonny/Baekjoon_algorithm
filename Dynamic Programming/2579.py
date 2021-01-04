n = int(input())
scores = []
for _ in range(n):
	scores.append(int(input()))

dp = []
for i in range(n):
	if i == 0:
		dp.append(scores[0])
	elif i == 1:
		dp.append(scores[0] + scores[1])
	elif i == 2:
		result = scores[2] + max(dp[0], scores[1])
		dp.append(result)
	else:
		result = scores[i] + max(scores[i - 1] + dp[i - 3], dp[i - 2])
		dp.append(result)

print(dp[-1])