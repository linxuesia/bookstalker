## 什么是爬虫

## 学爬虫前的基础
### requests 网络请求库

### 正则表达式
python 内置的 re 模块，拥有一系列方法用于正则表达式匹配和替换，用于快速查找和匹配字符串。
参考地址： [http://www.runoob.com/python/python-reg-expressions.html]

### python open 方法操作文件
python 内置的 open 方法可以打开一个文件，并创建一个 file 对象，对其进行读写操作。
参考地址：[http://www.runoob.com/python/python-func-open.html]

### lxml 与 Xpath
XPath 是一门在 XML 文档中查找信息的语言。XPath 用于在 XML 文档中通过元素和属性进行导航，它使用路径表达式来选取 XML 文档上的节点，与系统中的文件路径类似。
lxml 类库是一个 Html/XML 的解析器，并且解析效率比较高。
文档链接：
Xpath - [http://www.w3school.com.cn/xpath/xpath_intro.asp]
lxml - [https://lxml.de/index.html]

### 多线程概念

## 练习 demo
从小说网站爬取聊斋志异全文的内容，并存储到一个 txt 文件中。
链接地址：[http://www.dushu369.com/gudianmingzhu/lzzy/]

思路：
* 分析章节链接的 html 构成
* 获取每章节的链接地址
* 访问每一章节，分析章节内容的 html 内容
* 新建一个文本文件，将每章节的文本写入

其他思考：
#### 通过打时间戳查看每个请求的耗时
#### 通过调整线程池的大小缩短爬虫时间



