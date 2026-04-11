import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

city = list(list(map(int, input().split())) for _ in range (m))

result = False
dx = [1, 0]
dy = [0, 1]

def dfs_recur(x, y) :
    global result
    if x < 0 or y < 0 or x >= n or y >= m :
        return False
    elif city[y][x] == 1 :
        if x == n-1 and y == m-1 :
            result = True
        city[y][x] = 0
        for d in range(2) :
            dfs_recur(x+dx[d], y+dy[d])
        return True      

if dfs_recur(0, 0) :
    if result == True :
        print("Yes")
    else :
        print("No")