class Father():
    __money = 1000#私有变量继承不了
    def __action(self):#父类私有方法
        money = 1000
        print("调用了父类方法")

class Son(Father):
    def action(self):
        super()._Father_action()
        print(money)


son = Son()
son.action()