import sys

k = int(sys.stdin.readline())
st = []

for _ in range(k) :
    x = int(sys.stdin.readline())
    if x == 0 :
        st.pop()
    else :
        st.append(x)
print(sum(st))