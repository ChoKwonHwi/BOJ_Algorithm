from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

farm = list(list(map(int, input().split())) for _ in range(n))

tomato = []


for y in range(n) :
    for x in range(m) :
        if farm[y][x] == 1 :
            tomato.append([x, y])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(tomato, visited) :
    queue = deque()
    for t in tomato :
        queue.append(t)
        
    while queue :
        x, y = queue.popleft()
        
        for d in range(4) :
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0 :
                if farm[ny][nx] == 0 :
                    queue.append([nx, ny])
                    visited[ny][nx] = visited[y][x] + 1
                    
                
visited = list([0]*m for _ in range(n))

bfs(tomato, visited)

answer = 0

for y in range(n):
    for x in range(m):
        if farm[y][x] == 0 and visited[y][x] == 0:
            print(-1)
            exit()
        answer = max(answer, visited[y][x])

print(answer)