n = int(input())

count = 0

if n < 100 :
    print(n)
else :
    for i in range(100, n+1) :
        h = i // 100
        t = (i % 100) // 10
        o = i % 10
        if (h+o) == 2*t :
            count += 1
            
    print(count+99)
