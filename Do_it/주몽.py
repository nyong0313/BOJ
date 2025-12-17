n = int(input())
m = int(input())
A = list(map(int, input().split()))

A.sort()

i = 0
j = n-1
count = 0

# != 하지말고 < 로 하기 !! **
while i < j:

    sum = A[i] + A[j]

    if sum == m:
        count += 1
        i += 1
        j -= 1

    elif sum < m:
        i += 1

    else:
        j -= 1

print(count)