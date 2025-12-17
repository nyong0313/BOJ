import sys
input = sys.stdin.readline
from collections import deque

v = int(input())
tree = [[] for _ in range(v+1)]
visited = [False] * (v+1)
distance = [0] * (v+1)
myqueue = deque()

for _ in range(v):
    temp = list(map(int, input().split()))
    cnt = 1
    while temp[cnt] != -1:
        tree[temp[0]].append((temp[cnt], temp[cnt+1]))
        cnt += 2

# for i in range(1, v+1):
#     for j in tree[i]:
#         print(j, end=" ")
#     print("")

def BFS(v):
    visited[v] = True
    myqueue.append((v, 0))
    while myqueue:
        temp = myqueue.popleft()
        distance[temp[0]] += temp[1]
        for i in tree[temp[0]]:
            if not visited[i[0]]:
                visited[i[0]] = True
                # pop할때 이전것까지 다 더해서 거리 저장하고 싶은데 잘안됨
                distance[i[0]] += distance[temp[0]]
                myqueue.append((i[0], i[1]))

BFS(1)
max_index = distance.index(max(distance))

visited = [False] * (v+1)
distance = [0] * (v+1)
myqueue = deque()
BFS(max_index)

print(max(distance))