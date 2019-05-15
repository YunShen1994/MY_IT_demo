#  *_*  ：UTF-8 *_*
#来源    ：《python从入门到项目实践》
#开发时间 ：  2019/5/15    16:38 
#文件名称 ：seven_正则表达式.py
#开发工具 ：PyCharm
'''
    在处理字符串时，经常会有查找符合某些规则的字符串的需求，
    正则表达式就是用于描述这些规则的工具，换句话，正则表达式
    就是记录文本规则的代码

    例如DOS的用户   dir *.txt  简单的正则表达式
'''
#行定位符
'''
    用来描述子串的边界，^表示行的开始，$表示行的结尾
    ^tm
    该表达式表示要匹配字符串tm的开始位置是行头
    tm$
    匹配末尾
    tm 任意部分
'''
'''
    元字符：
    \b  \w
    \bmr\w*\b   匹配以字母mr开头的单词，先是从某个单词开始出（\b）
    然后匹配字母mr，接着是任意数量的字母或者数字（\w*）
    最后是单词结束处（\b}
'''
'''
    .：匹配除换行字符意外的任意字符
    \w：匹配字母，数字，下划线或者汉字
    \W：匹配除字母，数字，下划线或者汉字意外的字母
    \s：匹配当个的空字符（包括<Tab>键和换行符）
    \S：除单个空白字符（包括<Tab>键和换行符）以外的所有字符
    \d：匹配数字
    \b：匹配单词的开始或者结束，单词的分解符通常是空格、标点符号或者换行
    ^：匹配字符串的开始
    $：匹配字符串的结束
'''
'''
    限定符：
    (\w*)：匹配数字任意数量的字母或者数字
    ^\d{8}$：匹配8位QQ
'''
'''
    常用限定符：
    ？：匹配前面的字符零次 或者一次
    +：匹配前面的字符一次或者多次
    *：匹配前面的字符零次或者多次
    {n}:匹配前面的字符n次
    {n，}：匹配前面的字符最少n次
'''
'''
    字符类：
    查找数字和字母：\d  \w
    匹配没有预定义元字符的字符集合 比如原因字母  a e i o u
    [aeiou]
    [.?!]：匹配标点符号. ? !
    [0-9] 与\d含义完全一致
    [a-z0-9A-Z] 与\w一致
    如果想要匹配字符串中的任意一个汉字 [\u4e00-\u9fa5]
    如果匹配连续多个汉字，可以使用哪个[\u4e00-\u9fa5]+
'''
'''
    排除字符：
        [^a-z-Z]  匹配一个不是字母的字符
    选择字符：
    (^\d{15}$)\(^\d{18}$)\(^\d{17})(\d|X|x)$
    转义字符：
    [1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}
    括号在正则表达式中叶栓一个元字符
    分组：
    (six|four)th  表示：sixth 或 fourth
    如果匹配以字母m开头的单词的正则表达式转换为字符串模式，则不能直接在
    其两侧添加引号定界符
    错误：'\bm\w*\b'
    正确：'\\bm\\w*\\b'
    转换为原生字符串的形式
    r'\bm\w*\b'
    或者 R'\bm\w*\b'
'''
'''
    使用re模式实现正则表达式操作
    可以使用re模块提供的方法 search() match() findall()
    也可先试用re模块的compile()方法将模式字符串转换为正则表达式对象
    然后再使用该正则表达式对象的相关方法来操作字符串
    import re
'''
#匹配字符串
'''
    使用match()方法进行匹配
        用于从字符串的开始进行匹配，如果在其实位置匹配成功，
        则返回Match对象，否则返回None
        re.match(pattern,string,[flags])
        patten：表示模式字符串，由要匹配的正则表达式转换而来
        string：表示要匹配的字符串
        flags：可选参数，表示标志位，用于控制匹配方式，如是否区分字母大小写
        常年用的标志如下：
        A或者ASCII：对于\w \W \b \B \d \D \s \S 只进行ASCII匹配（仅适用于Python3.x）
        I或者IGNORECASE：执行不区分大小写的匹配
        M或者MULTINE：将^和$用于包括整个字符串的开始和结束的每一行，（默认情况下，
        仅适用于整个字符串的开始和结尾处）
        S或DOTALL：使用(.)字符匹配所有字符，包括换行符
        X或VERBOSE：忽略模式字符串中未转义的空格和注释
'''
#匹配字符串是否是以mr_开头，不区分大小写
import re
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.match(pattern,string,re.I)
print(match)
string = '项目名称MR_SHOP mr_shop'
match = re.match(pattern,string,re.I)
print(match)
'''
    match对象中包含了匹配值的位置和匹配数据。
    其中，要获取匹配值的其实位置的其实位置可以使用Match
    对象是start()方法；要获取匹配值得结束位置可以使用end()方法
    通过span()方法可以返回匹配位置的元组；通过string属性可以获取要
    匹配的字符串
'''
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.match(pattern,string,re.I)
print("匹配值的起始位置：",match.start())
print('匹配值得结束位置：',match.end())
print("匹配位置的元组：",match.span())
print('要匹配的字符串：',match.string)
print('匹配数据：',match.group())
'''
    使用search()方法进行匹配
    search()方法用于在整个字符串中搜索第一个匹配的值，如果匹配成功，
    则返回None
    re.search(pattern,string,[flags])
'''
match = re.search(pattern,string,re.I)
print(match)
string = '项目名称MR_SHOP mr_shop'
match = re.search(pattern,string,re.I)
print(match)
'''
    search 不仅仅是在字符串的其实位置进行搜索，其他位置有符合的匹配也可以
'''
'''
    使用findall()方法进行匹配
    用于字整个字符串中搜索左右符合正则表达式的字符串，并以列表的形式返回
    如果匹配成功，则返回包含匹配结构的列表，否则返回空列表
    re.findall(pattern,string,[flags])
'''
string = 'MR_SHOP mr_shop'
match = re.findall(pattern,string,re.I)
print(match)
string = '项目名称MR_SHOP mr_shop'
match = re.findall(pattern,string)
print(match)
#如果在指定的模式字符串中，包含分组，则返回与分组匹配的文本列表
pattern = r'[1-9]{1,3}(\.[0-9]{1,3}){3}'
str1 = '127.0.0.1 192.168.1.66'
match = re.findall(pattern,str1)
print(match)
print()
pattern = r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
str1 = '127.0.0.1 192.168.1.66'
match = re.findall(pattern,str1)
for iterm in match:
    print(iterm[0])
