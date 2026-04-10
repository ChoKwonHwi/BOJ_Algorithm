import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

war = list(list(input().strip()) for _ in range (m))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_recur_blue(x, y) :
    global blue_cnt
    if x < 0 or y < 0 or x >= n or y >= m :
        return False
    elif war[y][x] == 'B' :
        war[y][x] = 'X'
        blue_cnt += 1
        for d in range(4) :
            dfs_recur_blue(x+dx[d], y+dy[d])
        return True


def dfs_recur_white(x, y) :
    global white_cnt
    if x < 0 or y < 0 or x >= n or y >= m :
        return False
    elif war[y][x] == 'W' :
        war[y][x] = 'X'
        white_cnt += 1
        for k in range(4) :
            dfs_recur_white(x+dx[k], y+dy[k])
        return True

blue, white = 0, 0
blue_cnt, white_cnt = 0, 0

for x in range (n) :
    for y in range(m) :
        if dfs_recur_blue(x, y) :
            blue += (blue_cnt**2)
        if dfs_recur_white(x, y) :
            white += (white_cnt**2)
        blue_cnt, white_cnt = 0, 0
print(white, blue)