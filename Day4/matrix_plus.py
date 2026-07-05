r, c = [int(i) for i in input().split()]
A = [[int(j) for j in input().split()] for i in range(r)]
B = [[int(j) for j in input().split()] for i in range(r)]

for i in range(r):
    for j in range(c):
        A[i][j] += B[i][j]

for i in range(r):
    print(*A[i])