# 1219 / 세일즈맨의 고민
# 벨만포드
# 가지고 있는 돈의 액수를 최대
import sys
input = sys.stdin.readline
n, startCity, endCity, m = map(int, input().split())
edges = []
MIN_SIZE = -1 * sys.maxsize
distance = [MIN_SIZE] * n

for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

money = list(map(int, input().split()))

distance[startCity] = money[startCity]

for i in range(n-1):
    for s, e, w in edges:
        if distance[s] != MIN_SIZE and distance[e] < distance[s] - w + money[e]:
            distance[e] = distance[s] - w + money[e]

# pCycle = False -> 이걸로 체크하니까 목표 노드까지 못가는데 다른 노드들에서 양수 사이클 발생하는 경우를 처리 못함.
# n-1에서 n+1 바꿔주니 통과 ..
for i in range(n+1):
    for s, e, w in edges:
        if distance[s] != MIN_SIZE and distance[e] < distance[s] - w + money[e]:
            distance[e] = sys.maxsize
        elif distance[s] == sys.maxsize:
            distance[s] = sys.maxsize

if distance[endCity] == MIN_SIZE:
    print("gg")
elif distance[endCity] == sys.maxsize:
    print("Gee")
else:
    print(distance[endCity])