import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
# + - * /
operator_count = list(map(int, sys.stdin.readline().split()))
results = []


def get_result(oper_list):
	result = numbers[0]
	for i in range(1, N):
		if oper_list[i - 1] == 0:
			result += numbers[i]
		elif oper_list[i - 1] == 1:
			result -= numbers[i]
		elif oper_list[i - 1] == 2:
			result *= numbers[i]
		elif oper_list[i - 1] == 3:
			result = int(result / numbers[i])
	
	return result
		
def backtracking(oper_list):
	if len(oper_list) == N - 1:
		result = get_result(oper_list)
		results.append(result)
		return

	for operator in range(4):
		if operator_count[operator] > 0:
			operator_count[operator] -= 1
			oper_list.append(operator)
			backtracking(oper_list)
			oper_list.pop()
			operator_count[operator] += 1

backtracking([])
print(max(results))
print(min(results))
