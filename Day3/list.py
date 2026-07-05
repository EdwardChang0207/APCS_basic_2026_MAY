'''
l=[] #空串列 -> False
l = []
if l: print(123)
else: print('hello')

l[start(init:0):end(init:-1):interval(init:1)]
start -> end-1

1.length -> len()
2.maximum -> max()
3.minimum -> min()
4.sum -> sum()
l = [i for i in range(10)]
print(len(l))
print(max(l))
print(min(l))
print(sum(l))
avg: sum(l)/len(l)

#. -> 1.的 2.對...做...
1.新增 append()
2.移出 pop()
3.插入 insert()
4.刪除 remove()
5.倒轉 reverse()
6.排序 sort()
7.排序（不改變原本的）sorted() 
8.數 count()
9.找東西 index()
l = [1,2,3]
l.append(4)
print(l)
i = l.pop(0)
print(l, i)
l.insert(0, 5)
print(l)
l.remove(2)
print(l)
l.reverse()
print(l)
# l.sort()
print(sorted(l))
print(l)
l = [1,2,3,4,1,2,2,3,3,1]
print(l.count(1))
print(l.index(3))
'''