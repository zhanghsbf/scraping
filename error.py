# 此写法用于处理获取url时可能发生的错误，以及使用bs对象时的AttributeError

from urllib.request import urlopen
from urllib.error import URLError,HTTPError
from bs4 import BeautifulSoup

# 第一种异常，网页在服务器上不存在，或者服务器不存在
try:
    html = urlopen(url)
except HTTPError as e:
    print(e)              # 捕获HTTPError，并打印出
else:
    pass                  # 当发生错误时，在except就中断了程序，不会运行else. else里的代码是程序正常运行时使用的
    
# 第二种异常，服务器不存在,结构同上，新增if判断
if html is None:
    print("URL is not found")     # url不存在或写错了时，会返回None
else:
    # 程序继续
    
# 第三种异常，成功返回 bsObj对象后，使用时想调用的标签不存在，就会返回None.再继续使用该标签属性时，就会出现AttributeError
try:
    content = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    print("Tag was not found")
else:
    if content == None:
        print("Tag was not found")
    else:
        print(content)

# 综合写法
def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle(url)
if title == None:
    print("Title could not be found")
else:
    print(title)
    
