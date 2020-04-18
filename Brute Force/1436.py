# https://www.acmicpc.net/problem/1436
# 영화감독 숌

import sys

N = int(sys.stdin.readline())

answer = 666
count = 1
while count < N:
    answer += 1
    if '666' in str(answer):
        count += 1

print(answer)

    
    
    