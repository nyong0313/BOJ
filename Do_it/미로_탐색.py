#2178
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[0] * (m) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]
myqueue = deque()

dx = [0, 1, 0 ,-1]
dy = [1, 0, -1, 0]

for i in range(n):
    # mylist = list(map(int, input().strip()))
    mylist = list(input())
    for j in range(m):
        matrix[i][j] = int(mylist[j])

def BFS(i, j):
    myqueue.append((i, j))
    visited[i][j] = True
    while myqueue:
        temp = myqueue.popleft()
        for k in range(4):
            x = temp[0] + dx[k]
            y = temp[1] + dy[k]

            if x>=0 and y>=0 and x<n and y<m:
                if matrix[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    matrix[x][y] = matrix[temp[0]][temp[1]] + 1
                    myqueue.append((x, y))

def bfs(i, j):
    visited[i][j] = True
    myqueue.append((i, j))
    while myqueue:
        temp = myqueue.popleft()
        for i in range(4):
            x = temp[0] + dx[i]
            y = temp[1] + dy[i]
            if x>=0 and y>=0 and x<n and y<m:
                if matrix[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    myqueue.append((x, y))
                    matrix[x][y] = matrix[temp[0]][temp[1]] + 1


# BFS(0,0)
bfs(0,0)
print(matrix[n-1][m-1])