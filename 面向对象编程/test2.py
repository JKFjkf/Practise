class Person():
    Count = 0
    def __init__(self,name,age):
        Person.Count += 1
        self.name = name
        self.__age = age


p = Person("Runsen",20)
print(p.Count)

print(p.name)
print(p.__age)