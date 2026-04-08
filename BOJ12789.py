n = int(input())

line = list(map(int, input().split()))
st = [10000]
number = 1

while(line) :
    if line[0] == number :
        del line[0]
        number+=1
    elif st[-1] == number :
        number += 1
        st.pop()
    else :
        st.append(line[0])
        del line[0]

del st[0]

while(st) :
    if st[-1] == number :
        number+=1
        st.pop()
    else :
        break

if len(line) == 0 and len(st) == 0:
    print("Nice")
else :
    print("Sad")

        
            