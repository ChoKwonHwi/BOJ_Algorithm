from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sea = list(list(map(int, input().split())) for _ in range(n))

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

shark = []

for y in range(n) :
    for x in range(m) :
        if sea[y][x] == 1 :
            shark.append([x, y])

safe_zone = list([0]*m for _ in range(n))

def bfs(shark) :
    queue = deque()
    for s in shark :
        queue.append(s)
        
    while queue :
        x, y= queue.popleft()
        
        for d in range(8) :
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < m and 0 <= ny < n and safe_zone[ny][nx] == 0 :
                safe_zone[ny][nx] = safe_zone[y][x] + 1
                queue.append([nx, ny])

bfs(shark)

answer = 0

for x in range(m) :
    for y in range(n) :
        answer = max(answer, safe_zone[y][x])