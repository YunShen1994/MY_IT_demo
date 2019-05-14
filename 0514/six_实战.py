#  *_*  ：UTF-8 *_*
#来源    ：《python从入门到项目实践》
#开发时间 ：  2019/5/14 
#文件名称 ：six_实战.py
#开发工具 ：PyCharm

#任务一，解决“解决前年虫问题”
'''
    当前序列：[89,98,00,75,68,37,58,90]
    参考输出序列：[1989,1998,2000,1975,1968,1937,1958,1900]
'''
years = [89,98,00,75,68,37,58,90]
for     i   in  range(len(years)):
    if  years[i] != 00:
        years[i] +=1900
    else:
        years[i] = 2000
print(years)
#任务二 降序输出七家全国零售百强电商的销售额
''' 
    [58,12945,391,357,728,116,21086]
'''
sale = [58,12945,391,357,728,116,21086]
sale_dis = sorted(sale,reverse = True)
print(sale_dis)
#任务三 推算全国2018年全国零售百强电商销售额
sales = [int(x * 1.4 )  for   x     in  sale]
print(sales)
