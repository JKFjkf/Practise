#析构函数
class MyClass(object):

    message = 'Hello world'
    def show(self):
        print(self.message)

    def __int__(self,name = 'unset',sex = 'man'):
        print('this people is :',name,"",sex)

    def __del__(self):
        print('world is over!')

i = MyClass()
i.show()

i2 = MyClass('jsaor')
i2.show()

del i,i2

i3 = MyClass("lisa","women")
i3.show()

del i3