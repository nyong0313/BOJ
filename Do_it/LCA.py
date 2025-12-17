# 11437
# LCA : 최소 공통 조상노드 구하기(트리)
# 점화식 말고 일반적인 방법 이용 (노드 50,000개 이하)
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
myList = [[]for _ in range(n+1)]
parant = [0]*(n+1)
depth = [0]*(n+1)

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
            parant[i] = node
            myQueue.append((i, d))

def LCA(a, b):
    while a != b:
        if depth[a] < depth[b]:
            b = parant[b]
        elif depth[a] > depth[b]:
            a = parant[a]
        else:
            a = parant[a]
            b = parant[b]
    return a

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(LCA(a, b))