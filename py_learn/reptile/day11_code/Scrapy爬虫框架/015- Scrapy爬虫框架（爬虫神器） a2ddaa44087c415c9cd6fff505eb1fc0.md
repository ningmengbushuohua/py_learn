# 015- Scrapy爬虫框架（爬虫神器）

## 一、Scrapy 框架介绍

Scrapy 是一个基于Python开发的爬虫框架，用于从网站中抓取结构化的数据。可以说它是当前Python爬虫领域中最流行的爬虫框架，该框架提供了非常多爬虫相关的基础组件，架构清晰，可拓展性强。基于Scrapy，我们可以灵活高效的完成各种爬虫需求。

### 1.简介

在接触Scrapy之前，我们实现的爬虫无非是基于 requests 或者 aiohttp 的。在整个编写爬虫的过程中，我们需要实现很多的操作，例如网站请求、数据解析、数据存储等，写爬虫的老手看到这些操作顿感头大，因为这些操作很多都是通用的或者重复的。所以我们完全能够将每一部分抽离出来，将其做成通用的一块块积木，这样每次写爬虫时，只需要从现有的积木中获取对应的功能模块，再结合一些特定的代码就能够实现完整的爬取流程了。比如有一个积木的功能固定的就是在遇到404状态码时直接跳过页面，遇到403状态码时发起重试等，那么这个功能在被需要的时候此积木就可以直接拿过来使用，没必要将这个功能再编写一遍，既浪费时间又浪费成本。

框架就是从这样的思想中诞生出来的，经过时间的沉淀，趋于完美和强大。Scrapy便是其中之一，Scrapy框架几乎是Python爬虫学习和工作中必须要掌握的框架，需要好好的钻研。

### 2.安装

使用pip命令即可安装 Scrapy。

Windows使用**`pip install scrapy`**

Mac/Linux使用**`pip3 install scrapy`**

### 3.创建项目

在终端中使用命令**`scrapy startproject 项目名`**创建Scrapy爬虫项目，项目名要当成变量名进行命名。

例如，我要爬取中国新闻网，我先创建中国新闻网的Scrapy爬虫项目，如图所示输入**`scrapy startproject chinaNews`**，得到如下结果。

![Untitled](015-%20Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%EF%BC%88%E7%88%AC%E8%99%AB%E7%A5%9E%E5%99%A8%EF%BC%89%20a2ddaa44087c415c9cd6fff505eb1fc0/Untitled.png)

你可以根据提示使用**`cd chinaNews`**命令进入项目内，然后通过执行**`scrapy genspider NewsSpider https://www.chinanews.com/`**命令创建爬虫文件。此处的**`NewsSpider`**为爬虫文件名，对应上方示例的example；`**https://www.chinanews.com/**`为被爬网站的域名，对应上方示例的example.com。

![Untitled](015-%20Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%EF%BC%88%E7%88%AC%E8%99%AB%E7%A5%9E%E5%99%A8%EF%BC%89%20a2ddaa44087c415c9cd6fff505eb1fc0/Untitled%201.png)

此时的Scrapy爬虫项目初步建立完成，这个Scrapy项目的目录结构如下：

```
scrapy.cfg
chinaNews/
    __init__.py
    items.py
    middlewares.py
    pipelines.py
    settings.py
    spiders/
        __init__.py
        NewsSpiders.py
```

### 4.运行项目

先来看NewsSpider文件的代码，默认代码是这样的：

```python
import scrapy

class NewsspidersSpider(scrapy.Spider):
    name = 'NewsSpiders'
    allowed_domains = ['www.chinanews.com']
    start_urls = ['http://www.chinanews.com/']

    def parse(self, response):
        pass
```

上述代码中，我们发现Scrapy框架完全就是面向对象的应用了，毕竟是框架，所以不能和我们平时写的代码相比较。

其中，变量**`name`**的值就是这个爬虫的名字，运行这个项目时需要使用到的值；

