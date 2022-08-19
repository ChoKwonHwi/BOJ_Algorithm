import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n) :
    arr.append(sys.stdin.readline().strip())
set_list = set(arr)
arr = list(set_list)
arr.sort()
arr.sort(key = len)

for j in range(len(arr)) :
    print(arr[j])
