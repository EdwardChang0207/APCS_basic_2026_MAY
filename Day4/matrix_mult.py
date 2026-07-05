r, c = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for _ in range(r)]
m, n = [int(i) for i in input().split()]
B = [[int(i) for i in input().split()] for _ in range(r)]
C = []

if c != m: print('Error')
else:
    for i in range(r):
        row = []
        for j in range(n):
            x = 0
            for k in range(c):
                x += A[i][k]*B[k][j]
            row.append(x)
        C.append(row)

    for i in C:
        print(*i)