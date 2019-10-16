'''
class Person():
    #构造方法，在实例化的时候自动被执行
    def __init__(self,name,sex):
        print('执行init方法')
        self.name=name
        self.sex=sex
    #属性
    def eat(self,food):
        print('吃',food)


    def sleep(self):
        print(self.name,'睡觉')
#实例化
a=Person('小明','男')
a.sleep()

#调用类中的方法
#a.sleep()
#a.eat('米饭')
'''

