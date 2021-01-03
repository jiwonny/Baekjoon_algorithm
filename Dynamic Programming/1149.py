import sys

num = int(sys.stdin.readline())
lst = []

for _ in range(num):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, num):
    lst[i][0] = min(lst[i - 1][1], lst[i - 1][2]) + lst[i][0]
    lst[i][1] = min(lst[i - 1][0], lst[i - 1][2]) + lst[i][1]
    lst[i][2] = min(lst[i - 1][0], lst[i - 1][1]) + lst[i][2]

print(min(lst[num - 1]))