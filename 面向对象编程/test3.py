class Father():
    def __init__(self):
        self.money = 1000
    def action(self):
        print("调用了父类方法")

class Son(Father):    #子类son继承父类father的所有属性和方法
    pass


son = Son()
son.action()#调用父类方法
print(son.money)