**`allowed_domains`**是允许爬虫访问的域名，因为我们是针对某一网站创建的爬虫文件，所以这个爬虫只能访问指定的域名；

**`start_urls`**表示爬虫开始执行时访问的网站；

**`parse方法`**是在start_urls后开始执行的方法，其中的**`response参数`**是一个对象，其相当于**`requests.get()`**或者**`urllib.requests.urlopen()`**得到的结果，即相当于对start_urls中的链接请求完后得到的响应结果。

接下来我们修改下代码，然后执行。

```python
import scrapy

class NewsspidersSpider(scrapy.Spider):
    name = 'NewsSpiders'
    allowed_domains = ['www.chinanews.com']
    start_urls = ['http://www.chinanews.com/']

    def parse(self, response):
        print(response)
```

将**`pass`**改为**`print(response)`**，我们来打印下响应结果。

在终端中，使用命令**`scrapy crawl NewsSipders`**进行项目执行。结果如下，红框位置便是打印出来的结果，我们看到打印出来的是**`状态码`**和**`请求的网址`**。

![image.png](015-%20Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%EF%BC%88%E7%88%AC%E8%99%AB%E7%A5%9E%E5%99%A8%EF%BC%89%20a2ddaa44087c415c9cd6fff505eb1fc0/image.png)

### 5. 项目执行流程

项目执行以后，我根本没有写请求网址的代码，在执行程序以后，它怎么就自己实现了对应功能呢，并且这个项目是以什么样子的流程执行的，就需要我们仔细钻研。

![scrapy_architecture.png](015-%20Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%EF%BC%88%E7%88%AC%E8%99%AB%E7%A5%9E%E5%99%A8%EF%BC%89%20a2ddaa44087c415c9cd6fff505eb1fc0/scrapy_architecture.png)

上面这张图是Scrapy框架的执行流程图，大家可以按照序号标号来分析。

**Scrapy主要包括以下组件：**

- 引擎（Engine）：用来处理整个系统的数据流处理，触发事务（框架核心）。
- 爬虫（Spiders）：爬虫是主要干活的，用于从特定的网页中提取自己需要的信息，即所谓的实体（Item）。用户也可以从中提取出链接，让Scrapy继续抓取下一个页面。
- 调度器（Scheduler）：用来接受引擎发过来的请求, 压入队列中, 并在引擎再次请求的时候返回，可以想像成一个URL（被抓取网页的网址或者链接）的优先队列，由它来决定下一个要抓取的网址是什么，同时去除重复的网址。
- 下载器（Downloader）：用于下载网页内容, 并将网页内容返回给蜘蛛(Scrapy下载器是建立在twisted这个高效的异步模型上的)。
- 项目管道（Pipeline）：负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。
- 下载器中间件（Downloader Middleware）：位于Scrapy引擎和下载器之间的框架，主要是处理Scrapy引擎与下载器之间的请求及响应。
- 爬虫中间件（Spider Middleware）：介于Scrapy引擎和爬虫之间的框架，主要工作是处理蜘蛛的响应输入和请求输出。

**Scrapy执行流程如下：**

步骤一：引擎从蜘蛛那里获得初始的爬行请求。

步骤二：该引擎在调度器中调度请求，并要求对下一个请求进行爬取。

步骤三：调度器将下一个请求返回给引擎。

步骤四：引擎通过下载器中间件向下载器发送请求。

步骤五：页面下载完成后，下载器会生成一个响应(包含该页面)，并通过下载器中间件将其发送给引擎。

步骤六：引擎从下载器接收响应，并通过蜘蛛中间件将其发送给蜘蛛进行处理。

步骤七：蜘蛛处理响应，并通过蜘蛛中间件将抓取的项目和新请求(随后)返回给引擎。

步骤八：引擎将已处理的项目发送到项目管道，然后将已处理的请求发送到调度程序。

步骤九：重复该过程(从步骤三开始)，直到不再有来自调度程序的请求。

简单了解了Scrapy以后，我们详细的研究下Scrapy框架。

---

