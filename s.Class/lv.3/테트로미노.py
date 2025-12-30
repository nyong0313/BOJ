# 14500
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
myList = []

for _ in range(n):
    myList.append(list(map(int, input().split())))

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False for _ in range(m)]for __ in range(n)]
max_cell = max(map(max, myList))

def dfs(x, y, depth, total):
    global ans

    # 가지치기: 남은 칸을 전부 max로 더해도 ans 못 넘으면 컷
    if total + (3 - depth) * max_cell <= ans:
        return

    if depth == 3:
        ans = max(ans, total)
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:

            if depth == 1:
                visited[nx][ny] = True
                dfs(x, y, depth + 1, total + myList[nx][ny])
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + myList[nx][ny])
            visited[nx][ny] = False

ans = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 0, myList[i][j])
        visited[i][j] = False

print(ans)