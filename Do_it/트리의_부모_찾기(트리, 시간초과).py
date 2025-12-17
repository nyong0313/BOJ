# 11725
# 깊이를 저장하고 비교해서 부모 노드를 저장했는데 시간초과 ?
# 정답은 visted와 DFS를 활용
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n = int(input())
myList = [[]for _ in range(n+1)]
parant = [0]*(n+1)
visited = [False]*(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    myList[a].append(b)    
    myList[b].append(a)    

def DFS(a):
    for i in myList[a]:
        if not visited[i]:
            visited[i] = True
            parant[i] = a
            DFS(i)

visited[1] = True
DFS(1)

for i in range(2, n+1):
    print(parant[i])



# depth = [sys.maxsize]*(n+1)
# depth[1] = 0
# myQueue = []

# for i in range(n-1):
#     a, b = map(int, input().split())
#     if depth[a] < depth[b]:
#         depth[b] = depth[a] + 1
#         parant[b] = a
#     elif depth[a] > depth[b]:
#         depth[a] = depth[b] + 1
#         parant[a] = b
#     else:
#         myQueue.append((a, b))

# while myQueue:
#     a, b = myQueue.pop()
#     if depth[a] < depth[b]:
#         depth[b] = depth[a] + 1
#         parant[b] = a
#     elif depth[a] > depth[b]:
#         depth[a] = depth[b] + 1
#         parant[a] = b
#     else:
#         myQueue.append((a, b))

# for i in range(2, n+1):
#     print(parant[i])