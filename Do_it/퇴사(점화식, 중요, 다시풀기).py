# 14501
# 점화식 세우기.. 어려움 1_로_만들기(84/1463)와 같이 감 못잡고 답을 봤음
# D[i] : i번째 날부터 퇴사일까지의 최대 수입
# D[i] = max(D[i+T[i]] + P[i], D[i+1])
# D[] = 0으로 초기화
n = int(input())
T = [0]*(n+1)
P = [0]*(n+1)
D = [0]*(n+1)
for i in range(n):
    a, b = map(int, input().split())
    T[i] = a
    P[i] = b

for i in range(n-1, -1, -1):
    if i + T[i] > n:
        D[i] = D[i+1]
    else:
        D[i] = max(D[i+1], D[i + T[i]] + P[i])

print(D[0])