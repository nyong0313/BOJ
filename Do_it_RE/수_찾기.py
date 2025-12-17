# ch05 - 29/1920
n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

def binsearch(l, r, k):
    mid = (l + r) // 2
    if a[mid] == k:
        return 1
    
    if k > a[mid]:
        if mid+1 <= r:
            return binsearch(mid+1, r, k)
        else:
            return 0
    else:
        if l <= mid-1:
            return binsearch(l, mid-1, k)
        else:
            return 0

for i in b:
    print(binsearch(0, n-1, i))