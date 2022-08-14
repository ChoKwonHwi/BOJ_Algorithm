n = int(input())

count = 0

for i in range(n) :
    s = input()
    ss = [' ']
    if len(s) == 1 :
        count += 1
        continue
    else :
        for j in range(0, len(s)-1) :
            if s[j] in ss or s[j+1] in ss:
                break
            if s[j] != s[j+1] :
                ss.append(s[j])
            if j == len(s)-2 :
                count += 1
print(count)
