n = int(input())

quantities = []
for _ in range(n):
    quantities.append(int(input()))

dp = []
for i in range(n):
    if i == 0:
        dp.append(quantities[i])
    elif i == 1:
        dp.append(quantities[i] + quantities[i - 1])
    elif i == 2:
        result = max(quantities[i] + quantities[i - 1], quantities[i] + quantities[i - 2], quantities[i - 1] + quantities[i - 2])
        dp.append(result)
    else:
        result = max(quantities[i] + quantities[i - 1] + dp[i - 3], quantities[i] + dp[i - 2], dp[i - 1])
        dp.append(result)

print(dp[-1])