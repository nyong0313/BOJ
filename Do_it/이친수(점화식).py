# 2193
n = int(input())
D = [(0, 0)]*(n+1)
D[1] = (1, 0)

if n == 1:
    print(1)
else:
    for i in range(2, n+1):
        D[i] = (2*D[i-1][1] + (D[i-1][0] - D[i-1][1]), D[i-1][1] + (D[i-1][0] - D[i-1][1]))
        
    print(D[n][0])