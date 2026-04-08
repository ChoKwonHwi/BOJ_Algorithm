N, M = map(int, input().split())
card = list(map(int, input().split()))
minsum = 0
for x in range(0, N) :
    for y in range(x+1, N) :
        for z in range(y+1, N) :
            if M < (card[x] + card[y] + card[z]) :
                continue
            else :
                minsum = max(minsum, card[x] + card[y] + card[z])
print(minsum)