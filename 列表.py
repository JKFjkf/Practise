list = ['Google', 'Runoob', 1997, 2000]
list1 = ['google','runob',1991,2000]
list2 = [1,2,3,4,5]

print("list1[0]:",list1[0])
print("list2[1:5]:",list2[1:5])
print("第三个元素为：",list[2])
list[2] = 2001
print("更新后的第三个元素为：",list[2])
print("原始列表：",list)
del  list[2]
print("删除第三个元素：",list)
print(len(list))