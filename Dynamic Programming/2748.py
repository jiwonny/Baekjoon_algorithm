dp = {
	0: 0,
	1: 1,
}

def fibonacci(n):
	if n in dp:
		return dp[n]
	else:
		dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
		return dp[n]

def main():
	n = int(input())
	print(fibonacci(n))

main()