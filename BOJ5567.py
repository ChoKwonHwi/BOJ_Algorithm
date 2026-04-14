from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = list([] for _ in range(n+1))

for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(graph, start, visited) :
    global count
    queue = deque()
    queue.append((start, 0))
    
    while queue :
        friends, cnt = queue.popleft()
        
        if cnt < 2 :
            for friend in graph[friends] :
                if not visited[friend] :
                    count+=1
                    queue.append((friend, cnt+1))
                    visited[friend] = True
    
visited = [False] * (n+1)
visited[1] = True
count = 0
bfs(graph, 1, visited)
print(count)