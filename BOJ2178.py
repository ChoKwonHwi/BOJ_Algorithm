from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited) :
    queue = deque()
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1 :
                if maze[ny][nx] == '1' :
                    queue.append((nx, ny))
                    visited[ny][nx] = visited[y][x] + 1
            

maze = list(list(input().strip()) for _ in range (n)) 

visited = list([-1]*m for _ in range(n))
visited[0][0] = 1
bfs(0, 0, visited)
print(visited[n-1][m-1])