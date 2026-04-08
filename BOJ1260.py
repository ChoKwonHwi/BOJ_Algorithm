# https://www.acmicpc.net/workbook/view/1833
from collections import deque

def dfs(graph, v, visited) : 
    visited[v] = True
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)
            
def bfs (graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())

xx = list(list(map(int, input().split())) for _ in range(m))
graph = [[] for _ in range(n+1)]
for k in xx :
    graph[k[0]].append(k[1])
    graph[k[1]].append(k[0])

for num in range(1, len(graph)) :
    if graph[num] :
        graph[num] = sorted(graph[num])
    
visited = [False] * (n+1)
dfs(graph, v, visited)
print("")
visited = [False] * (n+1)
bfs(graph, v, visited)