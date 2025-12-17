# 13398
# Key : k를 제외한 최대값 (배열 XX)
# ans = L[k-1] + R[k+1] -> (0 ~ k-1)의 최대합 + (k+1 ~ n)의 최대합
# Key2 : (0~k)의 최대합 = 0~k합 or k (둘중하나임.)***
# Key3 : ans 초기값 = L배열 중 최대값
import sys
input = sys.stdin.readline
n = int(input())
myList = list(map(int, input().split()))
L = [0]*n
R = [0]*n

L[0] = myList[0]
R[n-1] = myList[n-1]
ans = L[0]

for i in range(1, n):
    L[i] = max(L[i-1] + myList[i], myList[i])
    ans = max(ans, L[i])

for i in range(n-2, -1, -1):
    R[i] = max(R[i+1] + myList[i], myList[i])

for i in range(1, n-1):
    ans = max(ans, L[i-1] + R[i+1])

print(ans)