## 二、中国新闻网爬虫

刚刚我们已经创建了中国新闻网的爬虫项目，接下来，我们就继续上述代码的完善。

### 1.是否遵循robots协议

我们在开始学习爬虫时，介绍了一个**`robots协议`**，在Scrapy中，默认是遵循robots协议的，但是你也可以选择不遵循，当然，这就需要看要求了，我们就暂时先选择不遵循。此时只需要对**`settings.py`**进行简单修改即可，**`settings.py`**是Scrapy的配置文件，允许你自定义所有 Scrapy 组件的行为，包括核心、扩展、管道和蜘蛛本身。此时，只需要在**`settings.py`**中，将`**ROBOTSTXT_OBEY = True**`改为**`False`**即可不遵循robots协议。

![Untitled](015-%20Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%EF%BC%88%E7%88%AC%E8%99%AB%E7%A5%9E%E5%99%A8%EF%BC%89%20a2ddaa44087c415c9cd6fff505eb1fc0/Untitled%202.png)

### 2.“即时新闻”链接抓取、构造

我要爬取《中国新闻网》的“即时新闻”部分，那么我就得找到其入口。

![Untitled](015-%20Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%EF%BC%88%E7%88%AC%E8%99%AB%E7%A5%9E%E5%99%A8%EF%BC%89%20a2ddaa44087c415c9cd6fff505eb1fc0/Untitled%203.png)

![Untitled](015-%20Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%EF%BC%88%E7%88%AC%E8%99%AB%E7%A5%9E%E5%99%A8%EF%BC%89%20a2ddaa44087c415c9cd6fff505eb1fc0/Untitled%204.png)

如图，找到入口后复制其selector，在我们创建的NewsSpider.py文件的parse方法中这样去写

```python
import scrapy
import re

class NewsspidersSpider(scrapy.Spider):
    name = 'NewsSpiders'
    allowed_domains = ['www.chinanews.com']
    start_urls = ['http://www.chinanews.com/']

    def parse(self, response):
        href = response.css(
            'body > div:nth-child(9) > div.news-right > div.top-jsxw > div.jsxw-title.lmtitle > a::attr(href)'
        ).get()  # 结果为： /scroll-news/news1.html
        for page in range(1, 11):
            link = self.start_urls[0] + re.sub(r'\d', str(page), href[1:])
            # http://www.chinanews.com/scroll-news/news1.html
						# print(link)
            yield scrapy.Request(url=link, callback=self.NewsInfo)

    def NewsInfo(self, response):
        pass
```

- 借助已经取得的主页面的 response，通过CSS选择器提取入口处的 URL，标签内属性值提取要使用 **`::attr(属性名)`** 的形式，最后使用 scrapy 中的 get方法 以字符串形式返回选择器找到的第一个项。
- 得到的结果为**`/scroll-news/news1.html`**，根据观察发现即时新闻页面一共只有10页，我们通过 URL 的规律进行 URL 构建。
- 根据类属性中的start_ urls及上方结果构建URL，其中使用了re模块中的 sub方法 进行页数的替换。
- 最终使用 yield 以及 scrapy.Requests，根据此10个页面的 URL 将 response 再次传递给新创建的 NewsInfo方法。
- 注意：回调函数**`callback`**
    
    此处涉及到一个回调函数的知识点，当程序运行时，一般情况下，应用程序会通过API调用库里预先备好的函数。但是有些库函数却要求应用先传给它一个函数，好在合适的时候调用，以完成目标任务。**这个提前被传入的、后又被调用的函数就称为回调函数（callback function）**。
    

![Untitled](015-%20Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%EF%BC%88%E7%88%AC%E8%99%AB%E7%A5%9E%E5%99%A8%EF%BC%89%20a2ddaa44087c415c9cd6fff505eb1fc0/Untitled%205.png)

可以选择将**`print(link)`**反注释，`**yield scrapy.Request(url=link, callback=self.NewsInfo)**`注释掉，执行命令**`scrapy crawl NewsSpiders`**，查看运行结果，能够发现我们不但将即时新闻的入口链接抓取出来了，并且还将这十页的链接构造出来了。

