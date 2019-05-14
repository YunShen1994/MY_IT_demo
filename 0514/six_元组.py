#  *_*  ：UTF-8 *_*
#来源    ：《python从入门到项目实践》
#开发时间 ：  2019/5/14 
#文件名称 ：six_元组.py
#开发工具 ：PyCharm
#元组
'''
    形式上放在( )中，元素之间用逗号隔开，元素类型可不同
'''
'''
    元组，列表的区别：
        主要区别：元组是不可改变序列，列表是可变序列。
        即元组中的元素不可以单独修改，而列表中的飚速可以任意修改
'''
'''
    元素的创建和删除
    创建：与列表类似
    如果要创建的彦祖只包括扩一个元素，则性需要在定义元组时，
    在元素的后面加一个逗号，若不加逗号，就会成为定义字符串
'''
vers1 = ("世界杯冠军",)
print(vers1)
print(type(vers1))
vers2 = ("世界杯冠军")
print(vers2)
print(type(vers2))
emptytuple = ()#创建空元组
'''
    tuple(data)
    data表示可以转化为元组的数据，
    其类型可以是range队形、字符串、元组或者其他可迭代类型的数据
'''
#创建一个10~20之间（不包括20）的偶数的元组
print()
two_n = tuple(range(10,20,2))
print(two_n)
#删除元组
del  two_n
#print(two_n)会报错
'''
    访问元组数据：
'''
untitle = ('python',28,('人生苦短','我用python'),['爬虫','云计算'])
print(untitle)
print(untitle[0])
print(untitle[:3])#输出元组中的前三个元素
#同列表 元组也可以用for循环进行遍历
'''
    修改元组元素，不可单独修改，可对元组重新赋值
'''
player = ('A','B','C','D','E','F','G')
player  =('X','Y','Z',)
print("新元素",player)
player1 = ('H','I')
player2 = player + player1
print("组合后：",player2)
'''
    元组推导式：同列表类似
'''
import  random
randomnum = (random.randint(10,100) for x in range(10))
print(randomnum)
''' 
    元组推导式生成的结果并不是一个元组或者列表，而是一个
    生成器对象，这一点和列表不同，需要使用该生成器对象可以
    将其转换为元组或者列表 其中，转换为元组需要使用tuple（）
    函数，转换为列表需要list（）函数
'''
randomnum = tuple(randomnum)
print(randomnum)
'''
    还可以直接通过for循环变量或者直接使用__next()__方法进行遍历
    在python2.x中，__next()__对应的方法为next()方法，也是用于
    遍历生成器的对象
'''
number = (i for i in range(3))
print(number.__next__())
print(number.__next__())
print(number.__next__())
number = tuple(number)
print("转化后：",number)
print()
number = (i for i in range(4))
for i in number:
    print(i,end = " ")
print(tuple(number))
#无论用那种方式，都要重新闯进一个生成器，
# 因为遍历后元生成器的对象已经不存在了
'''
    元组与列表的区别：
        都属于序列，都可以按照特定的顺序放一组元素，
        类型又不受限制
        区别：
            列表：在纸上用铅笔写字，错了还可以擦掉
            元组：在纸上用钢笔写字，错了只能换纸重新写
            1.列表属于可变序列，他的元素可以随时修改或者删除；
            而元组属于不可变序列，其中的元素不可以修改，除非整体替换
            2.列表可以用append()，extend()，insert()，remove()，pop()，
            等方法实现添加和修改列表元素，而元组没有这几个方法，
            因为不能同时向元组中添加和修改元素，同样也不能删除元素
            3.列表可以使用切片访问和修改列表中的元素；元组也支持切片，
            但是它只支持通过切片访问元组中的元素，不支持修改
            4.元组比列表的访问和处理速度快，所以只需对其中的与只能
            进行访问，而不进行任何修改，建议使用元组
            5.列表不能作为字典键，而元组却可以
'''
print()