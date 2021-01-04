N = int(input())

counts = []

for i in range(N):
    if i == 0:
        first_row = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        counts.append(first_row)
    else:
        row = []
        for j in range(10):
            if j == 0:
                row.append(counts[i - 1][j + 1])
            elif j == 9:
                row.append(counts[i - 1][j - 1])
            else:
                row.append(counts[i - 1][j - 1] + counts[i - 1][j + 1])
        counts.append(row)

print(sum(counts[-1]) % 1000000000)