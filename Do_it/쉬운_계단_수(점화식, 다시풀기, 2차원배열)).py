# 10844
# 아이디어를 먼저 봐서 쉽게 푼 듯.
# 문제 설명이 좀 이상. 계단은 0~9 이다. 다만 시작이 0이 안됨.
n = int(input())
D = [[0 for _ in range(10)]for _ in range(n+1)]

for i in range(1, 10):
    D[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            D[i][j] = D[i-1][j+1] % 1000000000
        elif j == 9:
            D[i][j] = D[i-1][j-1] % 1000000000
        else:
            D[i][j] = (D[i-1][j+1] + D[i-1][j-1]) % 1000000000

print(sum(D[n]) % 1000000000)