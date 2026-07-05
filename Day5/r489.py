R, C = [int(i) for i in input().split()]
A = [input().split() for _ in range(R)]
B = [input().split() for _ in range(R)]
r = 0
for _ in range(4):
    #計算相似度
    ans = 0
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        ans = 0
    else:
        s = 0
        for i in range(R):
            for j in range(C):
                if A[i][j] == B[i][j]: s += 1
        ans = int((s/(R*C))*100)
    #比較目前的結果是否比目前的「最佳」還要更好 -> 更新？
    if ans > r: r = ans
    #旋轉90度
    B.reverse()
    BT = []
    for i in range(len(B[0])):
        col = []
        for j in range(len(B)):
            col.append(B[j][i])
        BT.append(col)
    B = BT
print(f'{r}%')