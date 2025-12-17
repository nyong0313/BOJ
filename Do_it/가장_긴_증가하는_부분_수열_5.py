# 14003
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0) # 인덱스 1부터 시작

maxLen = 1
b = [0] * (n+1)
d = [0] * (n+1)
ans = [0] * (n+1)
b[1] = a[1]
d[1] = 1

def binsearch(l, r, now):
    while l < r:
        mid = (l+r)//2
        if b[mid] < now:
            l = mid+1
        else:
            r = mid
    return l

for i in range(2, n+1):
    if b[maxLen] < a[i]:
        maxLen +=1
        b[maxLen] = a[i]
        d[i] = maxLen
    else:
        index = binsearch(1, maxLen, a[i]) #a[i] 보다 작은 값 바로 다음 위치 반환 (= 큰 값 위치)
        b[index] = a[i]
        d[i] = index

print(maxLen)
index = maxLen

for i in range(n, 0, -1):
    if d[i] == index:
        ans[index] = a[i]
        index -= 1

for i in range(1, maxLen+1):
    print(ans[i], end=" ")