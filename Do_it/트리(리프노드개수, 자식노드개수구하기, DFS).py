# 1068
# 자식 노드를 세는 방법.. 생각못해서 자식노드가 없는 경우만 생각했음. 처음엔 틀렸었음..
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n = int(input())
parant = list(map(int, input().split()))
delNode = int(input())
myList = [[]for _ in range(n)]
visited = [False]*n

for i in range(n):
    if parant[i] == -1:
        startNode = i
    else:
        myList[i].append(parant[i])
        myList[parant[i]].append(i)

def DFS(a):
    global ans
    visited[a] = True
    leafNum = 0 # 자식 노드 개수 세기 **
    for i in myList[a]:
        if not visited[i] and i != delNode:
            leafNum += 1
            DFS(i)
    if leafNum == 0:
        ans += 1
    
ans = 0
if startNode == delNode:
    print(0)
else:
    DFS(startNode)    
    print(ans)



# leafNode = [True]*(n)
# myQueue = deque()
# myQueue.append(startNode)
# leafNode[startNode] = False

# while myQueue:
#     node = myQueue.popleft()
#     for i in myList[node]:
#         if i == delNode:
#             break
#         leafNode[node] = False
#         myQueue.append(i)

# def delDFS(a):
#     leafNode[a] = False
#     for i in myList[a]:
#         delDFS(i)

# delDFS(delNode)

# count = 0
# for i in range(n):
#     if leafNode[i]:
#         count += 1

# print(count)