def solution(N):
  for num in range(1, N):
    digits = list(map(int, str(num)))
    total = num + sum(digits)
    if total == N:
      return num
  return 0

def main():
  N = int(input())
  result = solution(N)
  print(result)

main()
  