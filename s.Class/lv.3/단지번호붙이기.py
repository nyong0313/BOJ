# 2667
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
a = []

for _ in range(n):
    a.append(list(map(int, input().strip())))

visited = [[False for _ in range(n)]for __ in range(n)]
# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(i, j):
    cnt = 1
    visited[i][j] = True
    dq = deque([(i, j)])

    while len(dq) > 0:
        nowX, nowY = dq.popleft()
        for k in range(4):
            x = nowX + dx[k]
            y = nowY + dy[k]
            if 0 <= x < n and 0 <= y < n and a[x][y] == 1 and not visited[x][y]:
                cnt += 1
                visited[x][y] = True
                dq.append((x, y))
    return cnt

ans = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and not visited[i][j]:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
for i in ans:
    print(i)