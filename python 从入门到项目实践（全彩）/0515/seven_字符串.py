#  *_*  ：UTF-8 *_*
#来源    ：《python从入门到项目实践》
#开发时间 ：  2019/5/15 
#文件名称 ：seven_字符串.py
#开发工具 ：PyCharm
'''
    字符串的相拥操作：
        拼接字符串
'''
#拼接字符串
mot_en = 'Remember is a from of meeting.Frgetfulness is a from of freedom.'
mot_cat = "记忆是一种相遇。遗忘是一种自由"
print(mot_en +'——'+mot_cat)

print()

#链接不同类型的字符串
str1 = '今天我一共走了'
num = 12098
str2 = '步'
print(str1  + str(num ) +str2)
print()
#计算字符串长度 len(string)
str1 = '人生苦短，我用python!'
length = len(str1)
print(length)
'''
    默认情况下，通过len()函数计算字符串的长度时，
    不区分英文，数字和汉字，所以字符都认为是一个
    
    在实际开发中，有时需要获取字符串实际所占的字节数，
    即如果采用UTF-8编码，汉字占3个字节，才用GBK或者GB2312时，
    汉字占两个字节，这时，可以通过使用encode()方法进行编码后在进行获取
'''
#utf-8的字码长度
length_utf = len(str1.encode())
print(length_utf)
#gbk
length_gbk = len(str1.encode('gbk'))
print(length_gbk)
print()
#截取字符串
''' 
    切片方法 string[start:end:step]默认为1
    字符串的索引同序列的索引，都是从0开始的，并且
    每个字符占一个位置
'''
substr1 = str1[1]#截取第二个字符
substr2 = str1[5:]#从第六个字符开始截取
substr3 = str1[:5]#从左边尅是截取5个字符
substr4 = str1[2:5]#截取第三个到带五个字符
print('原字符串：',str1)
print(substr1+'\n'+substr2+'\n'+substr3+'\n'+substr4+'\n')
'''
    注：如果指定的索引不存在，则会跑出异常
    IndexError: string index out of range
'''
tr1 = '人生苦短，我用python!'
try:
    substr1= str1[15]
except  IndexError:
    print("指定索引不存在")

print()
#分隔字符串
''' 
    字符串对相关提供了分隔字符串的方法。
    分割字符串是把字符串分割为列表
    分割字符串可以看做是互逆操作
    str.split(sep,maxplit)
    str：要分割的字符串
    sep：用于指定分割符，可以包含多个字符，默认None，即
    所有的空字符（包括空格、换行\n、制表符\t）
    maxplit：可选参数，用于指定分割的次数，如果不指定或者为-1，
    则分割的次数没有限制，否则返回结果列表的元素个数最多为maxplit+1
    注：如果不指定sep参数，那么也不能指定maxplit参数
'''
str1 = '明 日 学 院 官 网   >>>   www.mingrisoft.com'
print("原字符串：",str1)
list1 = str1.split()#采用默认分隔符很行分割
list2 = str1.split('>>>')#用多个分隔符很行分割
list3 = str1.split('.')#用.分隔符很行分割
list4 = str1.split(' ',4)#用空格分隔符很行分割，并且分割前4个
print(str(list1)+'\n'+str(list2)+'\n'+str(list3)+'\n'+str(list4))
list5 = str1.split('>')#>进行分割
print(list5)
#检索字符串
'''
    count()方法：str.count(sub[,start[,end]])
    str：原字符串
    sub：百世要检索的字符串
    start：可选参数检索，表示检索范围的起始位置的索引，
    如果不指定，则从头开始索引
    end：可选参数，表示检索范围的结束位置的索引，如果不指定，
    则一直检索到结尾
'''
str1 = '@明日科技 @扎克伯格 @雷军'
print('字符串“',str1,'"中包括',str1.count('@'),'个@符号')
print()
#find()方法
''' 
    该方法用于检索是否包含指定的字符串，如果检索的字符串不存在，则返回-1
    否则返回出现该字符串时的索引
    str.find(sub[,start[,end]])
'''
print('字符串“',str1,'"中@符号首次出现的位置索引为：',str1.find ('@'))
'''
    如果只是想单纯的判断指定的字符串是否存在，可以使用int关键字实现。
    print(‘@' in str)
    如果存在就返回True，否则返回False
'''
print()
print('字符串“',str1,'"中*符号首次出现的位置索引为：',str1.find ('*'))
print()
'''
    index()方法
    同find()方法类似，也用于检索是否包含指定的子字符串。只不过如果使用index()
    方法，当指定的字符串不存在时就会抛出异常
    str.index(sub[,start[,end]])
    ValueError: substring not found
    还提供了rindex()方法，作用与index()方法类似，只是从右边开始
'''
print('字符串“',str1,'"中@符号首次出现的位置索引为：',str1.index('@'))
#print('字符串“',str1,'"中*符号首次出现的位置索引为：',str1.index ('*'))
print()
'''
    startswith()方法
    用于检索字符串是否以指定字符串开头。如果是则返回True,否则返回False
    str.startswith(prefix[,start[,end]])
    prefix要检索的字符串
'''
print()
print("------------------")
print("判断字符串“",str1,'"是否以@符号开头，结果为：',str1.startswith('@'))
print()
#endswith()方法
'''
    该方法用于检索字符串是否以指定字符串结尾。如果是返回Truue,
    否则返回False
    str.startswith(prefix[,start[,end]])
'''
