#定义一个Teacher类，继承Person类，拥有自身的属性工号：gh，自身的方法：teach教课（课程）；
#1、实现gh为xx的老师，教xx课
#2、实现gh为xx老师，在xx上班，一月工资xx
#3、名字是xx，工号为xx的老师，吃饭

class Person:
    def work(self,work,gongzi):
        print('在',work,'上班','一月工资',gongzi)
    def name(self,name):
        print('名字是',name,'吃饭')

class Teach(Person):
    def __init__(self, gh):
        self.gh=gh
        print(gh,end=' ')
    def teacher1(self,kecheng):
        print('教',kecheng)


a=Teach('001')
a.teacher1('语文')
a=Teach('001')
a.work('华为','2000')
a=Teach('001')
a.name('张三')