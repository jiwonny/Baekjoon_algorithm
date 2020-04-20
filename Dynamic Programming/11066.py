# https://www.acmicpc.net/problem/11066
# 파일 합치기

import sys

def getCost(n, values, sum_lst):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(i - 1, 0, -1):
            dp[j][i] = 99999999
            for s in range(j, i):
                dp[j][i] = min(dp[j][i], dp[j][s] + dp[s + 1][i])
            
            dp[j][i] += sum_lst[i] - sum_lst[j - 1]
        
    return dp[1][n]


tcase = int(sys.stdin.readline())

for _ in range(tcase):
    K = int(sys.stdin.readline())
    lst = [0]
    lst.extend(list(map(int, sys.stdin.readline().split())))
    sum_lst = [0] * (K + 1)
    for i in range(1, K + 1):
        sum_lst[i] = sum_lst[i - 1] + lst[i]

    print(getCost(K, lst, sum_lst))

