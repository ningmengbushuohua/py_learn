import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

option =webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
option.add_argument('blink-settings=imagesEnabled=false')   # 图片不加载

browser = webdriver.Chrome(service=Service(executable_path='../day06_code/driver/chromedriver.exe'),options=option)
url = 'https://www.taobao.com/'
browser.get(url=url)

# 1. 从文件中读取cookie,注入到淘宝界面
# 注意：cookie 具有时效性，万一失效了需要重新获取
with open(r'cookie.txt','r') as f:
    cookie = eval(f.read())

for i in cookie:
    # 向浏览器(已经打开的淘宝界面)添加cookie
    browser.add_cookie(i)
# refresh(): 刷新界面.  页面已经加载完，添加的cookie 看起来没加进去，需要刷新
browser.refresh()
# 淘宝完全登录成功
# 淘宝登录成功，便可以爬取淘宝的商品信息

# 2. 需求：找到搜索框，搜索  手机 ，爬取手机相关信息
# send_keys()； 向输入框传递信息
browser.find_element(By.CSS_SELECTOR,'#q').send_keys('手机')
browser.find_element(By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button').click()

# 3. 实现页面的滚动
# 商品页有很多类型的商品，屏幕显示的商品有限。瀑布式加载---> 未显示的商品先不加载（节约网速，带来更好的体验）
# 页面显示的商品不全，爬虫获取的信息就会有缺失
y = 0
while True:
    # 每次滚动500 像素点
    y += 500
    # selenium 调用页面滚动的方法， execute_script() 执行js代码
    browser.execute_script(f'window.scrollTo(0,{y})')
    # 滚动一次休眠一次（防止被检测到时爬虫）
    time.sleep(1)
    if y > 6000:
        break

# 页面到底，信息加载完，爬虫得到的信息不再缺失
# 此时可以爬取信息
# 如果构造不出翻页信息，可以使用selenium 点击下一页
