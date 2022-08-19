n, k = map(int, input().split())
result = 1
x = 1
if k ==0 :
    print(1)
else :
    for i in range(n, n-k, -1) :
        result *= i
    for j in range(1, k+1) :
        x *= j
    print("{:.0f}".format(result/j%1000000007))
