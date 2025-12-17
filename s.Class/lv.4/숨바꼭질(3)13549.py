import sys
from collections import deque
input = sys.stdin.readline
ans = [-1]*100001
myDeque = deque()
n, k = map(int, input().split())

def bfs(v):
    ans[v] = 0
    myDeque.append(v)
    while myDeque:
        x = myDeque.popleft()
        if x == k:
            return

        # 순서 바뀌면 틀림
        for next in (x * 2, x-1, x+1):
            if 0 <= next <= 100000 and ans[next] == -1: # 처음 방문한 곳만
                if next == x * 2:
                    ans[next] = ans[x]
                    myDeque.appendleft(next)
                else:
                    ans[next] = ans[x] + 1
                    myDeque.append(next)
            
bfs(n)
print(ans[k])