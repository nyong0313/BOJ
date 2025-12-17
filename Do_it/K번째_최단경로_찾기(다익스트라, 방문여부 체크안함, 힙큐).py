# 1854
# HeapQueue로 다익스트라 구현
# HeapQueue : 그냥 리스트 만들고, heapq.heappush("리스트", "값") 하면 값이 리스트에 정렬되어 삽입됨.
# 각 도시당 거리의 최댓값을 k개 만들어 놓고 각 경우의 수를 삽입 후 정렬.
# + 특이점 : 방문 여부 체크 안함 !!
import sys, heapq
input = sys.stdin.readline
n, m, k = map(int, input().split())
mylist = [[]for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    mylist[a].append((b, c))

# ***
ans = [[sys.maxsize] * k for _ in range(n+1)]

# (0, 1)인 튜플 리스트 선언
myhq = [(0, 1)]
ans[1][0] = 0

while myhq:
    nowDistance, nowNode = heapq.heappop(myhq)
    for nextNode, nextDistance in mylist[nowNode]:
        d = nowDistance + nextDistance
        if ans[nextNode][k-1] > d:
            ans[nextNode][k-1] = d
            ans[nextNode].sort()
            heapq.heappush(myhq, (d, nextNode))

for i in range(1, n+1):
    if ans[i][k-1] < sys.maxsize:
        print(ans[i][k-1])
    else:
        print(-1)



# from queue import PriorityQueue
# myqueue = PriorityQueue()
# myqueue.put((0, 1))
# ans[1].append(0)

# while not myqueue.empty():
#     temp = myqueue.get()
#     nodeDistance = temp[0]
#     node = temp[1]
#     # if visited[node]:
#     #     continue
#     visited[node] = True
#     for i in mylist[node]:
#         nextNode = i[0]
#         nextDistance = i[1]
#         if not visited[nextNode]:
#             d = nodeDistance + nextDistance
#             ans[nextNode].append(d)
#             # visited[nextNode] = True
#             myqueue.put((d, nextNode))

# for i in range(1, n+1):
#     ans[i].sort()
#     if len(ans[i]) >= k:
#         print(ans[i][k-1])
#     else:
#         print(-1)