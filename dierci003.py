#2、小明爱跑步，爱吃东西。
#1）小明体重75.0公斤
#2）每次跑步会减肥0.5公斤
#3）每次吃东西体重会增加1公斤
#4）小美的体重是45.0公斤

class Person:
    def __init__(self,name):
        self.name=name


    def eat(self,weight):
        weight += 1
        print('%s吃东西后的体重是%d公斤'%(self.name,weight))

    def run(self, weight):
        weight -= 0.5
        print('%s跑步后的体重是%f公斤' % (self.name, weight))

    def a1(self,weight):
        print('%s的体重是%d公斤' % (self.name, weight))






a=Person('小明')
a.eat(75)
a.run(75)

a=Person('小美')
a.a1(45)

