import sys

moves = []

def hanoi(n, start, end, mid):
  if n == 1:
    moves.append((start, end))
  else:
    hanoi(n - 1, start, mid, end)
    moves.append((start, end))
    hanoi(n - 1, mid, end, start)


n = int(sys.stdin.readline())
hanoi(n, 1, 3, 2)
print(len(moves))
for move in moves:
  print(' '.join(map(str, move)))
