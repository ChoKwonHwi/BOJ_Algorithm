from collections import deque
import sys
input = sys.stdin.readline
def bfs (graph, start, visited):
    global number, count
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        number[v] = count
        count += 1
        
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
                
                

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    u, v = map(int, input().split())    
    graph[u].append(v)
    graph[v].append(u)
    
for num in range(1, len(graph)) :
    if graph[num] :
        graph[num] = sorted(graph[num])

count = 1       
number = [0]*(n+1)
visited = [False] * (n+1)
visited[0] = True

bfs(graph, r, visited)
for k in range(1, n+1) :
    print(number[k])