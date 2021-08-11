def insertionSort(list):
    n = len(list)
    for i in range(1,n):  #默认数列中的第一个元素已排好，故从第二个元素开始插入
        j = i
        while list[j] < list[j-1] and j>0:  #和已经排好序的数从右往左比较，小于则交换位置
            list[j],list[j-1] = list[j-1],list[j]
            j-=1
    return list

list=[2,1,0,5,7,4,0]
print(insertionSort(list))