# 1722 복습
n = int(input())
inputList = list(map(int, input().split()))
visited = [False]*21
factorial = [0]*21
factorial[0] = 1
for i in range(1, 21):
    factorial[i] = factorial[i-1] * i

if inputList[0] == 1:
    k = inputList[1]
    ans = [0]*21
    # 정답 배열
    for i in range(1, n+1):
        cnt = 1
        for j in range(1, n+1):
            if visited[j]:
                continue
            if k <= cnt * factorial[n-i]:
                k -= (cnt-1) * factorial[n-i]
                ans[i] = j
                visited[j] = True
                break
            cnt += 1
    for l in range(1, n+1):
        print(ans[l], end=" ")

else:
    ans = 1
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, inputList[i]):
            if not visited[j]:
                cnt += 1
        visited[inputList[i]] = True
        ans += cnt*factorial[n-i]
    print(ans)