### 3.每页新闻信息爬取

```python
# css选择器版本
def NewsInfo(self, response):
    liList = response.css(
        'body > div.w1280.mt20 > div.content-left > div.content_list > ul > li'
    )
    for li in liList:
        newsItem = ChinanewsItem()
        if li.css('li::attr(class)').get() != 'nocontent':
            # 新闻类型
            newsItem['NewsType'] = li.css('li > div.dd_lm > a::text').get()
            # 新闻标题
            newsItem['NewsTitle'] = li.css('li > div.dd_bt > a::text').get()
            # 新闻链接
            href = li.css('li > div.dd_bt > a::attr(href)').get()
            newsItem['NewsHref'] = self.start_urls[0] + href[1:]
            # 新闻发布时间
            newsItem['NewsTime'] = li.css('li > div.dd_time::text').get()
            yield newsItem

# XPath版本
# def NewsInfo(self, response):
#     liList = response.xpath('./body/div[@class="w1280 mt20"]/div[@class="content-left"]/div[2]//li')
#     for li in liList:
#         newsItem = ChinanewsItem()
#         if li.xpath('./@class').get() != 'nocontent':
#             # 新闻类型
#             newsItem['NewsType'] = li.xpath('./div[1]/a/text()').get()
#             # 新闻标题
#             newsItem['NewsTitle'] = li.xpath('./div[2]/a/text()').get()
#             # 新闻链接
#             href = li.xpath('./div[2]/a/@href').get()
#             newsItem['NewsHref'] = self.start_urls[0] + href[1:]
#             # 新闻发布时间
#             newsItem['NewsTime'] = li.xpath('./div[3]/text()').get()
#             yield newsItem
```

![Untitled](015-%20Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%EF%BC%88%E7%88%AC%E8%99%AB%E7%A5%9E%E5%99%A8%EF%BC%89%20a2ddaa44087c415c9cd6fff505eb1fc0/Untitled%206.png)

**对`NewsInfo方法`拓充：**

此处的response对象已经是对即时新闻每页链接请求后的响应结果，然后按部就班的将**新闻类型**、**新闻标题**、**新闻链接**、**新闻发布时间**抓取即可。

**此处还需注意：**

- 在scrapy中，像正则、css选择器、XPath都可以使用。
- 如果要使用css选择器，需要将css选择器写在css方法中。如果要使用XPath，直接将路径表达式写到xpath方法中即可。
- 在css方法中写css选择器使用**`::text`**提取标签下的内容，使用**`::attrs(属性名)`**提取标签内指定属性名对应的属性值。在xpath方法中正常写路径选择器即可。
- 使用**`get方法`**以字符串形式返回选择器找到的第一个项，还一个**`getall方法`**始终返回选择器找到的所有项的列表合集。

上述代码中，还有**`newsItem = ChinanewsItem()`**、**`newsItem['NewsType']`**、**`newsItem['NewsTitle']`**、**`newsItem['NewsHref']`**、**`newsItem['NewsTime']`**需要再给大家解释一下，scrapy中要求抓取到的数据要保存到一个字典对象中，我们这里相当于在将数据填写到这个字典对象中，请看下方代码。

---

我们针对**`items.py`**文件进行编辑：

```python
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ChinanewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    NewsType = scrapy.Field()
    NewsTitle = scrapy.Field()
    NewsHref = scrapy.Field()
    NewsTime = scrapy.Field()
```

爬虫的主要目标就是需要从非结构化的数据源中提取出结构化的数据，那么Items在其中就起到关键的作用。一般情况下，我们提取到数据都是放在一个字典中，虽然字典好用，但是缺少结构性的东西，比如说容易打错字段名称，从而容易出错。Scrapy提供了Item类，这些Item类可以指定字段。比方说在这个Scrapy爬虫项目中，定义了一个Item类，这个Item里边包含了name、age、year等字段，这样可以把爬取过来的内容通过Item类进行实例化，这样就不容易出错了。

