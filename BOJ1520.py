import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[-1] * n for _ in range(m)]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if area[ny][nx] < area[y][x]:
                dp[y][x] += dfs(nx, ny)

    return dp[y][x]

print(dfs(0, 0))