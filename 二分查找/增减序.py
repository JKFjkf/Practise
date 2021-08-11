# 二分查找（非递归版本）
# isAsc为True时，列表增序，否则减序
def binarySearch(sortedList, key, isAsc=True):
    left = 0                                             # 查找范围最左边的下标
    right = len(sortedList) - 1                          # 查找范围最右边的下标
    while left <= right:                                 #
        mid = left + right >> 1                          # 中间数下标（向下取整）
        if isAsc and sortedList[mid] < key \
                or not isAsc and sortedList[mid] > key:  # key在中间数右边时，查找范围变为右边
            left = mid + 1
        elif isAsc and sortedList[mid] > key \
                or not isAsc and sortedList[mid] < key:  # key在中间数左边时，查找范围变为左边
            right = mid - 1
        else:
            return mid                                   # key为中间数时，返回其下标
    return -1
if __name__ == '__main__':
    a = [40, 10, 5, 4, 3]
    x=10
    res = binarySearch(a,x,False)
    if res != -1:
        print("元素在数组中的索引为 %d" % res)
    else:
        print("元素不在数组中")