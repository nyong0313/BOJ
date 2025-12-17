# ch07 - 37/1929
import math
prime = [True]*1000001
prime[0] = prime[1] = False

for i in range(2, int(math.sqrt(1000001))):
    if prime[i]:
        for j in range(i+i, 1000001, i):
            prime[j] = False

m, n = map(int, input().split())
for i in range(m, n+1):
    if prime[i]:
        print(i)