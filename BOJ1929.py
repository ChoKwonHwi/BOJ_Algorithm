import math

def check_num(x) :
    for i in range(2, int(math.sqrt(x))+1) :
        if x%i == 0 :
            return False
    return True

m, n = map(int, input().split())


for i in range(m, n+1) :
    if check_num(i) :
        print(i)
