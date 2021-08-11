class Person:
    has_hair = True


    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sayhello(self,words):
        print("hello,I'm",self.name)
        print(words)

if __name__ == '__main__':
    J = Person(name = input('name:\n'),age = input('age:\n'))
    J.sayhello('welcome to python')

    T = Person(name = input('name:\n'),age = input('age:\n'))
    T.sayhello('welcome to python too')

