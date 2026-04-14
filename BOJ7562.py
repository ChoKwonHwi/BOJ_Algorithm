from collections import deque
import sys
input = sys.stdin.readline

test_case = int(input())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(knight_x, knight_y, fin_x, fin_y, chess) :
    if knight_x == fin_x and knight_y == fin_y :
        print(0)
        return
    
    queue = deque()
    queue.append((knight_x, knight_y))
    
    while queue :
        x, y = queue.popleft()
        
        for d in range(8):
            nx, ny = x+dx[d], y+dy[d]
            if 0<=nx<I and 0<=ny<I and chess[ny][nx] == 0 :
                if nx == fin_x and ny == fin_y :
                    print(chess[y][x]+1)
                    return
                queue.append((nx, ny))
                chess[ny][nx] = chess[y][x]+1
                
for _ in range (test_case) :
    I = int(input())
    chess = list([0]*I for _ in range(I))
    knight_x, knight_y = map(int, input().split())
    fin_x, fin_y = map(int, input().split())
    
    bfs(knight_x, knight_y, fin_x, fin_y, chess)
    