import sys

N = int(input())

dp = []

for i in range(N + 1):
    if i == 0 or i == 1:
        dp.append(0)
    else:
        result = sys.maxsize
        if i % 3 == 0:
            result = min(result, dp[i // 3])
        
        if i % 2 == 0:
            result = min(result, dp[i // 2])

        result = min(result, dp[i - 1])
        dp.append(result + 1)

print(dp[-1])