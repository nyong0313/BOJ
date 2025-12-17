# 11438
# LCA : 최소 공통 조상노드 구하기(트리)
# 점화식 이용 (노드 100,000개) P[K][N] = P[K-1][P[K-1][N]]
# 책에 나온 k는 트리 높이임.
# 반복문 종료 후 다른 노드라면 바로 위 부모가 LCA이다.
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
myList = [[]for _ in range(n+1)]
parant = [0]*(n+1)
depth = [0]*(n+1)

treeHeight = 0
while 2 ** treeHeight <= n:
    treeHeight += 1

parant = [[0 for _ in range(n+1)]for _ in range(treeHeight+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    # 입력값이 항상 부모 자식 순서가 아님.
    myList[a].append(b)
    myList[b].append(a)

# BFS로 parant, depth 배열 입력
visited = [False]*(n+1)
myQueue = deque()
myQueue.append((1, 0))
while myQueue:
    node, d = myQueue.popleft()
    visited[node] = True
    d += 1
    for i in myList[node]:
        if not visited[i]:
            depth[i] = d
            parant[0][i] = node
            myQueue.append((i, d))

for i in range(1, treeHeight+1):
    kmax = 2 ** i
    for j in range(n, 0, -1):
        parant[i][j] = parant[i-1][parant[i-1][j]]

def LCA(a, b):
    # b가 더 깊은 노드로 설정
    if depth[a] > depth[b]:
        temp = a
        a = b
        b = temp

    # 같은 높이로 맞추기
    for i in range(treeHeight, -1, -1):
        if 2 ** i <= depth[b] - depth[a]:
            # if depth[a] <= depth[parant[i][b]]:
                b = parant[i][b]
        # if depth[a] == depth[b]:
        #     break
        

    # 조상 찾기 -> 최초로 다른거 찾고 -> 그 후로 조금씩 올라가서 같은거 찾기
    for i in range(treeHeight, -1, -1):
        if a == b:
            break
        if parant[i][a] != parant[i][b]:
            a = parant[i][a]
            b = parant[i][b]

    if a != b:
        a = parant[0][a]

    return a

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(LCA(a, b))