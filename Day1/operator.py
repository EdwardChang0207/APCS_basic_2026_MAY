'''
operator 運算子

1.Math
    int op int -> int
    float op float -> float
    int op float -> float

    / -> float

    (1)+加法
    (2)-減法
    (3)*乘法
    (4)/除法
    (5)//整除(商的整數部分)
    (6)%取餘數
    (7)**次方
    20/3 = 6(商數)...2（餘數）

2.關係
    num op num -> bool
    (1)>大於
    (2)<小於
    (3)==等於
    (4)!=不等於
    (5)>=大於等於
    (6)<=小於等於
    (7)in...裡面
    l = [1, 2, 3, 4, 5]
    print(10 in l)

3.boolean logic gates
    bool op bool -> bool
    (1) not 反閘
        周杰倫：哎呦不錯喔
        不錯 -> True
        錯 -> False

        不行 -> False
        行 -> True
    (2) or 或閘
        MATH or ENG -> 3000
        T.      F.     T
        F.      T.     T
        T.      T.     T
        F.      F.     F 真值表 Truth table
    (3) and 且閘
        打掃 and HW -> :)
        T.      F.    F
        F.      T.    F
        T.      T.    T
        F.      F.    F
    (4) xor (exculusive or) 斥或閘
        珍奶 xor 烏龍 -> :)
        T.      F.      T
        F.      T.      T
        T.      T.      F
        F.      F.      F
        [1] not or and
            (a or b) and not(a and b)
        [2] ^
        a, b = 3, 5
        print((a or b) and not(a and b))
        print(a ^ b) # xor

s1, s2 = 'abc', 'def'
print(s1 + s2) # 字串串接

l1, l2 = [1, 2], [3, 4]
print(l1 + l2) # 串接串列
print('abc'*3)
print([1,2]*3)
'''