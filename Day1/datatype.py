'''
1.Numbers
    (1)整數 integer -> int:沒有小數點的數
    (2)浮點數 float -> float:有小數點的數
    eg. -1(int), pi(float), 3.0(float)
2.Text
    (1)字串 string -> str:''/""
3.Boolean
    (1)True(1)/False(0) -> bool:布林值
4.List
    l = [123, True, 'hi', 3.14]
    #.    0.    1.    2.    3
    print(l[1])
'''
#split(',')
#'10 20'
#1.的 2.對...做...
#input() -> '10 20'
a, b = input().split()#['10', '20']
a = int(a)
b = int(b)
print(a+b)