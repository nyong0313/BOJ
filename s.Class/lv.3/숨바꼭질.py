# 1697
# BFS로 풀어야 하는 이유
# 1. 모든 이동의 비용이 같다.
# 2. 최소 횟수를 구한다.
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())

# 메모리 관리를 위한 visited
visited = [False]*100001
dq = deque()
dq.append((n, 0))
visited[n] = True

while len(dq) > 0:
    now = dq.popleft()
    if now[0] == k:
        print(now[1])
        break

    for x in (now[0]-1, now[0]+1, 2*now[0]):    
        if 0 <= x <= 100000 and not visited[x]:
            visited[x] = True
            dq.append((x, now[1]+1))