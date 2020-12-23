answers = 0
N = int(input())
vertical = [True] * N
diag1 = [True] * (2 * N - 1)
diag2 = [True] * (2 * N - 1)

def backtracking(horse, N):
	if horse == N:
		global answers
		answers += 1
		return

	for i in range(N):
		if vertical[i] and diag1[horse + i] and diag2[N - 1 + horse - i]:
			vertical[i] = False
			diag1[horse + i] = False
			diag2[N - 1 + horse - i] = False
			backtracking(horse + 1, N)
			vertical[i] = True
			diag1[horse + i] = True
			diag2[N - 1 + horse - i] = True

backtracking(0, N)
print(answers)

