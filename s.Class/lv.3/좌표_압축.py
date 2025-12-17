# 18870
# 해당 좌표보다 작은 수 개수
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(set(a))
b.sort()

# 정렬 + 인덱스 이용
b_dic = {}
for i in range(len(b)):
    b_dic[b[i]] = i

for i in range(n):
    print(b_dic[a[i]], end=" ")