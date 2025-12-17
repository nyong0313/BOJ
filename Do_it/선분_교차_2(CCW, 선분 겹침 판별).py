# 17387
import sys
sys.stdin.readline
# A, B
x1, y1, x2, y2 = map(int, input().split())
# C, D
x3, y3, x4, y4 = map(int, input().split())
ans = [0]*4

def CCW(x1, y1, x2, y2, x3, y3):
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

abc = CCW(x1, y1, x2, y2, x3, y3)
abd = CCW(x1, y1, x2, y2, x4, y4)
cda = CCW(x3, y3, x4, y4, x1, y1)
cdb = CCW(x3, y3, x4, y4, x2, y2)

if abc == 0 and abd == 0:
    minXAB = min(x1, x2)
    maxXAB = max(x1, x2)
    minXCD = min(x3, x4)
    maxXCD = max(x3, x4)
    minYAB = min(y1, y2)
    maxYAB = max(y1, y2)
    minYCD = min(y3, y4)
    maxYCD = max(y3, y4)
    if minXAB <= maxXCD and minXCD <= maxXAB and minYAB <= maxYCD and minYCD <= maxYAB:
        print(1)
    else:
        print(0)
elif abc * abd <= 0 and cda * cdb <= 0:
    print(1)
else:
    print(0)