def binaryserch(a, x):
    mid = tempmid = len(a) // 2  # mid 用于记录数组a的中间数，tempid 用于记录原始数组中mid的值
    while len(a) > 1:
        if a[mid] > x:
            a = a[:mid]
            mid = len(a) // 2
            tempmid = tempmid - (len(a) - mid)
        elif a[mid] < x:
            a = a[mid + 1:]
            mid = len(a) // 2
            tempmid = tempmid + mid + 1
        else:
            break
    if len(a) == 1:
        tempmid = tempmid if a[mid] == x else -1
    if len(a) < 1:
        tempmid = -1

    return tempmid

if __name__ == '__main__':
    a = [2, 3, 4, 10, 40]
    x=10
    res = binaryserch(a,x)
    if res != -1:
        print("元素在数组中的索引为 %d" % res)
    else:
        print("元素不在数组中")