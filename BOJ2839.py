n = int(input())

five = n//5
ans = 1001

for i in range(five, -1, -1) :
    if (n-i*5)%3 == 0 :
        ans = i+(n-i*5)//3
        break
    if i == 0 :
        ans = -1

print(ans)
