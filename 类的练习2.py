'''
class Student:
    #def __init__(self, name):

       # self.name = name
    def study(self,name):
        print(name,'学习')

    def kecheng(self,name):
        print(name,'课程')
a=Student()
a.study('小红')
a.kecheng('小红')
'''
'''
class Student:
    def __init__(self, sno,name):

       self.sno = sno
       self.name = name


    def study(self,kecheng):
        print(self.sno,self.name,'学习',kecheng)





a=Student('123','小明')
a.study('数学')
'''
'''
class Animal:
    def __init__(self, color):
        self.color = color

    def eat(self):
        print('......吃')
    def drink(self):
        print('......喝')

class Dog(Animal):
    def __init__(self, color,size):
        Animal.__init__(self, color)
        self.size= size
    def bark(self):
        print('......汪汪叫')

class Cat(Animal):
    def bark(self):
        print('.......抓老鼠')
wangcai=Dog()
wangcai.eat()
wangcai.bark()
'''















