# 11403
# N (1 ≤ N ≤ 100), 그래프 + 인접행열 (, 최단거리..?) -> 플로이드워셜
# 사이클로 자기자신 올때만 가능
import sys
input = sys.stdin.readline
n = int(input())
distance = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    distance[i] = list(map(int, input().split()))

for k in range(n):
    for s in range(n):
        for e in range(n):
            if distance[s][k] == 1 and distance[k][e] == 1:
                distance[s][e] = 1

for s in range(n):
    for e in range(n):
        print(distance[s][e], end=" ")
    print()