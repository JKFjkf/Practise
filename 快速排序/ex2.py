def quickSort(arr):
    if(len(arr)<2): #不用进行排序
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if(i<pivot)]
        great=[i for i in arr[1:] if(i>pivot)]
        return quickSort(less)+[pivot]+quickSort(great)
arr=[1,4,5,2,41,4,24,5]
print("原始数据：",arr)
print("排序后的数据：",quickSort(arr))