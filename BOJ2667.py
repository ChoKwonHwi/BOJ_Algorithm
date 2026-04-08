import sys

n = int(sys.stdin.readline())
graph = list(list(sys.stdin.readline().rstrip()) for _ in range(n))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y) :
    global count, graph
    if x < 0 or y < 0 or x >= n or y >= n :
        return False
    
    elif graph[x][y] == '1' :
        graph[x][y] = '0'
        count += 1
        for i in range(4) :
            dfs(x+dx[i], y+dy[i])
        return True
             
    
answer = []
count = 0
for i in range(n) :
    for j in range(n) :
        if dfs(i, j) :
            answer.append(count)
            count = 0
print(len(answer))
for i in sorted(answer) :
    print(i)