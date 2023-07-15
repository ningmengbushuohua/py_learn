# selenium基础

### 基本使用

1.创建浏览器对象并加载页面

```python
from selenium import webdriver
# 创建Chrome浏览器对象
browser = webdriver.Chrome()
URL = 'https://www.baidu.com/'
# 加载页面
browser.get(URL)
```

2.打印页面源码

```python
from selenium import webdriver
# 创建Chrome浏览器对象
browser = webdriver.Chrome()
URL = 'https://www.baidu.com/'
# 加载页面
browser.get(URL)
print(browser.page_source)
```

3.基本配置

```python
from selenium import webdriver
# 创建设置对象
options = webdriver.ChromeOptions()
# 设置option.add_experimental_option("detach", True)不自动关闭浏览器
option.add_experimental_option("detach", True)
# 解决DevToolsActivePort文件不存在的报错
options.add_argument('--no-sandbox')
# 谷歌文档提到需要加上这个属性来规避bug
options.add_argument('--disable-gpu')
# 隐藏滚动条, 应对一些特殊页面
options.add_argument('--hide-scrollbars')
# 图片不加载选其一# 不加载图片, 提升速度
options.add_argument('blink-settings=imagesEnabled=false')
# 不加载图片, 提升速度
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
# 设置取消测试环境
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 无头模式# 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败(无头浏览器)
# 减少了资源消耗的同时，增加了被反爬的风险
options.add_argument('--headless')
# 设置代理
option.add_argument('--proxy-server=http://代理服务器:端口')
# 避免终端下执行代码报错
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
# 加载拓展插件
options.add_extension(插件路径)
# 设置请求头UA = "Mozilla…………"
options.add_argument(f"--user-agent={UA}")
# 设置配置
browser = webdriver.Chrome(options=options)
# 加载用户缓存# 可以像正常使用浏览器一样，记录使用记录和cookie# 如果不指定缓存路径，不指定的时候会创建临时文件夹。
# 如果selenium实例没有正常销毁，那么当前缓存文件夹不会被删除。
user_dir = r'C:\userDir'options.add_argument(f"--user-data-dir={user_dir}")
# 去除navigator.webdriver属性
browser.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",{
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    }
)
# 或者
options.add_argument("disable-blink-features=AutomationControlled")
URL = 'https://www.baidu.com/'
# 加载页面
browser.get(URL)
```

4.控制浏览器窗口的大小

```python
# WebDriver提供了set_windows_size()方法来设置浏览器的大小
# 设置浏览器大小800*800
browser.set_window_size(800, 800)
# 浏览器最大化
browser.maximize_window()
```

5.页面滚动

```python
# selenium使用execute_script方法执行JavaScript操作
# scrollTo()方法可把内容滚动到指定的坐标。
max_y = 5000
y = 0
while y <= max_y:
    browser.execute_script(f'window.scrollTo(0,{y})')
    y += 500
    time.sleep(1)
```

6.前进后退

```python
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
time.sleep(1)
browser.get('https://www.taobao.com/')
time.sleep(1)
browser.get('https://www.jd.com/')
time.sleep(1)
# 后退
browser.back()
time.sleep(1)
# 前进
browser.forward()
```

7.浏览器选项卡切换

```python
from selenium import webdriver
import time
browser = webdriver.Chrome()
# 打开百度页面
browser.get('https://www.baidu.com/')
# 打开新的选项卡
browser.execute_script('window.open()')
# 切换到新打开的选项卡
browser.switch_to.window(browser.window_handles[1])
# 打开淘宝页面
browser.get('https://www.taobao.com')
time.sleep(1)
# 切换回百度选项卡
browser.switch_to.window(browser.window_handles[0])
```

8.获取cookies

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
# 获取cookie
cookies = browser.get_cookies()
# 设置cookie
browser.add_cookie(cookies)
# 删除所有cookie
browser.delete_all_cookies()
print(browser.get_cookies())
```

9.查找单个元素

```python
from selenium import webdriver
browser = webdriver.Chrome()
URL = 'https://www.baidu.com/'
browser.get(URL)
# 通过id属性查找百度页面logo地址
browser.find_element_by_id('s_lg_img').get_attribute('src')
# 通过CSS选择器查找百度搜索框
browser.find_element_by_css_selector('#kw')
# 以上两种方法仅为举例，不代表全部查找元素方法
```

10.查找多个元素

查找多个元素和查找单个元素相同，仅仅是将`find_element`换成了`find_elements`,

同时，`find_element`与`find_elements`的区别就相当于`select_one`和`select`的区别一样。

11.关闭浏览器窗口

```python
browser.close()
# 或者
browser.quit()
"""二者区别：close方法是关闭当前的选项卡，如果是打开了多个选项卡，那么close关闭的是browser操作的当前选项卡，如果当前浏览器只打开一个选项卡，那么close方法相当于关闭浏览器了；quit方法则是完全关闭所有选项卡，关闭浏览器。那么问题来了，我们关闭浏览器应该采用那个方法呢？当我们用webdriver打开浏览器时，会在系统盘产生临时文件，如果使用close方法关闭浏览器，并不会主动清除系统盘的临时文件，反之使用quit方法完全关闭浏览器会自动清除临时文件，减少对系统盘空间的占用。所以，当你浏览器打开多选项卡时，只想关闭当前选项卡，就用close方法，但是关闭浏览器最好使用quit方法。"""
```

12.元素交互动作

```python
from selenium import webdriver
# 导入按键事件库
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
URL = 'https://www.baidu.com/'
browser.get(URL)
# 通过id属性查找百度页面logo地址
browser.find_element_by_id('s_lg_img').get_attribute('src')
# 通过CSS选择器查找百度搜索框
search = browser.find_element_by_css_selector('#kw')
# 向搜索框中添加搜索内容
search.send_keys('手机')
# 回车进行搜索
search.send_keys(Keys.ENTER)
# 或者
# 查找点击搜索按钮
search_btn = browser.find_element_by_css_selector('#su')
# 点击事件
search_btn.click()
# 如果页面中存在iframe标签，需要先进行标签切换
# switch_to.frame() 默认可以直接取表单的id或name属性
browser.switch_to.frame('id或name属性')
# 从iframe标签切换出来
browser.switch_to.default_content()
```

13.等待

- 隐式等待：无条件的等待
    
    原理：隐式等待就是在创建浏览器对象时，为浏览器对象创建一个等待时间，这个方法是得不到某个元素就等待一段时间，直到拿到某个元素位置。
    
- 显式等待：有条件的等待
    
    原理：显示等待就是指定一个等待条件，和一个最长等待时间，程序会判断在等待时间内条件是否满足，如果满足则返回，如果不满足会继续等待，超过时间就会抛出异常。
    

```python
from selenium import webdriver
browser = webdriver.Chrome()
# 隐式等待
browser.implicitly_wait(10)# 等待10秒钟
url = 'https://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)
```

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
# 显式等待
wait = WebDriverWait(browser, 10)
# 等待指定元素加载成功
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)
```

有很多命令行可以用于 GoogleChrome 浏览器。一些改变特性的行为，另一些用于调试或试验。此页面列出了可用的开关，包括它们的条件和说明。

https://peter.sh/experiments/chromium-command-line-switches/