就比如这里，我们在此处定义了NewsType、NewsTitle、NewsHref、NewsTime字段，只需要在前一处抓取数据的代码中，实例化此处的**`ChinanewsItem类`**，然后将对应的数据赋予给对应的字段，即可实现数据的结构化，结果如图：

![Untitled](015-%20Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%EF%BC%88%E7%88%AC%E8%99%AB%E7%A5%9E%E5%99%A8%EF%BC%89%20a2ddaa44087c415c9cd6fff505eb1fc0/Untitled%207.png)

### 4.设置多线程

scrapy默认是开始多线程模式的，在**`settings.py`**配置项文件中，有这样一句话`Configure maximum concurrent requests performed by Scrapy (default: 16)`，也就是说scrapy默认是16线程，当然可以将下方的代码反注释掉，随意的修改指定的线程数，比如改为单线程：

```python
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1
```

### 5.数据存储

数据存储，其实就是我们常说的数据持久化，爬虫爬下来的数据终究是需要保存的。我们有这么两种方案进行数据的存储：

- 使用Scrapy的Exporter组件利用指定的命令进行数据导出
- 自建管道，进行文件存储代码的编写

我们先来看第一种方式，Scrapy提供了这样一条命令进行数据的存储：`scrapy crawl 爬虫名字 -o 文件名.后缀名`或者`scrapy crawl 爬虫名字 --output 文件名.后缀名`

**注意：**scrapy只提供了对json、jsonlines、jsonl、jl、csv、xml、marshal、pickle这八种文件格式的支持，所以如果有其他需求，请看第二种方式。

**演示一下：**在终端输入`scrapy crawl NewsSpiders -o data.csv`，程序执行完以后就可以看到目录下出现了`data.csv`文件，里面包含了你想要的数据。

再来看下第二种方式，通过自建管道Pipeline对数据进行存储，前文我们在Scrapy流程图中说过，管道就是为了处理爬虫从网页中抽离出的实体而存在的，数据转化为Item以后，会传递到Item Pipeline做进一步的处理，比如：清洗数据、数据去重、数据存储等。

去**`pipeline.py`**文件中编写存储数据的代码，该文件中原本是这些内容：

```python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class ChinanewsPipeline:
    def process_item(self, item, spider):
        return item
```

首先先打开注释中的链接*`https://docs.scrapy.org/en/latest/topics/item-pipeline.html`*，弄懂教程是关键，必要时使用翻译。Scrapy官方文章中介绍说，每个项目管道组件都是一个类，这个类中存在四个方法，分别是**`process_item`**、**`open_spider`**、**`close_spider`**、**`from_crawler`**，这些方法并不是必须都要写的，选择合适的情况写入即可。那么这四个方法分别有什么作用呢？

**`open_spider(self, spider)`**：运行爬虫时调用此方法，spider参数会自动指向目前运行的爬虫。

`**close_spider(self, spider)**`：关闭爬虫时调用此方法，spider参数会自动指向运行结束的爬虫。

`**process_item(self, item, spider)**`：爬虫执行时进一步处理数据的方法，item参数代表的就是**`item.py`**文件中Item类中的数据，spider参数指向当前爬虫。

`**from_crawler(cls, crawler)**`：这个方法是个类方法，可用于爬虫开始执行时数据处理的一些初始化参数。

