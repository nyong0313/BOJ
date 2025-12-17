import sys
input = sys.stdin.readline
from collections import deque

expression = input().strip()
num = ''
tokens = []
count = 0

for char in expression:
    if char.isdigit():
        num += char  # 숫자일 경우 num에 추가 but 소수는 불가능.
    else:
        tokens.append(int(num))  # 숫자 저장
        tokens.append(char)  # 연산자 저장
        num = ''  # 숫자 초기화
        count += 2

tokens.append(int(num))  # 마지막 숫자 추가
count += 1

tokens = deque(tokens)
ans = 0
temp = 0
bracketMode = False
while tokens:
    token = tokens.popleft()
    if bracketMode:
        if token == "-":
            ans -= temp
            temp = 0
        elif token == "+":
            continue
        else:
            temp += token
    else:
        if token == "-":
            bracketMode = True
        elif token == "+":
            continue
        else:
            ans += token

if bracketMode:
    ans -= temp

print(ans)