# 1722
n = int(input())
inputList = list(map(int, input().split()))
factorial = [0]*21
visited = [False]*21

# 팩토리얼 값 배열로 미리 저장
factorial[0] = 1
for i in range(1, 21):
    factorial[i] = factorial[i-1] * i

# k를 입력받고 k번째 수열을 구하는 경우
if inputList[0] == 1:
    ans = [0]*21
    k = inputList[1]

    # 정답 배열의 i번째 수 구하기
    for i in range(1, n+1):
        cnt = 1 # ex) cnt = 1: 가능한 숫자 중에서 제일 작은 수, 2: 두번째로 작은수

        # 사용할 수 있는 숫자
        for j in range(1, n+1):
            if visited[j]: # 숫자 썼는지 check
                continue # 아래 코드를 실행하지 않고 건너뜀
            
            # i번째 자리에 숫자 하나 당 (n-i)!의 경우의 수가 있음.
            # 따라서 (n-1)! 넘을 때 마다 cnt(몇번째로 작은수 인지)가 올라감
            if k <= cnt * factorial[n-i]: 
                k -= (cnt-1) * factorial[n-i] # i번째 자리의 경우의 수 빼기 -> 그다음 자리의 경우의 수 구함
                ans[i] = j
                visited[j] = True
                break

            cnt += 1 # 가능한 숫자 중에서 그다음으로 작은 수
    
    for i in range(1, n+1):
        print(ans[i], end=" ")


# 임의의 수열을 입력받고 몇 번째 수열인지 구하는 경우
else:
    ans = 1
    # 몇번째 자리의 수열인지
    for i in range(1, n+1):
        cnt = 0

        # 더 작은 수 몇개 안썼는지 개수 세기
        for j in range(1, inputList[i]):
            if not visited[j]:
                cnt += 1

        ans += cnt * factorial[n-i]
        visited[inputList[i]] = True

    print(ans)