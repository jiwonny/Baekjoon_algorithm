import sys
import unittest

def getAnswer(N, M, cards):
  maximum = 0
  for first in range(N - 2):
    for second in range(first + 1, N - 1):
      for third in range(second + 1, N):
        total = cards[first] + cards[second] + cards[third]
        if total <= M and total > maximum:
          maximum = total
  
  return maximum

def run():
  N, M = map(int, sys.stdin.readline().split())
  cards = list(map(int, sys.stdin.readline().split()))
  
  result = getAnswer(N, M, cards)
  print(result)
  
  
class Test(unittest.TestCase):
  def test1(self):
    N, M, cards = 5, 21, [5, 6, 7, 8, 9]
    self.assertEqual(getAnswer(N, M, cards), 21)

  def test2(self):
    N, M, cards = 10, 500, [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
    self.assertEqual(getAnswer(N, M, cards), 497)

if __name__ == "__main__":
  run()