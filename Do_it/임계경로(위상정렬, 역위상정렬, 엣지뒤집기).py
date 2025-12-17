# 1948
# 모든 도로가 일방통행인 도로이고, 싸이클이 없다 = 방향 O, 사이클 X -> 위상정렬
# 임계 경로 값(= 가장 높은 시간)은 일반적인 위상정렬 이용.
# 해당 임계 경로의 도로 수를 구하기 위해 역방향 위상정렬 이용.
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
mylist = [[]for _ in range(n+1)]
indegree = [0] * (n+1)
reversed_mylist = [[]for _ in range(n+1)]
# reversed_indegree = [0] * (n+1)
criticalPath = [0] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    mylist[a].append((b, c))
    indegree[b] += 1
    reversed_mylist[b].append((a, c))

startNode, endNode = map(int, input().split())

# 위상정렬
myqueue = deque()
myqueue.append(startNode)

while myqueue:
    node = myqueue.popleft()
    for i in mylist[node]:
        nextNode = i[0]
        nextTime = i[1]
        indegree[nextNode] -= 1
        # 전 문제와 동일 및 중요 포인트
        criticalPath[nextNode] = max(criticalPath[nextNode], criticalPath[node] + nextTime)
        if nextNode != endNode and indegree[nextNode] == 0:
            myqueue.append(nextNode)

# 역 위상정렬
count = 0
myqueue.clear()
myqueue.append(endNode)
visited = [False] * (n+1)
visited[endNode] = True
# 방문 여부 확인이 필요한 이유
# ex)
# 경로 1: 0 → A(1) → B(2) → 4
# 경로 2: 0 → C(3) → B(2) → 4

while myqueue:
    node = myqueue.popleft()
    for i in reversed_mylist[node]:
        nextNode = i[0]
        nextTime = i[1]
        # ***
        if criticalPath[node] == criticalPath[nextNode] + nextTime:
            # 임계 값이 같지만 경로가 여러개 일 수 있기 때문에 다 카운트 해야됨
            count += 1
            if not visited[nextNode]:
                visited[nextNode] = True
                myqueue.append(nextNode)

print(max(criticalPath))
print(count)