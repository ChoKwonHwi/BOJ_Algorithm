from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 세로, m: 가로

farm = list(list(map(int, input().split())) for _ in range(n))

for i in range(n) :
    for j in range(m) :
        if farm[i][j] == 2 :
            x, y = j, i
            break
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
   
def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    
    while queue :
        a, b = queue.popleft()
        for i in range(4) :
            nx, ny = a+dx[i], b+dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1 :
                if farm[ny][nx] == 1 :
                    visited[ny][nx] = visited[b][a] + 1
                    queue.append((nx, ny))

visited = list([0]*(m) for _ in range (n))

for i in range(n):
    for j in range(m):
        if farm[i][j] == 1:
            visited[i][j] = -1
            
bfs(x, y, visited)
for row in visited :
    print(*row)