1. 例如，将数据存储到Excel文件中，自己新建一个**`ChinanewsToExcelPipline`**类，表示在这个类中实现写入Excel的操作（当然，也可以在已存在的ChinanewsPipline类中编写）。
    
    ```python
    class ChinanewsToExcelPipline:
        """
        将数据写入Excel文件
        """
        def open_spider(self, spider):
            self.workbook = openpyxl.Workbook()
            colName = ['newsType', 'newsTitle', 'newsHref', 'newsTime']
            for i in range(len(colName)):
                self.workbook['Sheet'].cell(1, i + 1).value = colName[i]
    
        def close_spider(self, spider):
            self.workbook.save('./data.xlsx')
    
        def process_item(self, item, spider):
            newsType = item['NewsType']
            newsTitle = item['NewsTitle']
            newsHref = item['NewsHref']
            newsTime = item['NewsTime']
            dataList = [newsType, newsTitle, newsHref, newsTime]
            rowIndex = self.workbook['Sheet'].max_row
            colIndex = 1
            for i in range(len(dataList)):
                self.workbook['Sheet'].cell(rowIndex + 1, colIndex).value = dataList[i]
                colIndex += 1
    
            return item
    ```
    
    记得在**`settings.py`**配置文件中将`Configure item pipelines`处配置项反注释，然后将刚才新建的**`ChinanewsToExcelPipline`**类写入到字典中，并且提供一个权重数值，这个数值在0～1000范围内即可，数值越小，优先级越高。
    
    ```python
    # Configure item pipelines
    # See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
    ITEM_PIPELINES = {
        # 'chinaNews.pipelines.ChinanewsPipeline': 300,
        'chinaNews.pipelines.ChinanewsToExcelPipeline': 300
    }
    ```
    
2. 或者，将数据写入MySQL数据库中。
    
    先从**`settings.py`**文件中添加数据库的相关参数
    
    ```python
    # MySQL config info
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306
    DB_USER = '数据库用户名'
    DB_PASS = '数据库密码'
    DB_NAME = '数据库名'
    ```
    
    再按照你需要爬取的信息，从数据库中创建数据表及对应的字段（创建数据库表的SQL不唯一）
    
    ```sql
    create database `News`;
    
    use News;
    
    create table `tb_News`(
    	`NewsType` varchar(10),
    	`NewsTitle` varchar(255),
    	`NewsLink` varchar(100),
    	`NewsTime` varchar(20)
    );
    ```
    
    再新建一个`**ChinanewsToMySQLPipeline**`类，表示在这个类中实现写入MySQL的操作。
    
    ```python
    class ChinanewsToMySQLPipeline:
        """
        将数据写入MySQL
        """
    
        @classmethod
        def from_crawler(cls, crawler):
            host = crawler.settings['DB_HOST']
            port = crawler.settings['DB_PORT']
            username = crawler.settings['DB_USER']
            password = crawler.settings['DB_PASS']
            database = crawler.settings['DB_NAME']
            return cls(host, port, username, password, database)
    
        def __init__(self, host, port, username, password, database):
            self.conn = pymysql.connect(host=host, port=port,
                                        user=username, password=password,
                                        database=database, charset='utf8mb4',
                                        autocommit=True)
            self.cursor = self.conn.cursor()
    
        def open_spider(self, spider):
            pass
    
        def close_spider(self, spider):
            self.conn.close()
    
        def process_item(self, item, spider):
            newsType = item['NewsType']
            newsTitle = item['NewsTitle']
            newsHref = item['NewsHref']
            newsTime = item['NewsTime']
            self.cursor.execute(
                'insert into `tb_news` '
                '(`NewsType`, `NewsTitle`, `NewsLink`, `NewsTime`) '
                'values (%s, %s, %s, %s)',
                (newsType, newsTitle, newsHref, newsTime)
            )
            return item
    ```
    
    同样的，记得在**`settings.py`**配置文件中将`Configure item pipelines`处配置项反注释，然后将刚才新建的`**ChinanewsToMySQLPipeline**`类写入到字典中，并且提供一个权重数值，这个数值在0～1000范围内即可，数值越小，优先级越高。
    
    ```python
    # Configure item pipelines
    # See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
    ITEM_PIPELINES = {
        # 'chinaNews.pipelines.ChinanewsPipeline': 300,
        'chinaNews.pipelines.ChinanewsToExcelPipeline': 100,
        'chinaNews.pipelines.ChinanewsToMySQLPipeline': 200
    }
    ```
    

