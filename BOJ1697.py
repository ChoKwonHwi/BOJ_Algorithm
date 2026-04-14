from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def bfs(n, k) :
    if n == k :
        print(0)
        return
    
    visited = [False] * 100001
    queue = deque()
    queue.append((n, 0))
    visited[n] = True
    
    while queue :
        now, now_cnt = queue.popleft()
        
        plus, minus, mult = now+1, now-1, now*2
        
        for nxt in (plus, minus, mult) :
            if 0 <= nxt <= 100000 and not visited[nxt] :
                if nxt == k :
                    print(now_cnt+1)
                    return
                visited[nxt] = True
                queue.append((nxt, now_cnt+1))

bfs(n, k)