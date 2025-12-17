# 2098
# TSP (Traveling Salesman Problem)
# DP[C][V] : 현재도시 C, 방문한 도시 V (비트마스킹으로 방문한 모든 도시 표현)
# DP[C][V] = min(DP[C][V], DP[i][V | (1 << i)])  -> V OR (0001 << i)
import sys
input = sys.stdin.readline
n = int(input())
w = [[0 for _ in range(n)]for __ in range(n)]

for i in range(n):
    w[i] = list(map(int, input().split()))

dp = [[0 for _ in range(1 << n)] for __ in range(n)]

def TSP(c, v):
    if v == ((1 << n) - 1):
        if w[c][0] == 0: #시작도시(0)로 갈 수 없을 때
            return sys.maxsize
        else:
            return w[c][0]
    if dp[c][v] != 0:
        return dp[c][v]
    
    result = sys.maxsize
    for i in range(0, n):
        if (v & (1 << i)) == 0 and w[c][i] != 0:
            result = min(result, TSP(i, v | (1 << i)) + w[c][i])
    dp[c][v] = result
    return dp[c][v]

# 도시를 순회하는 것이기 때문에 어떤 도시에서 시작해도 상관없다.
print(TSP(0, 1))