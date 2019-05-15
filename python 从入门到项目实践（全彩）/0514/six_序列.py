#  *_*  ：UTF-8 *_*
#来源    ：《python从入门到项目实践》
#开发时间 ：  2019/5/14 
#文件名称 ：six_序列.py
#开发工具 ：PyCharm
#第六章 序列
print("第六章：")
print()
'''
    序列结构主要有列表，元组，集合，字符串
    
    索引：
        若使用负数索引，索引从-1开始，即最后一个元素，防止与第一个元素重合
'''
verson = ["圣安东尼奥马刺","洛杉矶湖人","修斯顿火箭","金州勇士"]
print(verson[2])
print(verson[-1])
print()
'''
    切片：sname[start:end:step]
            sname：序列名称
            start：切片开始的位置
            end：切片截止的位置
            step：切片的步长
'''
nba = ["迈克尔.乔丹","比尔.盖茨",
       "张三","李四","王五","赵六",
       "韩七","紫八","老九","第十"]
print(nba[1:5])#获取第二道第五个元素
print(nba[0:5:2])#获取1,3,5元素
print(nba[:])#赋值整个序列

print()
print("序列相加")
print()
nab2 = ["我是凑热闹的"]
print(nba+nab2)
'''
    相同的㤡是指：同为列表、元组、或者集合等
'''
'''
    乘法
'''
print()
print("乘法：")
phone= ["华为Mate 10","Vivo X21"]
print(phone * 3)
print()
'''
    检查某个元素是否是序列的成员
    语法：value in sequence
'''
print("王八" in nba)
print("韩七" in nba)
print()
print("计算序列的长度、最大值、最小值")
num = [7,14,21,28,35,42,49,56,63]
print("序列num的长度为：",len(num))
print("序列",num,"的最大数：",max(num))
print("序列",num,"的最小数：",min(num))
'''
    其它内置函数及其用途：
        list()：将序列转化为列表
        str()：将序列转化为字符串
        sum()：计算元素和
        sorted()：对元素进行排序
        reversed()：反向序列中的元素
        enumerate()：将序列组合为索引序列，多在for循环中
'''
print()