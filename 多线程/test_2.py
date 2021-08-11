import multiprocessing

def test(i):
    print(i)


if __name__ == '__main__':
    list1 = list(range(5))
    pool1 = multiprocessing.Pool(processes=4)#创建一个进程池
    pool1.map(test,list1)
    pool1.close()
    pool1.join()