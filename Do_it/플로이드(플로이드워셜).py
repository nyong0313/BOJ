# 11404
# 플로이드워셜 -> 시간복잡도 N^3이기 때문에 N이 100, 200개 일때만 가능.
# 핵심 이론 : 최단경로의 부분 경로도 모두 최단경로이다.
# -> 이중 배열 리스트 [start][end], 3중 for문 k, s, e *** 암기
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
distance = [[sys.maxsize] * (n+1) for _ in range(n+1)]
# distance = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    distance[i][i] = 0 # 자기자신 (대각선)

for i in range(m):
    a, b, c = map(int, input().split())
    # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다. ***
    if distance[a][b] > c: 
        distance[a][b] = c

for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            distance[s][e] = min(distance[s][e], distance[s][k] + distance[k][e])

for s in range(1, n+1):
    for e in range(1, n+1):
        if distance[s][e] == sys.maxsize:
            print(0, end=" ")
        else:
            print(distance[s][e], end=" ")
    print()