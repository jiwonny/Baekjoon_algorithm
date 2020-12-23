answers = []

def backtracking(result, remain, M):
	if len(result) == M:
		answers.append([] + result)
		return

	for i in range(len(remain)):
		num = remain[i]
		result.append(num)
		backtracking(result, remain[i:], M)
		result.pop()

def main():
	N, M = map(int, input().split())
	lst = [x for x in range(1, N + 1)]
	backtracking([], lst, M)
	for answer in answers:
		print(' '.join(map(str, answer)))
	
main()