import unittest
from unittest.mock import patch
from io import StringIO

def main():
    N = int(input())
    info_list = []

    for i in range(N):
        age, name = input().split()
        info_list.append((int(age), name, i))

    sorted_list = sorted(info_list, key = lambda x : (x[0], x[2]))
    for info in sorted_list:
        print(' '.join(map(str, (info[0], info[1]))))

class Test(unittest.TestCase):
    @patch('sys.stdout', new_callable = StringIO)
    def assert_equal(self, predicted_value, sys_out):
        main()
        self.assertEqual(predicted_value, sys_out.getvalue())
    
    def test1(self):
        prompted_input = "3\n21 Junkyu\n21 Dohyun\n20 Sunyoung"
        predicted_value = "20 Sunyoung\n21 Junkyu\n21 Dohyun\n"

        with patch('sys.stdin', StringIO(prompted_input)):
            self.assert_equal(predicted_value)

if __name__ == "__main__":
    unittest.main()