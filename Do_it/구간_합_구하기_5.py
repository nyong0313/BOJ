import sys
input = sys.stdin.readline

n,m = map(int, input().split())

# 주의점 : 파이썬에서 배열은 0부터 시작하나, 문제에서 인덱스를 1~n까지로 설정했다. -> 배열을 [n+1][n+1]크기로 설정하여 각 행과 열의 [0]을 빈공간으로 설정한다.
# 따라서 첫행은 [0][]으로 빈공간 설정.
A = [[0] * (n + 1)]
for i in range(n):
    A_row = [0] + list(map(int, input().split())) #앞에 [0] + 해줘서 A[][0]을 빈공간으로 설정.
    A.append(A_row)

D = [[0] * (n + 1)]
for i in range(n):
    D_row = [0] * (n+1)
    D.append(D_row)

# for 두번써야되는거 맞음. 인덱스(range) 주의 **
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

# 마지막 식 틀림 실수 잦을 듯, 다시보기 **
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(D[x2][y2] - D[x1-1][y2] -D[x2][y1-1] + D[x1-1][y1-1])