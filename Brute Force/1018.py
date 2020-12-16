import sys

N, M = map(int, input().split())
boards = []

for i in range(N):
  boards.append(list(input()))

minimum = sys.maxsize
colors = ['B', 'W']

for start_row in range(N - 7):
  for start_col in range(M - 7):
    for color_idx in range(len(colors)):
      count = 0
      for i in range(8):
        for j in range(8):
          if boards[start_row + i][start_col + j] != colors[color_idx % len(colors)]:
            count += 1
          color_idx += 1
        color_idx += 1
      minimum = min(minimum, count)

print(minimum)
