import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

figure = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
result = []

def dfs_recur(x, y) :
    global count
    
    if x < 0 or y < 0 or x >= m or y >= n :
        return False
    elif figure[y][x] == 1 :
        figure[y][x] = 0
        count += 1
        for d in range (4) :
            dfs_recur(x+dx[d], y+dy[d])
        return True

for x in range (m) :
    for y in range (n) :
        if dfs_recur(x, y) :
            result.append(count)
            count = 0
if len(result) :
    print(len(result))
    print(max(result))
else :
    print("0")
    print("0")