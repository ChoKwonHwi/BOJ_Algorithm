n = int(input())
x, y = map(int, input().split())
m = int(input())
family = list(list(map(int, input().split())) for _ in range(m))

graph = [[] for _ in range(n+1)]
visited = []

for rel in family :
    graph[rel[0]].append(rel[1])
    graph[rel[1]].append(rel[0])
    
def dfs_recur(graph, v, cnt, visited) :
    check = graph[v]
    cnt+=1
    visited.append(v)
    if y in check :
        print(cnt)
        exit()
    for i in check :
        if i not in visited :
            dfs_recur(graph, i, cnt, visited)

dfs_recur(graph, x, 0, visited)

print("-1")