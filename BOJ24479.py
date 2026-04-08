import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range (n+1)]

for _ in range (m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range (len(graph)) :
    graph[i] = sorted(graph[i])
 
def dfs_recur(graph, v, visited, result) :
    global count
    visited[v] = True
    result[v] = count
    count += 1
    for i in graph[v] :
        if not visited[i] :
            dfs_recur(graph, i, visited, result)
            
    
result = [0] * (n+1)
count = 1
visited = [False] * (n+1)
dfs_recur(graph, r, visited, result)
for i in range (1, len(result)) :
    print(result[i])