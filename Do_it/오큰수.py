# 스택을 만들고 순서대로 어팬드.
# 스택의 탑과 새로 들어오려는 애를 비교,
# 새로 들어오려는 애가 더 크면 탑의 오큰수로 판단하고 
# 탑의 인덱스에 해당하는 결과 리스트에 오큰수 저장 및 탑을 팝해서 빼버림.
# 그 밑에도 비교하고 반복.
# 반복하다 탑보다 새로운 값이 작은 경우 or 스택 빈 경우에는 어팬드
# 반복 or 더 이상 없을 경우 스택에 존재하는 애들 다 -1 입력. (= 오큰수 없음)

n = int(input())
nge = list(map(int, input().split()))
mystack = []
result = [0] * n

for i in range(n):
    # 스택의 top = stack[-1]
    while mystack and nge[mystack[-1]] < nge[i]:
        result[mystack[-1]] = nge[i]
        mystack.pop()
        # 위 두줄을 result[mystack.pop()] = nge[i] 으로 깔끔하게 변경 가능.

    # 스택에 인덱스를 저장 !!
    mystack.append(i)

while mystack:
    result[mystack[-1]] = -1
    mystack.pop()

for i in range(n):
    print(result[i], end=" ")