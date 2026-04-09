import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r, c = map(int, input().split())

farm = [list(input().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

wolf, sheep = 100000, 100000
def dfs_recur(x, y) :
    global wolf, sheep
    if x < 0 or y < 0 or x >= c or y >= r :
        return False
    elif farm[y][x] == '.' or farm[y][x] == 'v' or farm[y][x] == 'o' :
        if farm[y][x] == 'v' :
            wolf += 1
        elif farm[y][x] == 'o' :
            sheep += 1
        farm[y][x] = '#'
        
        for d in range(4) :
            dfs_recur(x+dx[d], y+dy[d])
            
        return True
    
alive_wolf, alive_sheep = 0, 0

for x in range(c) :
    for y in range(r) :
        if dfs_recur(x, y) :
            if not (wolf == 100000 and sheep == 100000) :
                
                wf = wolf-sheep
                if wf > 0 :
                    alive_wolf += (wolf-100000)
                elif wf == 0 :
                    alive_wolf += (wolf-100000)
                else :
                    alive_sheep += (sheep-100000)
            wolf, sheep = 100000, 100000
print(alive_sheep, alive_wolf)