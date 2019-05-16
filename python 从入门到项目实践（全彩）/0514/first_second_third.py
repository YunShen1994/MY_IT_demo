#  *_*  ：UTF-8 *_*
#来源    ：《python从入门到项目实践》
#开发时间 ：  2019/5/14 
#文件名称 ：first_second_third.py
#开发工具 ：PyCharm

#第一章：
import keyword
print(keyword.kwlist)

#第二章

#任务一
print("任务一：")
print("*****************************")
print("   想要满足用户需求吗？")
print("                 | ")
print("  — — — — — — — —  ")
print("| ea our own dog food  |")
print("  — — — — — — — —  ")

#任务二
print("任务二：")
print("**************************************************")
print("              大商电器商品仓库标签")
print("库号：        层号：         架号：          位号： ")
print("商品编号：                    商品名称：")
print("型号规格：                    计量单位：")
print("产       地：                    储备定额：")
#任务三 购物超市购物发票
print("任务三：")
print("")
print("操作员：1                       收据号：4370")
print("日期：2017-09-24 17:48   秤号：10414")
print("*****************************************")
print("商品名称：                                         ")
print("千克（个）         元/千克（个）        元")
print("*****************************************")
print("水晶梨（特价）                                   ")
print("           2.245             2.56              5.80")
print("*****************************************")
print("件数/商品数 1/1      合计：             5.80")
print("应付：                                          5.80")
print("现金：                                          5.80")
print("                         欢迎惠顾！                ")
#任务四
print("任务四：输出字符画史努比")
print()
print()
print("                                                       _ _ _ _                                       ")
print("                                                   .             .                                     ")
print("                                                 ,                 ,                                  ")
print("                                              _.  __                .                                 ")
print("                                        . --（$） （$$）---/#\\                            ")
print("                                    . ' @                      /###\\")
print("                                    :                     ，   #####")
print("                                    、—. .___.—    __.—\###/ '")
print("                                     ； __：")
print("                                          '  “    ”“   ”“ 、")
print("                                        .                                 .")
print("                                          /，            hi  ，      \\\\")
print("                                      /   /             你好！          \\\\")
print("                                      ’__  .  _____________  .  __  ’")
print("                                     ______ ' .        |       .  '______          ")
print("                                 ( _____________    |    _____________)")


print("--------------第三章--------------")
print()
print("print()函数的使用：")
import  datetime
print("当前年份："+str(datetime.datetime.now().year))
print("当前日期时间："+datetime.datetime.now().strftime('%y-%m-%d %H:-%M:-%S'))
print()
print("input()函数的使用")
#python.3x不管输入什么都是字符串类型，使用数字时需要转化
name = input("请输入字符：")
print(name + "的ASCII码为：",ord(name))
print()
print("根据当前年份计算多少岁：")
imyear = input("请输入您的出生年份：")
nowyear = datetime.datetime.now().year
age = nowyear - int(imyear)
print("您的年龄为："+str(age)+"岁")

if  age < 18:
    print("您现在为未成年人 ~@__@~")
if  age >= 18 and age < 66:
    print("您现在为年轻人 （-__-）")
if  age >= 66 and age < 80:
    print("您现在诶中年人 ~@__@~")
if  age >= 80:
    print("您现在为老年人 *-__-*")

print("输出字母、数字或符号的ASCII状态值：")
print()
str_demo = input("请输入一个字符：")
print()
print(str_demo,"的ASCII对应状态为：",ord(str_demo))


