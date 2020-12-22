import unittest
from unittest.mock import patch
from io import StringIO

def main():
	N = int(input())
	coordinates = []
	for _ in range(N):
		x, y = map(int, input().split())
		coordinates.append((y, x))

	sorted_coordinates = sorted(coordinates)
	for pair in sorted_coordinates:
		print(' '.join(map(str, (pair[1], pair[0]))))

class Test(unittest.TestCase):
	@patch('sys.stdout', new_callable = StringIO)
	def assert_stdout(self, expected_output, mock_stdout):
		main()
		self.assertEqual(mock_stdout.getvalue(), expected_output)

	def test1(self):
		prompt_input = "5\n0 4\n1 2\n1 -1\n2 2\n3 3\n"
		expected_output = "1 -1\n1 2\n2 2\n3 3\n0 4\n"

		with patch('sys.stdin', StringIO(prompt_input)):
			self.assert_stdout(expected_output)
	
if __name__ == "__main__":
	unittest.main()
	# main()