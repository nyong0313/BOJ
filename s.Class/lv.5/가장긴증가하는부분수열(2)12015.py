# D[i] = A[i]보다 작은 값(0~i-1) 중 최대 길이에 + 1
# O(nlogn)
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
ans = [a[0]]

def binsearch(now):
    l = 0
    r = len(ans) - 1

    while l < r:
        mid = (l+r)//2
        if ans[mid] < now:
            l = mid+1
        else:
            r = mid
    return l

# 실제 LIS는 아니지만 "길이" 값 만큼은 조건을 만족
for i in a:
    if ans[-1] < i:
        ans.append(i)
    else:
        index = binsearch(i)
        ans[index] = i

print(len(ans))