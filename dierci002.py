#打印小猫爱吃鱼，小猫要喝水
class Animal():
    def __init__(self, cat):
        self.cat = cat
        print( end='')

    def a1(self):
        print(self.cat, '爱吃鱼')
    def a2(self):
        print(self.cat, '爱喝水')

a=Animal('小猫')
a.a1()
a.a2()