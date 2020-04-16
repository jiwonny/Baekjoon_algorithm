# https://www.acmicpc.net/problem/10217
# KCM TRAVEL
import sys

'''
D[i][j] 를 1번 도시에서 i 번 도시까지 비용 j 이하를 써서 갈 때 최소 시간.
D 테이블을 차례대로 K 개의 교통편을 확인하며 채워나감.
O(MNK)
'''

INF = sys.maxsize

def kcmTravel(N, M, links):
    mat = [[INF] * (M + 1) for _ in range(N + 1)]
    mat[1][0] = 0
    for i in range(M + 1):
        for j in range(1, N + 1):
            if mat[j][i] == INF:
                continue
            t = mat[j][i]

            for v, c, d in links[j]:
                if  M < c + i : 
                    continue
                mat[v][c + i] = min(mat[v][c + i], t + d)
                
    return min(mat[N])

tcase = int(sys.stdin.readline())

for _ in range(tcase):
    N, M, K = map(int, sys.stdin.readline().split())
    # 공항 수, 지원비용, 티켓정보의 수
    links = [[] for _ in range(N + 1)]
    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        # 출발, 도착, 비용, 소요시간
        # 비용 M 이하로 쓰면서 도착할 수 있는 가장 빠른 길.
        links[u].append([v, c, d])
    
    answer = kcmTravel(N, M, links)
    if answer >= INF:
        print('Poor KCM')
    else:
        print(answer)