### 6.User-Agent下载中间件设置

在scrapy框架中，中间件（Middleware）是一个非常重要的组件，scrapy框架的中间件主要有两个，一个是spiderMiddleware(爬虫中间件)，一个是DownloaderMiddleware(下载中间件)。通常我们要处理的是请求对象和响应对象数据，这些操作在下载中间件中就能处理好，所以一般不会去使用爬虫中间件，因此我们首先来看一下DownloaderMiddleware(下载中间件)。

下载中间件的作用就是：

1. 引擎将request对象交给下载器之前，会经过下载器中间件。此时，下载中间件提供了一个方法 process_request，可以对request对象进行设置请求头、IP代理、Cookie等；
2. 当下载器完成下载后，获得到response对象，将它交给引擎的过程中，再一次经过下载中间件。下载中间件提供了另一个方法 process_response，可以判断response对象的状态码，来决定是否将response提交给引擎。
3. 当下载器或process_reqeust抛出异常时，scrapy调用process_exception，我们可以在process_exception中编写代码来处理这些异常。

我们本次进行随机User-Agent的设置，先来说明为什么要设置随机UA，前面我们说过有些网站会有封IP的手段，当你访问这个网站时，你的IP地址是被记录下来的，如果被发现短时间、高频次访问网站的行为，就会面临被当作爬虫对待的风险。当然，有些网站检测爬虫的手段还会更精确一些，例如检测UA，UA里面是包含了操作系统、浏览器、CPU等信息的，如果短时间发现同一个UA频繁出现，就再去有针对性的查看对应的IP地址。所以此时，我们可以通过随时更改UA的方式，躲过某些网站的检测，来降低被反爬的风险。

此处有一个文件，是我根据比较知名的UA随机模块fake-useragent提取出来的可用的UA，大家可以自行下载，如果没办法下载，大家可以通过打开的网页，手动复制其中的内容，自行写入txt文本文件。最后，请将此文件放入到scrapy项目的与**`scrapy.cfg`**同级的文件夹下。

[UserAgent.txt](015-%20Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%EF%BC%88%E7%88%AC%E8%99%AB%E7%A5%9E%E5%99%A8%EF%BC%89%20a2ddaa44087c415c9cd6fff505eb1fc0/UserAgent.txt)

做完这一切，请看在**`middlewares.py`**文件中编写的代码。

```python
import random

class UserAgentMiddleware:
    def __init__(self):
        file = open('UserAgent.txt', 'r', encoding='utf-8')
        self.UserAgentList = eval(file.read())

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.UserAgentList)
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass
```

首先，自己编写UserAgentMiddleware类，定义初始化方法，提前将**`UserAgent.txt`**中的内容读取出来，记得使用eval方法对读取的字符串序列化，因为文件中整体数据我是以字符串化的列表写进去的，一个UA是列表中的一个元素。注意，在项目中编写的读取文件的代码，默认都是读取**`scrapy.cfg`**所在位置的文件的。然后从process_request方法中，编写随机获取UA的代码，将值赋予给**`requests.headers[’User-Agent’]`**即可，记得在**`settings.py`**中，写入对应配置。

```python
DOWNLOADER_MIDDLEWARES = {
    # 'chinaNews.middlewares.ChinanewsDownloaderMiddleware': 543,
    'chinaNews.middlewares.UserAgentMiddleware': 100,
}
```

## 三、scrapy结合selenium

有同学说，我遇到的网站比较难爬，我想使用selenium，那么scrapy能结合selenium使用吗，这个是可以的。

先在**`scrapy.cfg`**同级路径下创建一个名为**`utils.py`**的代码文件，写入以下代码。

