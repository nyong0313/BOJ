# 2차원 배열 점화식 DP
import sys
input = sys.stdin.readline
a = list(input().strip())
b = list(input().strip())
a.insert(0, 0), b.insert(0, 0)
dp = [[0 for _ in range(len(b))]for __ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            continue
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(a)-1][len(b)-1])