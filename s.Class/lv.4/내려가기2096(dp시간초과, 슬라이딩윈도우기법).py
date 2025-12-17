# 메모리 초과 -> 슬라이딩 윈도우 기법
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dpMax = a
dpMin = a

for _ in range(1, n):
    a = list(map(int, input().split()))
    #dpMax
    dpMax = [max(dpMax[0], dpMax[1]) + a[0], 
             max(dpMax[0], dpMax[1], dpMax[2]) + a[1], 
             max(dpMax[1], dpMax[2]) + a[2]]
    #dpMin
    dpMin = [min(dpMin[0], dpMin[1]) + a[0], 
             min(dpMin[0], dpMin[1], dpMin[2]) + a[1],
             min(dpMin[1], dpMin[2]) + a[2]]
    
print(max(dpMax), min(dpMin))