```python
import os
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumSetting:
    driverPath = r'./chromeDriver'
    '文件夹已存在' if os.path.exists(driverPath) else os.mkdir(driverPath)
    with open('UserAgent.txt', 'r', encoding='utf-8') as file:
        UserAgentList = eval(file.read())
    s = ChromeService(ChromeDriverManager(path=driverPath).install())

    def create_chrome(self):
        Options = webdriver.ChromeOptions()
        Options.add_argument('--headless')
        Options.add_argument('blink-settings=imagesEnabled=false')
        Options.add_argument(f"--user-agent={random.choice(self.UserAgentList)}")
        browser = webdriver.Chrome(service=self.s, options=Options)
        return browser
```

此处导入的webdriver-manager模块，能够自动下载、配置浏览器驱动，学习起来很简单，关于webdriver-manager模块，详情请看官方文档：https://github.com/SergeyPirogov/webdriver_manager。

此处导入的os模块，负责判断chromeDriver文件夹是否存在，不存在就自动创建，创建chromeDriver文件夹的原因是指定webdriver-manager模块下载、配置浏览器驱动的路径。

创建SeleniumSetting类，然后定义create_chrome方法，在编写创建谷歌浏览器对象代码的同时，加入众多selenium配置项。

然后再从middlewares.py文件中编写如下代码：

```python
from scrapy.http import HtmlResponse
from utils import SeleniumSetting

class ChromeDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.closeSpider, signal=signals.spider_closed)
        return s

    def __init__(self):
        chromeObject = SeleniumSetting()
        self.browser = chromeObject.create_chrome()

    def closeSpider(self):
        self.browser.quit()

    def process_request(self, request, spider):
        self.browser.get(request.url)
        return HtmlResponse(url=request.url, body=self.browser.page_source, encoding='utf-8')

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass
```

此处创建了**`ChromeDownloaderMiddleware`**类，其中编写了初始化方法，用于实例化SeleniumSetting对象，以及调用SeleniumSetting类中的create_chrome方法；

然后编写的closeSpider方法，用于关闭打开的浏览器，即便是使用了无头浏览器，也是需要关闭的，关闭浏览器的操作借用了scrapy的signals信号机制，当检测到爬虫关闭时，执行关闭浏览器的操作。

**最重要的**，我们使用selenium来接管了scrapy的请求，那么需要修改process_request方法，**`self.browser.get(request.url)`**使用创建好的浏览器对象请求链接，需要请求的链接存在于scrapy中，可以通过**`request.url`**得到；下面写的**`return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8')`**是要将构造好的Response对象返回给引擎再通过蜘蛛中间件将其发送给蜘蛛进行处理。

在scrapy中有个Response类进行Response对象构造，但是这个类不允许调用，但是其子类HtmlResponse是允许调用使用的，所以我们将其所需参数传递给子类HtmlResponse，其中：

- **`url`**是HtmlResponse所需的网址，写成request.url即可，因为当前selenium请求的也是request.url，下面我们还需要这个网页的源代码。
- **`body`**是其所需的网页源代码，源代码已经得到，就是selenium请求request.url后的结果，使用page_source即可得到。
- **`encoding`**是其所需的网页编码方式，这个编码在网页的head标签中便能找到。

提供了这些参数，便能够得到最终的**`Response对象`**。

最终，将**`ChromeDownloaderMiddleware`**这个中间件，添加到scrapy的中间件配置中，就完成了scrapy和selenium的结合。其中注意，前文中我们设置了随机UA，但是那里设置的随机UA只适用于原来的scrapy爬虫，所以我一开始在**`utils.py`**文件中已经设置好了随机UA的代码。

```python
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'chinaNews.middlewares.ChinanewsDownloaderMiddleware': 543,
    # 'chinaNews.middlewares.UserAgentMiddleware': 200,
    'chinaNews.middlewares.ChromeDownloaderMiddleware': 100
}
```

## 四、项目源代码

[scrapyDemo_chinaNews.zip](015-%20Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%EF%BC%88%E7%88%AC%E8%99%AB%E7%A5%9E%E5%99%A8%EF%BC%89%20a2ddaa44087c415c9cd6fff505eb1fc0/scrapyDemo_chinaNews.zip)

需要安装的模块有scrapy、selenium、webdriver-manager、openpyxl、pymysql。