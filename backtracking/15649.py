import unittest
from unittest.mock import patch
from io import StringIO

answers = []

def backtracking(result, remain, M):
	if len(result) == M:
		result_to_append = []
		result_to_append += result
		answers.append(result_to_append)
		return
	
	for i in range(len(remain)):
		num = remain.pop(i)
		result.append(num)
		backtracking(result, remain, M)
		result.pop()
		remain.insert(i, num)


def main():
	N, M = map(int, input().split())
	lst = [x for x in range(1, N + 1)]
	backtracking([], lst, M)
	for answer in answers:
		print(' '.join(map(str,)))
	
main()