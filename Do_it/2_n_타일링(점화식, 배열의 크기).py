# 11726
# D[i] : i크기일때, 경우의 수
# n이 1일 때는 D[2] = 2를 할 수가 없겠죠.
n = int(input())
D = [0]*(n+2)
D[1] = 1
D[2] = 2

for i in range(3, n+1):
    D[i] = (D[i-1] + D[i-2]) % 10007
print(D[n])