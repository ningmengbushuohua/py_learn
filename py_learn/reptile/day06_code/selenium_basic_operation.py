# selenium 基本操作
from selenium import webdriver      # 导入网页驱动
from selenium.webdriver.chrome.service import Service   # 从谷歌浏览器包中导入驱动服务
import time     # 时间模块

# 3. 为谷歌浏览器对象修改配置（创建设置对象）------前提
options =webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# 1.创建谷歌浏览器对象
# 方式一
browser = webdriver.Chrome(service=Service(executable_path='driver/chromedriver.exe'),options=options)
# 方式二：（旧特性）
# browser = webdriver.Chrome(executable_path='driver/chromedriver.exe')

# 4. 修改浏览器窗口大小
# a.浏览器窗口最大化
# browser.maximize_window()
# b.自定义窗口尺寸
browser.set_window_size(400, 400)

# 2.请求页面
browser.get(url='https://www.baidu.com')
time.sleep(1)
browser.get(url='https://www.taobao.com/')
time.sleep(1)
# a.标签页后退
browser.back()
time.sleep(1)
# b.标签页前进
browser.forward()

# 5.是否关闭浏览器
'''
    注意：close() 和 quit() 二选一
        close() 如果浏览器只有一个标签页，关闭浏览器；如果浏览器有多个标签页，只关闭当前标签页
        quit() 直接关闭浏览器
'''

result = input('是否关闭浏览器（输入是或者否）：')
if result == '是':
    browser.close()
    # browser.quit()

