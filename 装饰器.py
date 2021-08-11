import time

def printtime(func):
    def wrapper(*args,**kwargs):
        print(time.ctime())
        return func(*args,**kwargs)

    return wrapper

@printtime  #装饰器：通过装饰器来加强程序
def printhello(name):
    print('hello',name)

if __name__ == '__main__':
    #print('请输入你的名字：\n')
    #name = input()
    #printhello(name)
    printhello_plus = printtime(printhello)
    printhello_plus('jasor')