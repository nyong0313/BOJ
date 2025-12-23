# 7576
import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
myList = [[0 for _ in range(m)]for __ in range(n)]
dq = deque()

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        myList[i][j] = temp[j]
        if temp[j] == 1:
            dq.append((i, j, 0))

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = 0
while len(dq) > 0:
    now = dq.popleft()
    for i in range(4):
        next = (now[0]+dx[i], now[1]+dy[i], now[2]+1)
        if 0<=next[0]<n and 0<=next[1]<m and myList[next[0]][next[1]] == 0:
            dq.append(next)
            myList[next[0]][next[1]] = 1
            ans = max(ans, next[2])

isEnd = True
for i in range(n):
    for j in range(m):
        if isEnd and myList[i][j] == 0:
            print(-1)
            isEnd = False
if isEnd:
    print(ans)