# 30804
# 처음부터 구간 늘려가기
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
# 과일번호 1~9
cnt = [0]*10
kind = set()

s = 0
e = 0
ans = 0

cnt[a[0]] += 1
kind.add(a[0])

while s <= e:
    if len(kind) <= 2:
        ans = max(ans, e+1-s)
        if e < n-1:
            e += 1
            cnt[a[e]] += 1
            if a[e] not in kind:
                kind.add(a[e])
        else:
            break
    else:
        cnt[a[s]] -= 1
        if cnt[a[s]] == 0:
            kind.remove(a[s])
        s += 1

print(ans)