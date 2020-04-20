import sys

DIV = 1000000000
N = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(10):
        if i == 1 and j != 0:
            dp[i][j] += 1
        elif i != 1:
            if j == 0:
                dp[i][j] += dp[i - 1][j + 1]
            elif j == 9:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j + 1]
        
print(sum(dp[N]) % DIV)
