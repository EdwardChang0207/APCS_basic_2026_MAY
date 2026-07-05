'''
input: r, c(A's size)
    ... (A)
    ...
    ...

output: AT
'''

r, c = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for _ in range(r)]
AT = []

for i in range(c):
    col = []
    for j in range(r):
        col.append(A[j][i])
    AT.append(col)

for i in AT:
    print(*i)