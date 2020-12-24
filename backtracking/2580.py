import sys

SIZE = 9
boards = []
zeros = []
for _ in range(SIZE):
	boards.append(list(map(int, input().split())))

for row in range(SIZE):
	for col in range(SIZE):
		if boards[row][col] == 0:
			zeros.append([row, col])

def check_lines(current, num):
	row, col = zeros[current]
	if num in boards[row]:
		return False

	for j in range(SIZE):
		if num == boards[j][col]:
			return False

	return True

def check_square(current, num):
	row, col = zeros[current]
	start_row = row // 3 * 3
	start_col = col // 3 * 3

	for i in range(start_row, start_row + 3):
		for j in range(start_col, start_col + 3):
			if boards[i][j] == num:
				return False
	return True

def backtracking(current, zeros_count):
	if current == zeros_count:
		for row in boards:
			print(' '.join(map(str, row)))
		sys.exit()
	
	for num in range(1, SIZE + 1):
		if check_square(current, num) and check_lines(current, num):
			row, col = zeros[current]
			boards[row][col] = num
			backtracking(current + 1, zeros_count)
			boards[row][col] = 0

backtracking(0, len(zeros))