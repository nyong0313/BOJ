# 1016
# 문제 잘못해석함. 거듭제곱이 아니고 제곱 하나만 해당함.
import sys, math
input = sys.stdin.readline

min_n, max_n = map(int, input().split())
m_n_len = max_n-min_n+1
a = [1] * m_n_len

for i in range(2, int(math.sqrt(max_n)) + 1):
    temp = i * i # k^2
    start_index = (temp - (min_n % temp)) % temp # 중요 point **
    if temp <= max_n:
        for j in range(start_index, m_n_len, temp):
            a[j] = 0

print(sum(a))