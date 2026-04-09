import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

campus = []

campus = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_recur(x, y) :
    global count, t
    if x < 0 or y < 0 or x >= m or y >= n :
        return False
    
    elif campus[y][x] == 'O' or campus[y][x] == 'P' or campus[y][x] == 'I':
        if campus[y][x] == 'P' :
            count += 1
        if campus[y][x] == 'I' :
            t = True
        campus[y][x] = 'X'
        for d in range (4) :
            dfs_recur(x+dx[d],y+dy[d])

            
        return True
    
count = 0
area = []
t = False
for x in range (m) :
    for y in range (n) :
        if dfs_recur(x, y) :
            area.append([count, t])
            count, t = 0, False

for k in range(len(area)) :
    if area[k][1] :
        if area[k][0] == 0 :
            print('TT')
        else :
            print(area[k][0])