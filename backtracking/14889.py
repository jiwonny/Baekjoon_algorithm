import sys

pairs = []
abilities = []
minimum = sys.maxsize

def make_pairs(remain, result):
	if len(result) == 2:
		pairs.append([] + result)
		return

	for i in range(len(remain)):
		result.append(remain[i])
		make_pairs(remain[i + 1:], result)
		result.pop()

def backtracking(remain, result, N):
	if len(result) == N // 2:
		global minimum
		total_1 = 0
		total_2 = 0
		another = list(set(list(range(N))).difference(set(result)))

		for pair in pairs:
			player1 = result[pair[0]]
			player2 = result[pair[1]]
			total_1 = total_1 + abilities[player1][player2] + abilities[player2][player1]

			player3 = another[pair[0]]
			player4 = another[pair[1]]
			total_2 = total_2 + abilities[player3][player4] + abilities[player4][player3]

		minimum = min(minimum, abs(total_1 - total_2))	
		return
	
	for i in range(len(remain)):
		result.append(remain[i])
		backtracking(remain[i + 1:], result, N)
		result.pop()

def main():
	N = int(sys.stdin.readline())
	for _ in range(N):
		abilities.append(list(map(int, sys.stdin.readline().split())))

	make_pairs(list(range(N // 2)), [])
	backtracking(list(range(N)), [], N)
	print(minimum)

main()