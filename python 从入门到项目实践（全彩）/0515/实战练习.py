#  *_*  ：UTF-8 *_*
#来源    ：《python从入门到项目实践》
#开发时间 ：  2019/5/15    22:02 
#文件名称 ：实战练习.py
#开发工具 ：PyCharm

#任务一：模拟拼多多砍价
'''
    假设一个好友只能砍掉不超过商品销售价格十分之一的价钱
    小红要买意见4000元的商品，@小明帮忙砍价

'''
#任务二：判断是否买到康师傅假货


import  re
import  random
#任务一
sale = 4000
pattern_1 = r'@小明'
string = '小红要买意见4000元的商品，@小明帮忙砍价'
name = re.findall(pattern_1,string)
matchs = float(4000* 0.1)
match_demo = random.randrange(matchs)
print('小明只能最多砍价：',matchs)
print("此次小明砍价为：",match_demo)

#任务二
pattern_2  = r'康师傅R'
string = '康师傅'
match = re.findall(pattern_2,string)
if match :
    print(match)
else:
    print("此为盗品")
