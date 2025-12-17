import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()
mylist = [0] * n
sum = 0
sum_output = 0
# 이렇게 직관적으로 말고 p[i]*(n-i)를 다 더하는 방법으로하면 간단하겠네.
# X 합배열을 이용하면 더 쉽다.. S[i] = S[i-1] + A[i]
for i in range(n):
    sum += p[i]
    mylist[i] = sum
    sum_output += mylist[i]

print(sum_output)