# 11051
# 나머지 연산은 각각의 모듈러의 합과 합의 모듈러가 동일.
# nCk = n-1Ck + n-1Ck-1 -> D[i][j] = D[i-1][j] + D[i-1][j-1]
# iC0 = 1 -> D[i][0] = 1 (i개 중 아무것도 선택하지 않는 경우의 수는 1)
# iC1 = i -> D[i][1] = i (i개 중 하나를 선택하는 경우의 수는 i)
# iCi = 1 -> D[i][i] = 1 (i개 중 i개를 선택하는 경우의 수는 1)
# D[3~n][i~i-1]
n, k = map(int, input().split())
D = [[0 for _ in range(n+1)]for _ in range(n+1)]

for i in range(n+1):
    D[i][0] = 1
    D[i][1] = i
    D[i][i] = 1

for i in range(3, n+1):
    for j in range(2, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]
        D[n][k] = D[n][k] % 10007

print(D[n][k])