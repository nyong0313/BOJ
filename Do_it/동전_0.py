import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = []
max_coin = 0
for i in range(n):
    a.append(int(input()))
    if max_coin < a[i] and a[i] <= k:
        max_coin = a[i]
        max_coin_index = i

count = 0
for i in range(max_coin_index, -1, -1):
    # if k == 0: break 

    count += k // a[i]
    k = k % a[i]

print(count)