# 1516
# N개 건물
# i번째 건물 짓는 시간 | 먼저 지어져야 하는 건물 | -1
# 틀린거 1. 건물짓는 시간 리스트랑 정답 리스트(건물짓기 시작하는 시간) 구별해야되는것. 
# (+ 마지막에 자신 건물 짓는 시간 더하기)
# 2. 건물짓기 시작하는 시간 리스트 결정할때, 
# 지어야 하는 건물의 (다른 이전 건물로 결정된 기존 시작 시간)과 (이전 건물 시작 시간 + 현재 건물 짓는 시간) 중 최댓값을 선택한다.
# 즉, 이전에 지어야하는 건물이 2개 이상일때 제일 많이 걸리는 것을 선택하는 것이다.
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
# 건물 짓는데 걸리는 시간
times = [0] * (n+1)
indegree = [0] * (n+1)
mylist = [[]for _ in range(n+1)]
for i in range(1, n+1):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if j == 0:
            times[i] = temp[j]

        elif temp[j] < 0 :
            break

        else:
            indegree[i] += 1
            mylist[temp[j]].append(i)

myqueue = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        myqueue.append(i)

# 건물 짓기 시작하는 타임
ans = [0] * (n+1)

while myqueue:
    node = myqueue.popleft()
    # ans[node] += times[node] 이거 있으면 안됨 ! 마지막에 더해야 중복 X
    for i in mylist[node]:
        indegree[i] -= 1
        # 두 시간 중 더 큰거 골라야 하는 이유
        # -> times      = [0, 5, 2, 4]
        #    ans        = [0, 0, 0, 0]
        #    indegree   = [0, 0, 0, 2]
        #    mylist     = [[], [3], [3], []]
        ans[i] = max(ans[i], ans[node] + times[node])
        if indegree[i] == 0:
            myqueue.append(i)


for i in range(1, len(ans)):
    ans[i] += times[i]
    print(ans[i])