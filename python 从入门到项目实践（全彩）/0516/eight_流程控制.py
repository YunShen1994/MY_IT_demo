#  *_*  ：UTF-8 *_*
#来源    ：《python从入门到项目实践》
#开发时间 ：  2019/5/16    8:50 
#文件名称 ：eight_流程控制.py
#开发工具 ：PyCharm
'''
    程序结构：顺序，选择，循环
    选择 if  if……else if……elif……else
    使用if语句时，如果只有一条语句，语句块可以直接写到：的右侧
    if  a>b:max x=a
    但是为了代码的可读性，不建议这样做
'''
#if…else语句可以使用以下技巧：
a = -9
if a > 0:
    b = a
else:
    b = -a
print(b)

print("-----------------------------")
a = -9
b = a if a > 0 else -a
print(b)
'''
    if的嵌套循环
'''
'''
    使用and连接条件语句 同时满足多个条件
    也可用if嵌套替换
    使用or连接条件语句，满足多个条件中的一个
'''
print()
#使用not语句
data = None
if not data:
    print("You lost")
else:
    print("You win")
'''
    not与逻辑判断句if连用，代表not后面的表达式为False的时候，执行冒号后面的语句。
    在python中False、None、空字符串、空列表、孔子点、空元祖都相当于False
    if   x  is  None是最好的写法
'''
'''
    在python中，要判断特定的值是否存在列表中，可以使用关键字in
    判断特定的值不存在；列表中，可以使用哪个关键字not in
    例如，在密码输入时，输入非数字关键字均认为非法输入
'''
#实战练习

print("================================")
#任务一：王多余能继承百亿遗产吗
'''
    可以设置一个手动输入，输入王先生一个月花了多少钱，然后再判断王先生是否需有财产继承权
'''
'''
    一个月内花掉10亿，才能够继承财产
'''
spend = 1000000000
spend_real = 10000000
if spend_real > spend:
    print("恭喜王先生可以继承王老爷的财产！！！")
else:
    print("很抱歉，王先生没有财产继承权！！！")

print()
#任务二
print("========================================")
'''
    分标准计算打车费
    收费标准：
        起步里程为3公里，起步费10元；
        超过起步里程后10公里内，每公里2元；
        超过10公里以上的部分加收5%的回空补贴费，即每公里3元
'''
print("--------------------出租车计价器-----------------")
speed = float(input("请输入出租车行驶路程："))
play = 0
if speed < 3:
    play = 10
else:
    speed_real = speed -3
    if speed_real < 10:
        play = speed * 2
    else:
         speed_over = speed - 13
         play = 13 * 2 + speed_over * 3
#
print('您好，乘客，您的里程为：',speed,'公里,','实际计费为：',play,'元')
#print(play)
print("祝您旅途愉快，谢谢惠顾！")