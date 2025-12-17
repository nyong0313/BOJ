# dp[n][3] = n번째까지 최소 비용. 이때, 빨, 초, 파 각각 다 구한다.
# dp[n][3] = min(dp[n-1][0], dp[n-1][1]) + a[n][3]
import sys
input = sys.stdin.readline
n = int(input())
a = [[]for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

dp = [[0 for _ in range(3)]for __ in range(n)]
dp[0] = a[0]

for i in range(1, n):
    for j in range(3):
        dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + a[i][j]

print(min(dp[-1]))