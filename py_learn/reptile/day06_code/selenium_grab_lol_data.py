# selenium 爬取英雄联盟 资料
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By     # 导入定位策略

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=Service(executable_path='driver/chromedriver.exe'),options=options)
url = 'https://101.qq.com/#/hero'
browser.get(url=url)
'''
    是否搜索到英雄名称，因为selenium 判定网页加载完，是判断标签前的刷新图标是否消失
    为了解决页面数据没加载完，selenium 就继续向下执行代码，需要添加等待
    等待分为三种： 休眠、隐式等待、显式等待
'''
# 休眠是强制的
time.sleep(2)

# 查看网页源代码（字符串类型）：page_source
print(browser.page_source, type(browser.page_source))
# 一.抓取信息（解析数据）：
# 方法一：
#     如果使用page_source，拿到的是字符串类型的源代码。接下来解析数据，直接用bs4模块即可

# 方法二：
'''
    find_element---->等价于select_one
    find_elements---->等价于select
    text---->获取标签内容
    get_attribute----> 获取标签对应的属性
'''
hero_list = []
# a. 获取一个英雄
# by:定位策略
result = browser.find_element(By.CSS_SELECTOR,
                     '#app > div > div.app-main > div > div.app-main-container.infomation-overview > ul > li:nth-child(97) > div > p')
# selenium 查找的结果是selenium 对象，数据被隐藏起来了
print(result, result.text)

pic_href = browser.find_element(
    By.CSS_SELECTOR,'#app > div > div.app-main > div > div.app-main-container.infomation-overview > ul > li:nth-child(97) > div > div > img')
print(pic_href.get_attribute('src'))

# b.获取所有英雄的信息
# nth-of-type:找某标签的第几个
# nth-child:找同级标签的第几个
li_list = browser.find_elements(By.CSS_SELECTOR,'#app > div > div.app-main > div > div.app-main-container.infomation-overview > ul > li')
for i in li_list:
    name = i.find_element(By.CSS_SELECTOR, 'li > div > p').text
    link = i.find_element(By.CSS_SELECTOR, 'li > div > div > img').get_attribute('src')
    hero_list.append([{'name': name, "link": link}])
print(hero_list)

browser.quit()