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
    该方法用于检索字符串是否以指定字符串结尾。如果是返回True,
    否则返回False
    str.startswith(suffix[,start[,end]])
'''
str1 = 'http://www.mingrisoft.com'
print("判断字符串“",str1,'"是否以.com符号结尾，结果为：',str1.endswith('.com'))
#字母的大小写转换
'''
    lower() upper()大小  小大
    str.low() str.upper()
'''
print()
str1 = 'HTTP://WWW.MingRisoft.com'
print("原字符串：",str1)
print('新的字符串：',str1.lower())#转化为小写
print('新的字符串：',str1.upper())
#去除字符串中的空格和特殊字符
'''
    strip()去除字符串左右两边的空格和特殊字符，
    也可使用lstrip()方法 左边
    rstrip()方法 右边
    特殊字符 是指制表符'\t',回车符,'\r',换行符,'\n'
    str.strip([chars]) chars可选参数
'''
str1= 'http://www.mingrisoft.com   \t\n\r'
print('原字符串str1：'+ str1 +'。')
print("新字符串："+str1.strip()+'。')#去除收尾的空格和特殊字符
str2 = "@明日科技.@."
print('原字符串str2：'+str2+'。')
print('新字符串：'+str2.strip('@.')+'。')
print()
str1 = '\t  http://www.mingrisoft.com '
print('原字符串str：'+str1+'。')
print('字符串：' + str1.lstrip()+'。')
str2 = '@明日科技'
print('原字符串str2：'+ str2+'。')
print('新字符串：'+str2.lstrip('@')+'。')
#rstrip类似
print()
#格式化字符串
'''
    格式化字符串是指先制定一个模板，在这个模板中留几个空位，
    然后再根据需要填上相应的内容。这些空位需要指定的符号标记（占位符）
    而这些符号还不会显出来
    python中，格式化字符串有两种方法
    1.使用%操作费
    '%[-][+][0][m][.n]格式化字符串'%exp
    都为可选参数
    -：指定左对齐 正无符号，负数前加符号
    +：指定右对齐
    0：右对齐 用0填充空白（一般与m参数一起使用）
    m：表示占有宽度
    .n：表示小数点后保留的位数
    exp：要转换的项 多个元组，不能使用列表
    
    常用的格式化字符：
    %s：字符串 str（）
    %c：单个字符
    %r：字符串 repr()
    %o：八进制
    %d/%i：十进制整数
    %f/%F：浮点数
    %x：十六进制
    %E：指数 基地E
    %：except
    %% 字符%
'''
#格式化输出一个保存公司信息的字符串
template = '%09d\t公司名称： %s \t官网：  http:www.%s.com'
context1 = (7,'百度\t\t','baidu')
context2 = (8,"明日学院",'mongrisoft')
print(template%context1)
print(template%context2)
'''
    使用字符串对象的format()方法
    str.format(args)
    str：用于指定指定字符串的显示样式（模板）
    args：用于指定要转换的项  多项 逗号分隔
    创建模板时，需要使用{}he :指定占位符，基本语法：
    {[index][:[[fill]align][sign][#][width][.precision][type]]}
    参数说明：
    index ：用于指定要设置格式的对象在参数列表中的索引位置
    索引值从0开始，如果省略，则根据值得信后顺序自动分配
    fill：用于指定空白处填充的字符
    align（配合width一起使用）：用于指定对齐方式 <左对齐 >右对齐
    =内容右对齐，且支队数字类型有效
    ^内容居中
    sign：用于指定有无符号数（值为+表示整数加+，负数加-；值为“-”表示整数不变，
    负数加负号，值为空格表示加空格，负数加负号）
    #：对于二进制，八进制，和十六进制，如果加上#，表示会显示‘0b/0o/0x’前缀，
    否则不显示前缀
    width：用于指定所占宽度
    .precision：用于指定保留的小数位置
    type：用于指定类型
'''
'''
    formcat()方法中常用的格式化字符
    s：对字符串类型格式化
    b：将十进制整数自动转换为二进制表示再格式化
    d：十进制整数
    c：将十进制整数自动转换成对应的Unicode字符
    x或者X：将十进制整数自动转化成十六进制表示再格式化
    e或者E：转换为科学计数法表示再格式化
    f或者F：转化为浮点数（默认小数点后保留6位再格式化）
    g或者G：自动在e和f或者E和F中切换
    %：显示百分比（默认显示小数后6位）
    
    当一个模板中出现多个占位符时，指定索引位置的规范需统一
'''
template = '编号：{:0>9s}\t公司名称：    {:s}    \t官网：   http://www.{:s}.com'
context1 = template.format('7','百度\t','baidu')
context2 = template.format('8','明日学院','mingrisoft')
print(context1)
print(context2)