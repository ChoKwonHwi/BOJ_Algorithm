k = int(input())
for _ in range(k) :
    x = []
    ps = input()
    for i in ps :
        if i == '(' :
            x.append(i)
        elif i == ')' :
            if x :
                x.pop()
            else :
                print("NO")
                break  
    else :
        if len(x) == 0 :
            print("YES")
        else :
            print("NO")