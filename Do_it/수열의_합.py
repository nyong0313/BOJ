n, l = map(int, input().split())

while 1:
    a = (2*n - l*l + l) // (2 * l)
    if a >= 0 and (2*n - l*l + l) % (2 * l) == 0:
        # print(a, l)
        for i in range(l):
            print(a + i, end=" ")
        break
    elif a < 0 or l > 100:
        # print(a, l)
        print(-1)
        break
    l = l+1