# mock & backtracking 방식으로 풀어보기 -> 런타임 에러

import unittest

from unittest.mock import patch

SELECT_NUM = 3

class Problem:
  maximum = 0

  @classmethod
  def main(cls):
    N, M = map(int, input().split())
    cls.M = M
    cards = list(map(int, input().split()))
    
    result = cls.__get_answer(cards, card_count = 0, total = 0)
    return cls.maximum

  @classmethod
  def __get_answer(cls, remain, card_count, total):
    if card_count == SELECT_NUM:
      if cls.maximum < total <= cls.M:
        cls.maximum = total
      return

    for i in range(len(remain)):
      selected_card = remain[i]
      cls.__get_answer(remain[i + 1:], card_count + 1, total + selected_card)
    
    return cls.maximum

class Test(unittest.TestCase):
  def test1(self):
    prompt_input = [
      '5 21',
      '5 6 7 8 9'
    ]

    with patch('builtins.input', side_effect = prompt_input):
      ans = Problem.main()
    
    self.assertEqual(ans, 21)

  def test2(self):
    prompt_input = [
      '10 500',
      '93 181 245 214 315 36 185 138 216 295'
    ]

    with patch('builtins.input', side_effect = prompt_input):
      ans = Problem.main()
    
    self.assertEqual(ans, 497)

if __name__ == "__main__":
  # print(Problem.main())
  unittest.main()