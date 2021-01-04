N = int(input())

numbers = list(map(int, input().split()))
ranks = [0] * N
rev_ranks = [0] * N

for i in range(N):
    if i == 0:
        ranks[i] = 1
        continue

    for j in range(i):
        if numbers[j] < numbers[i] and ranks[j] > ranks[i]:
            ranks[i] = ranks[j]
    
    ranks[i] += 1

for i in range(N - 1, -1, -1):
    if i == N - 1:
        rev_ranks[i] = 1
        continue

    for j in range(i + 1, N):
        if numbers[j] < numbers[i] and rev_ranks[j] > rev_ranks[i]:
            rev_ranks[i] = rev_ranks[j]
    
    rev_ranks[i] += 1


for i in range(N):
    ranks[i] = ranks[i] + rev_ranks[i] - 1

print(max(ranks))