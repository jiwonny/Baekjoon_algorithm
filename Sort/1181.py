import unittest
from unittest.mock import patch
from io import StringIO

def main():
	N = int(input())
	string_set = set()

	for _ in range(N):
		string = input()
		string_set.add(string)

	sorted_list = sorted(list(string_set), key = lambda x : (len(x), x))
	print('\n'.join(sorted_list))

class Test(unittest.TestCase):
	@patch('sys.stdout', new_callable = StringIO)
	def assert_output(self, predicted_value, sys_out):
		main()
		self.assertEqual(predicted_value, sys_out.getvalue())

	def test1(self):
		prompted_value = "13\nbut\ni\nwont\nhesitate\nno\nmore\nno\nmore\nit\ncannot\nwait\nim\nyours"

		predicted_value = "i\nim\nit\nno\nbut\nmore\nwait\nwont\nyours\ncannot\nhesitate\n"
		with patch('sys.stdin', StringIO(prompted_value)):
			self.assert_output(predicted_value)

if __name__ == "__main__":
	unittest.main()