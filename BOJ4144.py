count = 0
c = int(input())
for _ in range(c) :
    num = list(map(int, input().split()))
    average = sum(num[1:])/num[0]
    for i in (num[1:]) :
        if i > average :
            count += 1
    print(f'{count/num[0]*100:.3f}%')
    count = 0
