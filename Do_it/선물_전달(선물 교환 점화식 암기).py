# 1947
# 선물 교환 점화식 **
# D[N] = (N-1) * (D[N-2] + D[N-1])
import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
    print(0)
else:
    D = [0]*(n+1)
    D[1] = 0
    D[2] = 1
    for i in range(3, n+1):
        D[i] = (i-1) * (D[i-2] + D[i-1]) % 1000000000

    print(D[n])