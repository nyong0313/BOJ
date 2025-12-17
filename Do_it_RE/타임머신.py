# ch08 - 59/11657
# 벨만포드 : 이론과 실제 코드 동작 방식이 조금 다름.
# 이론 : 엣지 최대 사용 개수별 최단거리
# 코드 : 출발노드 방문했으면 계속 반복
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
myList = []

for _ in range(m):
    a, b, c = map(int, input().split())
    myList.append((a, b, c))

d = [sys.maxsize]*(n+1)
d[1] = 0

for _ in range(n-1):
    for start, end, weight in myList:
        if d[start] != sys.maxsize and d[end] > d[start] + weight:
            d[end] = d[start] + weight

mCycle = False
for start, end, weight in myList:
        if d[start] != sys.maxsize and d[end] > d[start] + weight:
             mCycle = True

if mCycle:
    print(-1)
else:
    for i in range(2, n+1):
        if d[i] == sys.maxsize:
            print(-1)
        else:
            print(d[i])