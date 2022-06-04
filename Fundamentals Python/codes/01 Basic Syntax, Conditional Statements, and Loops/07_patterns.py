n = int(input())

for i in range(0, n):
    print(i * '*')
    if i == n-1:
        for j in range(n, 0, -1):
            print(j * '*')
