from collections import deque
import sys
input = sys.stdin.readline

def bfs (graph, start) :
    global way
    queue = deque([start])
    way[start] = 0
    
    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if way[i] == -1 :
                queue.append(i)
                way[i] = way[v] + 1
    
    
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)

way = [-1] * (n+1)
bfs(graph, x)

if not k in way :
    print('-1')
    exit()
else :
    for i in range(1, len(way)) :
        if way[i] == k :
            print(i)