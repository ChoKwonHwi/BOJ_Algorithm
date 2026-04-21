import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
x = int(input())

dp = [0]*(x+1)
def dynamic(x) :
    if x == 1 :
        return 0
    if dp[x] :
        return dp[x]
    case1 = case2 = case3 = 10e6
    if x % 3 == 0:
        case1 = dynamic(x // 3)
    if x % 2 == 0:
        case2 = dynamic(x // 2)
    case3 = dynamic(x - 1)
    dp[x] = min(case1, case2, case3) + 1
    return dp[x]

print(dynamic(x))