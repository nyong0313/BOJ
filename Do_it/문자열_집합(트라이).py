# 14425
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
textList = [[]for _ in range(n)]

for i in range(n):
    textList[i] = input()

ans = 0

for i in range(m):
    text = input()
    if text in textList:
        ans += 1
    # for j in range(n):
    #     if text == textList[j]:
    #         ans += 1

print(ans)