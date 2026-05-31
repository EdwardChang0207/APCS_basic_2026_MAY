'''
for while

while <cond:bool>:
    ...

1, 2, 4, 8, 16, 32, 64, 128, 256, 512    
i = 1 #索引值 index idx
while i <= 512:
    print(i)
    i = i * 2

for i in ['鮭魚','鮪魚','玉子燒']:
    print(i)
    if i == '鮭魚':
        print('拿'+i)
for i in 'hello':
    print(i)

range(start[init:0], end, interval[init:1])   
start -> end-1 
2, 4, 6, 8, 10
5, 3, 1, -1, -3, -5
for i in range(5, -6, -2):
    print(i, end=' ')
for i in range(5):
    print('abc')

1 2 4 8 16 32 64
1 4 9 16 25 36 49
l = [2**i for i in range(7)]
l = [i**2 for i in range(1,8)]
print(l)
l = [i for i in range(10) if i%2==0]
print(l)

#'10 20 30 40 50'
l = [int(i) for i in input().split()]
print(l)

continue(skip) break(stop)
for i in range(10):
    if i % 3 == 0:
        continue
    if i == 8:
        break
    print(i, end=' ')
'''