import time
import multiprocessing

def doIt(num):
    print("Process num is : %s" % num)
    time.sleep(1)
    print("process %s end" %num)


if __name__ == '__main__':
    print('mainProcess start')
    start_time = time.time()
    pool = multiprocessing.Pool(3)
    print("Child start")
    for i in range(3):
        pool.apply(doIt,[i])
    print('mainprocsee done time:%s s' %(time.time() - start_time))
    pool.close()
    pool.join()