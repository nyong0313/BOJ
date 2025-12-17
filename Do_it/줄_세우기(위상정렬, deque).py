# 2252
# 위상정렬 (topology sort)
# -> 방향성 O, 사이클 X -> 노드 순서 정하기
# 인접리스트는 만들어 놓고 pop은 안함.
# indegree 0될때만 deque에 삽입하기.
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
mylist = [[]for _ in range(n+1)]
indegree = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    mylist[a].append(b)
    indegree[b] += 1

myqueue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        myqueue.append(i)

while myqueue:
    a = myqueue.popleft()
    print(a, end=" ")
    for i in mylist[a]:
        indegree[i] -= 1
        if indegree[i] == 0:
            myqueue.append(i)



# 시간초과 ㅜ
# count = n
# while count > 0:
#     for i in range(1, n+1):
#         if indegree[i] == 0:
#             count -= 1
#             indegree[i] -= 1
#             print(i, end=" ")

#             while mylist[i]:
#                 b = mylist[i].pop()
#                 indegree[b] -= 1

#             break