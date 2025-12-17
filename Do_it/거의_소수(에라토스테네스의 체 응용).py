# 1456
import math, sys
input = sys.stdin.readline

a, b = map(int, input().split())
# 문제에서 b는 최대 10^14
# 따라서 제곱근, 10^7까지 구함. (b로 하면 out of Memory)
LIMIT = 10000000
prime_number = [True] * (LIMIT + 1)
prime_number[0] = prime_number[1] = False

for i in range(2, int(math.sqrt(LIMIT))+1):
    if prime_number[i]:
        for j in range(i + i, LIMIT + 1, i):
            prime_number[j] = False

count = 0
# int(math.sqrt(LIMIT))로 하면 틀림 -> 이미 LIMIT을 제곱근으로 설정했기 때문에
# int(math.sqrt(b))은 가능
for i in range(2, LIMIT + 1):
    if prime_number[i]:
        temp = i * i
        while temp <= b:
            if temp >= a:
                count += 1
            # if temp > b // i:  # 오버플로우 방지 가능
                # break
            temp *= i

print(count)