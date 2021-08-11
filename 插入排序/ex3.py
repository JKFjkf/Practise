arr = [1,12,2, 11, 13, 5, 6,18,4,9,-5,3,11]

def insertionSort(arr):
    #从要排序的列表第二个元素开始比较
    for i in range(1,len(arr)):
        j = i
        #从大到小比较，直到比较到第一个元素
        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1
    return arr
print(insertionSort(arr))