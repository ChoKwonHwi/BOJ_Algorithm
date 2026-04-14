from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

maze = list(map(int, input().split()))

visited = [0]*(n+1)

def bfs(visited) :
    if n == 1 :
        print(0)
        return
    
    queue = deque()
    queue.append(0)
    
    while queue :
        now = queue.popleft()
        
        if maze[now] == 0 :
            continue
        
        for k in range(1, maze[now]+1) :
            if  now+k < n and visited[now+k] == 0 :
                if now+k == n-1 :
                    print(visited[now]+1)
                    return
                visited[now+k] = visited[now]+1
                queue.append(now+k)
    print(-1)

bfs(visited)
        
        