#替换字符串
print()
'''
    sub()
    re.sub(pattern,repl,string,count,flang)
    peal：表示替换的字符串
    string：表示要被查找替换的原始字符串
    count：可选参数，表示模式匹配后替换的最大次数，默认值为0，表示替换所有的匹配
    flags：可选参数，表示是标志位，用于控制匹配的方法，如是否区分字母大小写
'''
pattern = r'1[34578]\d{9}'
string = '中奖号码为：84978981 联系电话为：13611111111'
result = re.sub(pattern,'1XXXXXXXXXX',string)
print(result)
'''
     split()方法
     使用正则表达式分割字符串用于实现根据正则表达式分割的字符串，并以列表的形式进行返回
     其作用与字符串对象的split()方法类似，所不同的就是分割字符有模式字符串指定
     re.split(pattern,string,[maxsplit],[flags]
     string：表示要匹配的字符串
     maxsplit：可选参数，表示最大的拆分次数
     flags：可选参数，表示标志位，控制匹配方式，是否区分大小写
'''
print()
#从给定的URL地址中提取出请求地址和各个参数
pattern = r'[?|&]'#定义分割符
url = 'http://www.mingrisoft.com/login.jsp?username="mr"&pwd = "mrsoft"'
result = re.split(pattern,url)
print(result)