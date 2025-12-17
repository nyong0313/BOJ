# 11758
# CCW counter clock wise : 벡터 외적 -> 시계(<0), 직선(=0), 반시계(>0)
# |CCW|/2 = 삼각형 넓이
p = []
for _ in range(3):
    x, y = map(int, input().split())
    p.append((x, y))

# ccw = (p[0][0]*p[1][1] + p[1][0]*[2][1] + p[2][0]*p[0][1]) - (p[0][0]*p[2][1] + p[1][0]*p[0][1] + p[2][0]*p[1][1])
ccw = 0
for i in range(3):
    ccw += p[i][0] * p[(i+1)%3][1]
for i in range(2, -1, -1):
    ccw -= p[i][0] * p[i-1][1]

if ccw < 0:
    print(-1)
elif ccw > 0:
    print(1)
else:
    print(0)