# https://www.acmicpc.net/problem/12865
# 평범한 배낭

import sys

N, K = map(int, sys.stdin.readline().split())

# 배낭에 넣을 수 있는 물건들의 가치합의 최댓값
lst = []
dp = [0] * (K + 1)
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    w, v = lst[i]
    for j in range(K, -1, -1):
        if w <= j:
            dp[j] = max(dp[j], dp[j - w] + v)
    
print(dp[-1])
