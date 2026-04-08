def dfs(graph, v, visited) :
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)
    return visited            

n = int(input())
e = int(input())

v = list(list(map(int, input().split())) for _ in range (e))
graph = list([] for _ in range (n+1))

for x in v :
    graph[x[0]].append(x[1])
    graph[x[1]].append(x[0])

visited = [False] * (n+1)
final_visit = dfs(graph, 1, visited)
print(final_visit.count(True)-1)