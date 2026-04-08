import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

land = list(list(map(int, input().split())) for _ in range(n))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0

def dfs_recur(x, y, rain) :
    global tmp_land
    
    if x < 0 or y < 0 or x >= n or y >= n :
        return False
    
    elif tmp_land[x][y] > rain :
        tmp_land[x][y] = 0
        for d in range (4) :
            dfs_recur(x+dx[d], y+dy[d], rain)
        return True

rain_max = max(map(max, land))
result = [1]
for rain in range(1, rain_max) :
    tmp_land = [row[:] for row in land] # deepcopy
    for x in range (n) :
        for y in range (n) :
            if dfs_recur(x, y, rain) :
                count += 1
    result.append(count)
    count = 0
    
print(max(result))