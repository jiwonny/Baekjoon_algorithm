import sys
import unittest

class Problem:
  memoryList = None

  @classmethod
  def run(cls, n = None):
    if n is None:
      n = int(sys.stdin.readline())

    cls.memoryList = [None] * (n + 1)
    if n == 0:
      cls.memoryList[0] = 1
    if n >= 1:
      cls.memoryList[0], cls.memoryList[1] = 1, 1

    result = cls.__factorial(n)
    print(result)
    return result

  @classmethod  
  def __factorial(cls, n):
    if cls.memoryList[n]:
      return cls.memoryList[n]
    
    result = n * cls.__factorial(n - 1)
    cls.memoryList[n] = result
    return result

class Test(unittest.TestCase):
  def test1(self):
    result = Problem.run(0)
    self.assertEqual(result, 1)
  
  def test2(self):
    result = Problem.run(1)
    self.assertEqual(result, 1)

  def test3(self):
    result = Problem.run(3)
    self.assertEqual(result, 6)
  
  def test4(self):
    result = Problem.run(10)
    self.assertEqual(result, 3628800)

  def test5(self):
    result = Problem.run(12)
    self.assertEqual(result, 479001600)

if __name__ == "__main__":
  unittest.main()
  Problem.run()