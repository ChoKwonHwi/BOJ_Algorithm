def dfs(graph, v, visited) : # node가 list로 표현되어있을 때 재귀 식
    visited[v] = True
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)
            
def dfs_stack_graph(graph, start, visited):
    stack = [start]
    visited[start] = True
    
    while stack:
        v = stack.pop()
        print(v, end=' ')
        for i in reversed(graph[v]):
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                            
def dfs_stack_array(graph, visited) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    stack = [(0, 0)]
    visited[0][0] = True

    while stack :
        x, y = stack.pop()
        
        print(x, y)
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) :
                if not visited[nx][ny] and graph[nx][ny] == 'O' :
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                    
graph = [
        ['O', 'O', 'O', 'O', 'O', 'X'],
        ['O', 'O', 'O', 'O', 'X', 'O'],
        ['O', 'O', 'O', 'X', 'O', 'O'],
        ['O', 'O', 'X', 'O', 'O', 'O'],
        ['X', 'O', 'O', 'O', 'O', 'O'],
    ]

# 노드별 방문 정보
visited = [[False] * len(graph[0]) for _ in range(len(graph))]

dfs_stack_array(graph, visited)