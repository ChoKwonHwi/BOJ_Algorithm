import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, k = map(int, input().split())

area = [[0] * m for _ in range (n)]

for _ in range (k) :
    r, c = map(int, input().split())
    area[r-1][c-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_recur(x, y) :
    global count
    if x < 0 or y < 0 or x >= m or y >= n :
        return False
    elif area[y][x] == 1 :
        count += 1
        area[y][x] = 0
        for d in range (4) :
            dfs_recur(x+dx[d], y+dy[d])
        return True

count = 0
arr = [0]
for x in range (m) :
    for y in range (n) :
        if dfs_recur(x, y) :
            arr.append(count)
            count = 0

print(max(arr))