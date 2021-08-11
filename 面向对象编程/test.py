class public():
    _name = 'protected类型的变量'
    __info = '私有类型的变量'
    def _f1(self):
        print("这是一个protected的方法")
    def _f2(self):
        print("这是一个私有类型的方法")
    def get(self):
        return(self._info)


pub = public()
print(pub._name)
print(pub.__info)
print(pub._f2)