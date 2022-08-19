n = int(input())
fx = [0] + list(map(int, input().split()))

dp = [[fx[i]] for i in range(n+1)]

for j in range(1, 21) :
	for i in range(1, n+1) :
		dp[i].append(dp[dp[i][j-1]][j-1])
		
query = int(input())
for i in range(query) :
	x, k = map(int, input().split())
	for j in range(20, -1, -1) :
		bit = 1 << j
		if k >= bit :
			k -= bit
			x = dp[x][j]
	print(x)
