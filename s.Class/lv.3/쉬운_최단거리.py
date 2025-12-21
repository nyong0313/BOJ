# 14940
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

def find():
    for i in range(n):
        for j in range(m):
            if a[i][j] == 2:
                return (i, j)

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 배열 생성 시 행, 열 구분
visited = [[False for _ in range(m)]for __ in range(n)]
ans = [[0 for _ in range(m)]for __ in range(n)]
dq = deque()
r, c = find()

dq.append((r, c, 0))
visited[r][c] = True

while len(dq) > 0:
    now = dq.popleft()
    for i in range(4):
        next = (now[0] + dx[i], now[1] + dy[i], now[2]+1)
        if 0 <= next[0] < n and 0 <= next[1] < m and a[next[0]][next[1]] != 0 and not visited[next[0]][next[1]]:
            dq.append(next)
            visited[next[0]][next[1]] = True
            ans[next[0]][next[1]] = next[2]

for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and not visited[i][j]:
            ans[i][j] = -1

for i in range(n):
    for j in range(m):
        print(ans[i][j], end=" ")
    print()