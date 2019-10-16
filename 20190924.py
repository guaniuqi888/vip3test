'''
#1.输入一个数，判断该数的范围：90-100：等价为A……60以下：等级为E
a=int(input('输入分数：'))
if a>=90:
    print('A')
elif a>=80:
    print('B')
elif a>=70:
    print('C')
elif a>=60:
    print('D')
else:
    print('E')
'''

'''
#2.定义一个列表，从键盘输入一个随机数，判断该数是否在列表中
a=[1,2,3,4,5,6,7,8,9]
b=int(input('输入一个随机数：'))
if b in a:
    print('存在')
else:
    print('不存在')
'''

'''
#3、求10阶乘
m=1
for i in range(1,11):
    m=m*i
print(m)
'''

'''
#4、求100以内能被3整除的数，并将作为列表输出
a=[]
for i in range(3,100,3):
    a.append(i)
print(a)
'''

'''
#5、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表

orgList = [1,2,3,4,3,4,2,5,5,8,9,7]
formatList = []
for id in orgList:
    if id not in formatList:
        formatList.append(id)
print (formatList)
'''

'''
#6、求斐波那契数列 1 2 3 5 8 13 ……
def fib_recur(n):

  if (n ==1)or (n ==2):
    return n
  return fib_recur(n-1) + fib_recur(n-2)

for i in range(1, 20):
    print(fib_recur(i))
'''

'''
#求10000以内的质数
num=[];

for i in range(2,10000):

   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)
'''


'''
class student:
    def study(self,study):
        print('学习')

    def course(self,course):
        print('课程')

a=student()
'''

'''
n=1
sum=0
while n<101:
    sum+=n
    n+=1
print(sum)
'''

'''
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print((add_end()))
'''

'''
def calc(*numbers):
    a=1
    for n in numbers:
        a=a*n
    return a
b=[1,2,3]
print(calc(*b))
'''
'''
def add(a,b):
    a=int(input('输入第一个数：'))
    b=input('输入运算符号：')
    c=int(input('输入第一个数：'))
    if b=='+':
        d=a+c
        print(a,b,c,'=',d)
    elif b=='-':
        d = a -c
        print(a, b, c, '=', d)
    elif b == '*':
        d = a *c
        print(a, b, c, '=', d)
    elif b == '/':
        d = a / c
        print(a, b, c, '=', d)

add(3,4)
'''
'''
def person(name,age,**kwarges):
    print('name',name,'age',age,kwarges)

extra={'city':'beijing','job':'math'}
person('xiaoming',25,**extra)
'''
'''
def calc(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('除数不能为0')

a=int(input(''))
b=int(input(''))
calc(a,b)
'''
'''
def calc(a,b):
    try:
        print(a/b)
    except BaseException:
        print('除数不能为0')

a=int(input(''))
b=int(input(''))
calc(a,b)
'''
'''
def calc(a,b):
    try:
        print(a/b)
    except Exception:
        print('除数不能为0')

a=int(input(''))
b=int(input(''))
calc(a,b)
'''

'''
def add(a,b):
    a=int(input('输入第一个数：'))
    b=input('输入运算符号：')
    c=int(input('输入第一个数：'))
    if b=='+':
        d=a+c
        print(a,b,c,'=',d)
    elif b=='-':
        d = a -c
        print(a, b, c, '=', d)
    elif b == '*':
        d = a *c
        print(a, b, c, '=', d)
    elif b == '/':
        try:
            d = a / c
            print(a, b, c, '=', d)
        except BaseException:
            print('除数不能为0')
        finally:
            print('程序执行完毕')

add(3,4)
'''
'''
def calc(a,b):
    try:
        print(a/b-c)
    except NameError:
        print('该对象未声明')

a=int(input(''))
b=int(input(''))
calc(a,b)
'''
'''
L=[]
f = open('F:\\2wan\\data.txt','r+')
#print(f.readlines())
a=f.readlines()

for i in a:
    i=i.strip()
    L.append(int(i))


c=sorted(L)
#print(c)
d=[]
w=open('F:\\2wan\\backup.txt','w+')

for m in c:
    m=str(m)
    d.append(m)
for n in d:
    w.write(n)
    w.write('\n')

w.seek(0)
print(w.read())
'''


'''
a=[1,2,3,4,5]
s1=[str(i)for i in a]
b='+'

print(b.join(s1))
'''

'''
a='hello world'
print(a.split('l'))
'''








































