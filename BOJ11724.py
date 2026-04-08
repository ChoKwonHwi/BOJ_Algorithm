import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(n+1)
visited[0] = True
cnt = 0

def dfs_recur(graph, v, visited) :
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            dfs_recur(graph, i, visited)

for index in range(len(visited)) :
    if not visited[index] :
        dfs_recur(graph, index, visited)
        cnt += 1

print(cnt)
