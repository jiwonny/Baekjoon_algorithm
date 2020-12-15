import sys
import unittest

memoryList = []
def fibonacci(n):
  if memoryList[n] is not None:
    return memoryList[n]

  value = fibonacci(n - 1) + fibonacci(n - 2)
  memoryList[n] = value
  return value

def run(n = None):
  if n is None:
    n = int(sys.stdin.readline())
  
  memoryList.extend([None] * (n + 1))
  if n >= 1:
    memoryList[1] = 1
  if n >= 0:
    memoryList[0] = 0
  
  result = fibonacci(n)
  return result

class Test(unittest.TestCase):
  def test1(self):
    self.assertEqual(run(0), 0)

  def test2(self):
    self.assertEqual(run(1), 1)

  def test3(self):
    self.assertEqual(run(10), 55)

  def test4(self):
    self.assertEqual(run(4), 3)

if __name__ == "__main__":
  print(run())