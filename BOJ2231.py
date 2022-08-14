n = int(input())

for i in range(1, n+1) :
    result = i+sum(list(map(int, str(i))))
    if result == n :
        print(i)
        break
else :
    print(0)
