# [백준 12865번 평범한 배낭] [백준 2758번 로또]  [백준 1106번 호텔]
import sys
input = sys.stdin.readline
t = int(input())
dp = [[0 for _ in range(2001)]for __ in range(11)]

for i in range(1, 2001):
    dp[1][i] = i

for i in range(2, 11):
    for j in range(1, 2001):
        dp[i][j] = dp[i-1][j//2] + dp[i][j-1]

for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])