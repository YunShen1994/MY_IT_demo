#  *_*  ：UTF-8 *_*
#来源    ：《python从入门到项目实践》
#开发时间 ：  2019/5/14 
#文件名称 ：five.py
#开发工具 ：PyCharm

#第五章：算术运算符
print("第五章：算术运算符")
print()
'''
+ - * / % //（取商的整数部分） **
优先级：
    第一级：**
    第二级：* / % //
    第三级：+-
'''
print("M"*10,"  "*10,)
print("   "*10,"@"*10)
print()
english = 92
python= 95
C = 89
sub = python - english
avg = (english + python + C) / 3
print("Python与英语的分数差："+str(sub))
print("平均成绩："+str(avg))
print()
'''
赋值运算符：
= += -= *= /= %= //= **=
比较运算符：
> < == >= <= !=
逻辑运算符：and （左到右）or（左到右） not（右到左）
'''
'''
位运算符：位与& 位或| 异位^ 取返~ 左移<< 右移>>
'''
'''
运算符优先级：
    **
    ~ +（正号）-（负号）
    * / % //
    << >>
    &
    ^
    |
    比较运算符
'''
print()
print("实战：")
print()
print(str(int(0b00010))+str(int(0b00000))+str(int(0b00010))+str(int(0b00000))+str(int(0b00001))+str(int(0b01010)))

first_num = input("输入第一个数字：")
second_num = input("输入第二个数字：")
third_num = input("输入第三个数字：")
#sum_nu = sum(int(first_num),int(second_num),int(third_num))
sum_num = int(first_num)+int(second_num)+int(third_num)
print(sum_num)
#print(sum_nu)



