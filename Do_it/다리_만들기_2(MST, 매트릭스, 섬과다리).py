# 백준 17472
# 최소 신장 트리(Minimum Spanning Tree) -> 엣지리스트, 유니온파인드
import sys, heapq
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [[]for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    matrix[i] = list(map(int, input().split()))

sNum = 1
mList = []
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(i, j):
    myQueue = deque()
    mList.clear()
    myQueue.append((i, j))
    mList.append((i, j))
    visited[i][j] = True
    #
    matrix[i][j] = sNum
    while myQueue:
        nowX, nowY = myQueue.popleft()
        for k in range(4):
            x = nowX + dx[k]
            y = nowY + dy[k]
            while x >= 0 and x < n and y >= 0 and y < m:
                if matrix[x][y] != 0 and not visited[x][y]:
                    myQueue.append((x, y))
                    mList.append((x, y))
                    visited[x][y] = True
                    matrix[x][y] = sNum
                else:
                    break

                if dx[k] < 0:
                    x -= 1
                elif dx[k] > 0:
                    x += 1
                elif dy[k] < 0:
                    y -= 1
                elif dy[k] > 0:
                    y += 1
    return mList

sumList = []
for i in range(n):
    for j in range(m):
        # 매트릭스에 섬 마다 번호 붙여줄꺼임 -> != 0 으로 해야됨
        if matrix[i][j] != 0 and not visited[i][j]:
            tempList = list(BFS(i, j))
            sumList.append(tempList)
            sNum += 1

myHeapq = []

for landList in sumList:
    for nowLand in landList:
        nowX = nowLand[0]
        nowY = nowLand[1]
        nowSNum = matrix[nowX][nowY]
        for k in range(4):
            x = nowX + dx[k]
            y = nowY + dy[k]
            bridgeLen = 0
            while x >= 0 and x < n and y >= 0 and y < m:
                # 같은 섬일 경우
                if matrix[x][y] == nowSNum:
                    break
                # 다른 섬일 경우
                elif matrix[x][y] != 0:
                    if bridgeLen > 1: # 다리 길이 2이상 (문제조건)
                        heapq.heappush(myHeapq, (bridgeLen, nowSNum, matrix[x][y])) # 엣지 리스트 추가 (가중치, 시작, 끝)
                    break
                # 바다 일 경우
                else:
                    bridgeLen += 1
                
                if dx[k] < 0:
                    x -= 1
                elif dx[k] > 0:
                    x += 1
                elif dy[k] < 0:
                    y -= 1
                elif dy[k] > 0:
                    y += 1

def Find(a):
    if a == parant[a]:
        return a
    else:
        parant[a] = Find(parant[a])
        return parant[a]

def Union(a, b):
    a_parant = Find(a)
    b_parant = Find(b)
    parant[b_parant] = a_parant

parant = [i for i in range(sNum)] # 마지막에 1더해졌음

ans = 0
cnt = 0
while myHeapq:
    weight, start, end = heapq.heappop(myHeapq)
    if Find(start) != Find(end):
        Union(start, end)
        ans += weight
        cnt += 1

if cnt == sNum-2:
    print(ans)
else:
    print(-1)
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=" ")
#     print()