import unittest
from unittest.mock import patch

def solution(N, measurements):
  ranks = [1] * N
  for i in range(N - 1):
    for j in range(i + 1, N):
      if measurements[i]['weight'] > measurements[j]['weight'] and measurements[i]['height'] > measurements[j]['height']:
        ranks[j] += 1
      
      if measurements[i]['weight'] < measurements[j]['weight'] and measurements[i]['height'] < measurements[j]['height']:
        ranks[i] += 1

  return ranks

def main():
  N = int(input())
  measurements = []
  for i in range(N):
    weight, height = map(int, input().split())
    measurements.append({
      'weight': weight,
      'height': height,
    })

  result = solution(N, measurements)
  return ' '.join(map(str, result))
  

class Test(unittest.TestCase):
  def test1(self):
    prompt_input = [
      '5',
      '55 185',
      '58 183',
      '88 186',
      '60 175',
      '46 155',
    ]

    with patch('builtins.input', side_effect = prompt_input):
      answer = main()
    
    self.assertEqual('2 2 1 2 5', answer)
  

if __name__ == "__main__":
  # unittest.main()
  print(main())