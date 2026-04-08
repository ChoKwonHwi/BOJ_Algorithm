import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

rel = [[] for _ in range(n)]

for _ in range (m) :
    a, b = map(int, input().split())
    rel[b].append(a)
    rel[a].append(b)

def dfs_recur(graph, v, visited, dep) :
    global result
    visited[v] = True
    if dep == 4 :
        result = True
        return
    for i in graph[v] :
        if not visited[i] :
            visited[i] = True
            dfs_recur(graph, i, visited, dep+1)
            visited[i] = False
visited = [False] * n

result = False
dep = 0
for i in range (n) :
    dfs_recur(rel, i, visited, dep)
    visited[i] = False
    if result :
        break
if result :
    print(1)
else :
    print(0)