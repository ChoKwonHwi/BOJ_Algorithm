from collections import deque
import sys

input = sys.stdin.readline

a, b = map(int, input().split())

def bfs(a, b) :
    queue = deque()
    queue.append((a, 1))
    
    while queue :
        now, now_cnt = queue.popleft()
        one, two = now*10+1, now*2
        now_cnt += 1
        if one == b or two == b :
            print(now_cnt)
            exit()
        if one <= b :
            queue.append((one, now_cnt))
        if two <= b :
            queue.append((two, now_cnt))
    print(-1)
    
bfs(a, b)