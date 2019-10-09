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







