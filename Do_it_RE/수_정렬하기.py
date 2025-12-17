# ch04 - 15/2750
n = int(input())
a = [0]*n

for i in range(n):
    a[i] = int(input())

a.sort()
for i in a:
    print(i)