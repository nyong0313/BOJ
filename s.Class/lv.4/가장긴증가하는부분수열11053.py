# D[i] = A[i]보다 작은 값(0~i-1) 중 최대 길이에 + 1
# O(N^2) -> lv.5 12015번 O(nlogn)
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [0]*n
dp[0] = 1

for i in range(1, n):
    result = 0

    for j in range(i):
        if a[i] > a[j]:
            result = max(result, dp[j])
    
    dp[i] = result + 1

print(max(dp))