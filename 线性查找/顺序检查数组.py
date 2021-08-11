def search(arr,n,x):

    for i in range(0,n):
        if (arr[i]==x):
            return i;

    return -1

if __name__ == '__main__':
    arr=['a','b','c','d','e''f']
    x = 'd'
    n = len(arr)
    res = search(arr,n,x)
    if (res==-1):
        print('元素不在数组数组中')

    else:

        print('元素在数组中的索引为：',res)