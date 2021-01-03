dp = {
	(0, 0, 1): 1
}

def func(a, b, c):
	if (a, b, c) in dp:
		return dp[(a, b, c)]

	if a <= 0 or b <= 0 or c <= 0:
		dp[(a, b, c)] = 1
	elif a > 20 or b > 20 or c > 20:
		dp[(a, b, c)] = func(20, 20, 20)
	elif a < b and b < c:
		dp[(a, b, c)] = func(a, b, c - 1) + func(a, b - 1, c - 1) - func(a, b - 1, c)
	else:
		dp[(a, b, c)] = func(a - 1, b, c) + func(a - 1, b - 1, c) + func(a - 1, b, c - 1) - func(a - 1, b - 1, c - 1)

	return dp[(a, b, c)]

while True:
	a, b, c = map(int, input().split())
	if a == -1 and b == -1 and c == -1:
		break
	
	result = func(a, b, c)
	print('w(%d, %d, %d) = %d' % (a, b, c, result))