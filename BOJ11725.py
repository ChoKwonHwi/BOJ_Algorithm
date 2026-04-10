import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

tree = list([] for _ in range(n+1))

for i in range (n-1) :
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (n+1)
parent = [0] * (n+1)

def dfs_recur(graph, v) :
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            parent[i] = v
            dfs_recur(graph, i)
            
dfs_recur(tree, 1)
for i in range(2, len(parent)) :
    print(parent[i])