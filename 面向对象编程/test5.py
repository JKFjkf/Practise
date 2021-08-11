class Father():
    def __init__(self):
        self.money = 0

    def action(self):
        print("调用了父类方法")

class Son(Father):
    def __init__(self):
        self.money = 1000
    def action(self):
        print("子类重写父类方法")

son = Son()#子类son继承父类father的所有属性和方法
son.action()#子类son调用自身的action而不是父类的action方法
print(son.money)#自己的1000