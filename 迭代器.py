# 迭代器的概念
# 迭代器协议 —— 内部含有__next__和__iter__方法的就是迭代器

# 迭代器协议和可迭代协议
# 可以被for循环的都是可迭代的
# 可迭代的内部都有__iter__方法
# 只要是迭代器 一定可迭代
# 可迭代的.__iter__()方法就可以得到一个迭代器
# 迭代器中的__next__()方法可以一个一个的获取值
#迭代器的好处：
    # 从容器类型中一个一个的取值，会把所有的值都取到。
    # 节省内存空间
        #迭代器并不会在内存中再占用一大块内存，
            # 而是随着循环 每次生成一个
            # 每次next每次给我一个

#列表List、元组Tuple、字典Dictionary、字符串String等数据类型虽然是可迭代的，
#但都不是迭代器，因为他们都没有next( )方法。

#iter()函数，Python中的iter( object[, sentinel])函数可用来返回一个迭代器对象，

a=[1,2,3,4]
b=(1,2,3)
str='Tomwenxing'
print(iter(a))  #<list_iterator object at 0x000001F4CFCDE208>
print(iter(b))  #<tuple_iterator object at 0x000001F4CFCDE208>
print(iter(str))  #<str_iterator object at 0x000001F4CFCDE208>


# 三、迭代器的方法

#iter.__next__()：返回迭代器的下一个元素，但没有下一个元素时抛出StopIteration异常

list=[1,2,3,4]
list=iter(list)
print(list.__next__())      #1
print(list.__next__())      #2
print(list.__next__())      #3
print(list.__next__())      #4


from collections import Iterable  #判断是否可迭代
from collections import Iterator  #判断是不是迭代器
##判断是否可迭代
print(isinstance([],Iterable))  #True
print(isinstance((),Iterable))  #True
print(isinstance({},Iterable))  #True
print(isinstance('',Iterable))  #True
##判断是不是迭代器
print(isinstance('',Iterator))  #False
print(isinstance('',Iterator))  #False
print(isinstance('',Iterator))  #False
print(isinstance('',Iterator))  #False

#isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。

# >>>a = 2
# >>> isinstance (a,int)
# True
# >>> isinstance (a,str)
# False
# >>> isinstance (a,(str,int,list))    # 是元组中的一个返回 True
# True
