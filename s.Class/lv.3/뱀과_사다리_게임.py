# 16928
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
ladder_dict = {}
snake_dict = {}

for _ in range(n):
    x, y = map(int, input().split())
    ladder_dict[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    snake_dict[x] = y

visited = [False]*101
dq = deque()
dq.append((1, 0))

while len(dq) > 0:
    now = dq.popleft()
    if now[0] == 100:
        print(now[1])
        break

    for i in range(1, 7):
        next = (now[0]+i, now[1]+1)
        if 0<next[0]<=100 and not visited[next[0]]:
            visited[next[0]] = True
            if next[0] in ladder_dict:
                next = (ladder_dict[next[0]], next[1])
                visited[next[0]] = True
            if next[0] in snake_dict:
                next = (snake_dict[next[0]], next[1])
                visited[next[0]] = True
            dq.append(next)