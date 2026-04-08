import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n, k = map(int, input().split())

figure = list([0]*n for _ in range (m))
rec = []

for _ in range (k) :
    rec.append(list(map(int, input().split())))


for i in range(k) :
    for x in range(rec[i][0], rec[i][2]) :
        for y in range(rec[i][1], rec[i][3]) :
            figure[y][x] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = []
count = 0

def dfs_recur(x, y) :
    global count
    if x < 0 or y < 0 or x >= n or y >= m :
        return False
    
    elif figure[y][x] == 0 :
        count += 1
        figure[y][x] = 1
        for d in range (4) :
            dfs_recur(x+dx[d], y+dy[d])
        return True

for x in range (n) :
    for y in range (m) :
        if dfs_recur(x, y) :
            arr.append(count)
            count = 0

print(len(arr))
for node in (sorted(arr)) :
    print(node, end=' ')