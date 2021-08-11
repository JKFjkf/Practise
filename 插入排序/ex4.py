"""插入排序
InsertionSort.py"""

# 一次往数组添加多个数字
def AppendNumbers(array):
    num = input('Numbers:(split by spaces)\t').split()
    for i in num:
        array.append(int(i))
    print('排序前数组：{}.'.format(array))

def InsertionSort(array):
    AppendNumbers(array)  # 添加

    list = []
    while True:
        for i in array:
            minimum = min(array)
            if i == minimum:
                list.append(i)
                array.remove(i)  # 删去最小值

        if array == []:
            break

    print('排序后数组：{}.'.format(list))

array = [6, 4, 45, -2, -1, 2, 4, 0, 1, 2, 3, 4, 5, 6, -4, -6,  7, 8, 8, 34, 0]
InsertionSort(array)