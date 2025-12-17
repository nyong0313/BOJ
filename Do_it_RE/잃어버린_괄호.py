#  ch06 - 36/1541
# split 함수 응용 ***
a = list(input().split("-"))
b = []

for i in a:
    temp = list(map(int, i.split("+")))
    b.append(sum(temp))

ans = 0
for i in range(len(b)):
    if i == 0:
        ans += b[i]
        continue

    ans -= b[i]

print(ans)    