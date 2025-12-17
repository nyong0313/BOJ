# dp[n][w] = 1 ~ n까지 n개의 물건이 있고, 가방의 최대용량이 w일 때 담을 수 있는 최대 가치
# [백준 12865번 평범한 배낭] [백준 2758번 로또]  [백준 1106번 호텔]
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
myList = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    myList.append((w, v))

dp = [[0 for _ in range(k+1)]for __ in range(n+1)]

for i in range(1, n+1):
    for w in range(k+1):
        if myList[i][0] > w:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], myList[i][1] + dp[i-1][w - myList[i][0]])

print(max(dp[n]))