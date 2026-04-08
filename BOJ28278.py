import sys

n = int(sys.stdin.readline())
st = []

for _ in range(n) :
    cmd = sys.stdin.readline().split()
    if cmd[0] == '1' :
        st.append(int(cmd[-1]))
    elif cmd[0] == '2' :
        if len(st) == 0 :
            print("-1")
        else :
            print(st.pop(-1))
    elif cmd[0] == '3' :
        print(len(st))
    elif cmd[0] == '4' :
        if len(st) == 0 :
            print(1)
        else :
            print(0)
    elif cmd[0] == '5' :
        if len(st) == 0 :
            print("-1")
        else :
            print(st[-1])