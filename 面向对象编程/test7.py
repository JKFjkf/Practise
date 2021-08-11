class Father():
    def __init__(self):
        self.earn_money = 1000
        self.spend_money =  -500

class Son(Father):
    def __init__(self):
        super().__init__()
    def add(self):
        return self.spend_money+self.spend_money


son = Son()
print(son.add())