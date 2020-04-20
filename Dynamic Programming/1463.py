import sys

N = int(sys.stdin.readline())

dp = [0] * (N + 1)

for i in range(2, N + 1):
    minimum = 9999999
    if i % 3 == 0:
        idx = i // 3
        minimum = min(minimum, dp[idx])
    
    if i % 2 == 0:
        idx = i // 2
        minimum = min(minimum, dp[idx])
    
    minimum = min(minimum, dp[i - 1])
    dp[i] = minimum + 1

print(dp[N])

    