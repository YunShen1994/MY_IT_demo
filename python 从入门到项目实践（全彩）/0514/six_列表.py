#  *_*  ：UTF-8 *_*
#来源    ：《python从入门到项目实践》
#开发时间 ：  2019/5/14 
#文件名称 ：six_列表.py
#开发工具 ：PyCharm
#列表
'''
    列表在形式上 是放在[ ]中，相邻元素使用逗号分隔
'''

print("列表的创建和删除：")
'''
    列表的创建和删除：
        语法：listname = [element 1,element 2,element 3,....element n]
            创建空列表：emptylist[]
            创建数值列表：list(date)
                date为可以转换为列表的数据，类型可以是range对象，
                字符串，元组或者其他可迭代的数据      
'''
print()
str_demo = list(range(10,20,2))
print(str_demo)
print()
print("删除列表")
'''
    del listname
'''
team = ["皇家","罗马"]
print(team)
del  team
print()
print("访问列表元素：")
untitle = ["python",28,'人生苦短']
print(untitle)
print(untitle[2])
print()
print("遍历列表：")
'''
    语法格式：
        for item in listname
        #输出item  item用于保存获取得到的元素值
'''
print("2018年俄罗斯世界杯四强：")
team = ["法国","比利时","英格兰","克罗地亚"]
for  item in team:
    print(item)
'''
    使用for循环和enumerate()函数同事输出索引值和内容
'''
for index,item in enumerate(team):
     print(index + 1,item)
'''
    添加 修改 和删除列表元素
    语法：listname.append(obj)
    将一个列表中的所有元素添加到另一个列表中，使用extend()方法实现
        语法：listname.extend(seq)
        注：listname 为原列表，seq为要添加的列表，
        执行之后，将seq的内容追加到listname的后面
'''
phone = ["摩托罗拉","三星","诺基亚","OPPO"]
len(phone)
phone.append("iPhone")
len(phone)
print(phone)
print()
print("修改元素：")
verse = ['A','B','C']
print(verse)
verse[2] = 'D'
print(verse)
print()
print("删除元素：")
del     verse[-1]
print(verse)
print()
print("根据元素值删除元素：")
verse.remove('A')
print(verse)
team = ['A','B','C','D','E']
value = 'F'
if  team.count(value) > 0:
    team.remove(value)
print(team)
'''
    对列表进行统计计算
        语法：
                listname.count(obj)
                返回值 元素在列表中出现的次数
'''
player = ['A','b','C','A','E']
num = player.count('A')
print(num)
print()
'''
    获取指定元素首次出现的下标：
    语法：
        listname.index(obj)
        返回首次出现的索引值
'''
position = team.index('E')
print(position)
print()
'''
    统计列表中的元素和
    sum(iterable[,start])
    iterable：要统计的列表
    start：表示统计结果是从哪个位置开始，默认为0
'''
grade = [98,99,97,100,100,96,94,89,95,100]
total = sum(grade)
print("总成绩为：",total)
print()
'''
    对列表进行排序
    listname.sort(key = None,reverse = False)
    key：指定一个从每个列表元素中提取一个用于比较的键 
    key = str.lower  排序时不区分字母大小写
    Ture 表示降序 False 表示升序 默认升序
'''
print("原表：",grade)
grade.sort()
print("升序：",grade)
grade.sort(reverse=True)
print("降序：",grade)
print()
chars = ['cat','Tom','Angele','pet']
chars.sort()
print("区分分大小写字母：",chars)
chars.sort(key=str.lower)
print("不区分大小写字母：",chars)
print()
'''
    内置sorted
    sorted(iterable,key = None,reverse=False) 默认升序
'''
grade = [98,99,97,100,100,96,94,89,95,100]
grade_as = sorted(grade)
print("升序：",grade_as)
grade_des = sorted(grade,reverse=True)
print("降序：",grade_des)
print("原序列：",grade)
'''
    sort 与 sorted 区别：
        用法基本相同，sort会改变原序列的顺序，
        sorted会创建一个副本，副本为排序后的列表
'''
print()
'''
    列表推导式：
        1.：生成指定范围的数值列表：
        list = [expression for var in range]
        excepression：表达式，用于计算新列表的元素
        var :循环变量
        range：采用range()函数生成range对象
'''
import  random
ranndomnumber = [random.randint(10,100) for  i in range(10)]
print("生成的随机数为：",ranndomnumber)
print()
'''
    2.：根据列表生成指定需求的列表
    newlist = [Expression for var in list]
    var：值为后面列表每个元素值
    list：用于生成新列表的原列表
'''
print("全部商品打五折：")
price = [1200,5300,2988,6200,1988,8888]
sale = [int(x * 0.5) for x in price]
print("原价：",price)
print("打折后：",sale)
print()
'''
    3.：从列表中选择符合条件的元素组成新的列表
    newlist = [expression for  var in list if condiction]
'''
sale = [x for x in price if x > 5000]
print("原列表：",price)
print("价格高于5000：",sale)
print()