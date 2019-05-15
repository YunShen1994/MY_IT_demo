#  *_*  ：UTF-8 *_*
#来源    ：《python从入门到项目实践》
#开发时间 ：  2019/5/14 
#文件名称 ：forth.py
#开发工具 ：PyCharm

#保留字的查看
import  keyword
print(keyword.kwlist)
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
  'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
  'with', 'yield']
'''

'''
标识符注意事项：
    1.只能由字母，数字，下划线组成，不能由数字开头
    2.不能使用保留字
    3.区分大小写
    4.以下划线开头的标识符具有特殊意义，如下：
        以单下划线开头的标识符表示不能直接访问的类属性
        以双下划线开头的标识符表示类的私有成员
        以双下换线开头和结尾的是Python里专用的标识，如__init__
        
注：尽量不要使用汉字作为标识符
'''
'''
变量的定义和使用：
    1.变量名必须是有效标识符
    2.变量名不能使用Python中的保留字
    3.慎用小写字母l和大写字母O
    4.应该选择有意义的标识符作为变量名
'''
myname = 505
print(type(myname))
print(id(myname))
#id()返回变量所指内存地址
print()
'''
基本数据类型：
    主要包括：整数，浮点型，复数
    整数：
    十进制：不能以0开头
    八进制：0-7，逢8进1，并以0O开头
    十六进制：0-9，A-F 以0x开头
    二进制：0-1
    浮点数：
    复数：
字符串类型：单引号，双引号，三引号
'''
print('''

         .----.
      _.'__    `. 
  .--(#)(##)---/#\\
.' @          /###\\
:         ,   #####
 `-..__.-' _.-\###/  
       `;_:    `"'
     .'"""""`. 
    /,  JOE  ,\\
   //  COOL!  \\\\
   `-._______.-'
   ___`. | .'___ 
  (______|______)''')
print('''
  .       .
  \`-"'"-'/
   } 6 6 {
  =.  Y  ,=
(""-'***`-"")
 `-/     \-'
  (  )-(  )===' 
   ""   ""  ''')
#So...搜狗输入法
print()
'''
布尔类型：True(1) False(0)
False 和 None：
    数值中的0，包括0，0.0，虚数0
    空序列：包括字符串，空元组，空列表，空字典
    自定义对象的实例，该对象的__bool__方法返回False，__len__方法返回0
'''

'''
数据类型转换：
hex()十六进制转换
oct()八进制
ord()整数转换为字符串
'''
eight_bit = 0O267
#print(type(eight_bit))
print(int(eight_bit))
six_bit = 0xe3ab
print(int(six_bit))
two_bit = 0b10110001
print(int(two_bit))
print()
print()
str_love = "我爱你一生一世"
fl_love = 521.1314
in_love = 5211314
print(str_love)
print(fl_love)
print(in_love)
print()
print()
print(chr(73)+chr(32)+chr(108)+chr(111)+chr(118)+chr(101)+chr(32)+chr(121)+chr(111)+chr(117)+chr(33))




####添加 修改  测试