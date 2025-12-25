# 10026
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
myList = []

for _ in range(n):
    myList.append(list(input().strip()))

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def first_bfs():
    visited = [[False for _ in range(n)]for __ in range(n)]
    dq = deque()
    cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                key = myList[i][j]
                visited[i][j] = True
                dq.append((i, j))
                cnt += 1

            while len(dq) > 0:
                now = dq.popleft()
                for t in range(4):
                    next = (now[0]+dx[t], now[1]+dy[t])
                    if 0<=next[0]<n and 0<=next[1]<n and myList[next[0]][next[1]] == key and not visited[next[0]][next[1]]:
                        dq.append(next)
                        visited[next[0]][next[1]] = True
    return cnt

def second_bfs():
    visited = [[False for _ in range(n)]for __ in range(n)]
    dq = deque()
    cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if myList[i][j] == 'B':
                    isColored = False
                else:
                    isColored = True
                visited[i][j] = True
                dq.append((i, j))
                cnt += 1

            while len(dq) > 0:
                now = dq.popleft()
                for t in range(4):
                    next = (now[0]+dx[t], now[1]+dy[t])
                    if 0<=next[0]<n and 0<=next[1]<n and not visited[next[0]][next[1]]:
                        if isColored and myList[next[0]][next[1]] == 'B':
                            continue
                        if not isColored and myList[next[0]][next[1]] != 'B':
                            continue
                        dq.append(next)
                        visited[next[0]][next[1]] = True
    return cnt

print(first_bfs(), second_bfs())