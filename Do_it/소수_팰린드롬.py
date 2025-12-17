import sys, math
from collections import deque
input = sys.stdin.readline

n = int(input())
LIMIT = 10000000
prime_number = [True] * (LIMIT+1)
prime_number[0] = prime_number[1] = False

for i in range(2, int(math.sqrt(LIMIT)) + 1):
    if prime_number[i]:
        for j in range(i + i, LIMIT + 1, i):
            prime_number[j] = False

for i in range(n, LIMIT+1):
    if prime_number[i]:
        ans_true = True
        num = deque()
        num_len = len(str(i))
        while i:
            num.appendleft(i % 10)
            i //= 10
        for j in range(num_len // 2):
            if num[j] != num[num_len-1-j]:
                ans_true = False
                break

        if ans_true:
            ans = 0
            for j in range(num_len):
                ans += num.pop()*10**j
            print(ans)
            exit()