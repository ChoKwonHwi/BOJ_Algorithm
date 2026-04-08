import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

figure = list(list(input().rstrip()) for _ in range(n))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
count2 = 0

def dfs_recur_1(x, y) :
    global tmp_figure
    
    if x < 0 or y < 0 or x >= n or y >= n :
        return False
    
    elif tmp_figure[x][y] == 'R' or tmp_figure[x][y] == 'G' :
        tmp_figure[x][y] = 'X'
        for d in range (4) :
            dfs_recur_1(x+dx[d], y+dy[d])
        return True


def dfs_recur_2(x, y, opt) :
    global tmp_figure
    
    if x < 0 or y < 0 or x >= n or y >= n :
        return False
    
    elif tmp_figure[x][y] == opt :
        tmp_figure[x][y] = 'X'
        for d in range (4) :
            dfs_recur_2(x+dx[d], y+dy[d], opt)
        return True

tmp_figure = [row[:] for row in figure] # deepcopy
for x in range(n) :
    for y in range(n) :
        if dfs_recur_2(x, y, 'R') :
            count += 1
for x in range(n) :
    for y in range(n) :
        if dfs_recur_2(x, y, 'G') :
            count += 1
for x in range(n) :
    for y in range(n) :
        if dfs_recur_2(x, y, 'B') :
            count += 1

tmp_figure = [row[:] for row in figure]

for x in range(n) :
    for y in range(n) :
        if dfs_recur_2(x, y, 'B') :
            count2 += 1
for x in range(n) :
    for y in range(n) :
        if dfs_recur_1(x, y) :
            count2 += 1 
            
print(count, count2)