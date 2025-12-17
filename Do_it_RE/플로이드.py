# ch08 - 61/11404
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
myList = [[]for _ in range(n+1)]
d = [[sys.maxsize for _ in range(n+1)]for __ in range(n+1)]

for i in range(1, n+1):
    d[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    # 중복된 노선 중 최솟값 선택
    if d[a][b] > c: 
        d[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if d[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(d[i][j], end=" ")
    print()