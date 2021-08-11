class Father():
    def __init__(self):
        self.money = 1000

class Son(Father):
    def __init__(self):
        Father.__init__(self)

son = Son()
print(son.money)