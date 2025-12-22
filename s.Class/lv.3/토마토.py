# 7569
import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
myList = [[[0 for _ in range(m)]for __ in range(n)]for ___ in range(h)]
dq = deque()

for k in range(h):
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(m):
            myList[k][i][j] = temp[j]
            if temp[j] == 1:
                dq.append((k, i, j, 0))

# 우, 하, 좌, 상, 위, 아래
dz = [0, 0, 0, 0, 1, -1]
dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]

ans = 0
while len(dq) > 0:
    now = dq.popleft()
    for i in range(6):
        next = (now[0]+dz[i], now[1]+dx[i], now[2]+dy[i], now[3]+1)
        if 0<=next[0]<h and 0<=next[1]<n and 0<=next[2]<m and myList[next[0]][next[1]][next[2]]==0:
            myList[next[0]][next[1]][next[2]] = 1
            dq.append(next)
            ans = max(ans, next[3])

isEnd = True
for k in range(h):
    for i in range(n):
        for j in range(m):
            if isEnd and myList[k][i][j] == 0:
                isEnd = False
                print(-1)
            
if isEnd:
    print(ans)