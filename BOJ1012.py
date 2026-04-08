import sys
sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y) :
    global count, farm
    
    if x < 0 or y < 0 or x >= m or y >= n :
        return False
    elif farm[y][x] == 1 :
        count += 1
        farm[y][x] = 0
        for d in range(4) :
            dfs(x+dx[d], y+dy[d])
        return True

for _ in range(t) :
    m, n, k = map(int, input().split())

    farm = list([0]*m for _ in range (n))

    for _ in range(k) :
        x, y = map(int, input().split())
        farm[y][x] = 1
    answer = []
    count = 0
        
    for i in range (m) :
        for j in range(n) :
            if dfs(i, j) :
                answer.append(1)
                count = 0
    print(len(answer))
