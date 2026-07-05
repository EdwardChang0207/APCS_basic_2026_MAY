R, C, M = [int(i) for i in input().split()]
B = [input().split() for _ in range(R)]
k = [int(i) for i in input().split()]

k.reverse()
for i in k:
    if i == 0: #rotate
        #轉置
        BT = []
        for i in range(len(B[0])):
            col = []
            for j in range(len(B)):
                col.append(B[j][i])
            BT.append(col)
        B = BT
        #翻轉
        B.reverse()
    else: #flip
        B.reverse()

print(len(B),len(B[0]))
for row in B:
    print(*row)