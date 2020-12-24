import sys

n = int(sys.stdin.readline())
s = []
index = []
pairs = []

for i in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))
    index.append(i)

minimum = 9999999


def dfs_team(rem, res = []):
    if len(res) == 2:
        global pairs
        pairs.append(res[0:])
        return

    for i in range(len(rem)):
        res.append(rem[i])
        dfs_team(rem[i+1:], res)
        res.pop()


def dfs(rem, res = []):
    if len(res) == n / 2:
        global pairs
        global minimum
        total1, total2 = 0, 0
        another = list(set(index).difference(res))
        
        for pair in pairs:
            player1 = res[pair[0]]
            player2 = res[pair[1]]
            total1 += s[player1][player2] + s[player2][player1]

            player3 = another[pair[0]]
            player4 = another[pair[1]]
            total2 += s[player3][player4] + s[player4][player3]
        
        minimum = min(minimum, abs(total1- total2))
        return
        # dfs_team(list(range(0, len(res))), res = [])
    
        # minimum = min(minimum, res)

    for i in range(len(rem)):
        res.append(rem[i])
        dfs(rem[i+1:], res)
        res.pop()
        
dfs_team(list(range(0, n // 2)))
dfs(rem = index, res = [])
print(minimum)