import unittest
from unittest.mock import patch
from io import StringIO

def main():
	N = int(input())
	coordinates = []
	for _ in range(N):
		x, y = map(int, input().split())
		coordinates.append((x, y))

	sorted_coordinates = sorted(coordinates)
	for pair in sorted_coordinates:
		print(' '.join(map(str, pair)))

class Test(unittest.TestCase):
	@patch('sys.stdout', new_callable = StringIO)
	def assert_stdout(self, expected_output, mock_stdout):
		main()
		self.assertEqual(mock_stdout.getvalue(), expected_output)

	def test1(self):
		prompt_input = [
			'5',
			'3 4',
			'1 1',
			'1 -1',
			'2 2',
			'3 3'
		]
		expected_output = "1 -1\n1 1\n2 2\n3 3\n3 4\n"

	
		with patch('builtins.input', side_effect = prompt_input):
			self.assert_stdout(expected_output)
	
if __name__ == "__main__":
	# unittest.main()
	main()