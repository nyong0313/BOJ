#11689
# GCD : 최대공약수
# 오일러 피 함수 = N - (N / 소인수)
import sys, math
input = sys.stdin.readline        

n = int(input())
result = n

# 그냥 n까지 반복 시, 시간 초과.
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        result = result - result // i
        while n % i == 0:
            n = n // i

# 루트 n 범위로 인해, 마지막 소인수 계산 안되는 경우.
if n > 1:
    result = result - result // n

print(result)

# out of Memory
# p = [i for i in range(n + 1)]

# for i in range(2, n + 1):
#     if p[i] == i: # 현재 리스트의 값과 인덱스가 같으면 (= 소수일 때)
#         for j in range(i, n + 1, i):
#             p[j] = p[j] - p[j] // i

# print(p[n])