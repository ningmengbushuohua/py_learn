# selenium 的环境配置
# 1. 简介
'''
    selenium:
    selenium自动化测试工具
    selenium是一个用于web 程序测试的工具，selenium 是直接运行在浏览器中的，能够像真正的用户那样操作浏览器。
    支持‘IE、Google、edge、Firefox、Safari、open 浏览器等
    selenium 主要用来解决爬虫中的JavaScript 渲染问题
'''
# 2. 使用google 浏览器
# 谷歌为selenium 适配了一个 CDP(谷歌开发者工具协议)，selenium结合CDP能够发挥出巨大的威力

# 3.环境配置
# a. 谷歌浏览器，https://www.google.cn/chrome/index.html
# b. 查看谷歌浏览器的版本
# c. 下载驱动文件; https://registry.npmmirror.com/binary.html?path=chromedriver/
#   根据已安装的浏览器的版本号寻找相匹配的文件夹，如果没有，找最相近的但是低于已安装浏览器版本号的文件夹

# 4. 下载的驱动压缩包解压
'''
    解压后文件 chromedriver.exe
'''

# 5. 安装selenium 模块
# pip install selenium

# 6.验证环境是否正常
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

driver = Chrome(service=Service(executable_path='driver/chromedriver.exe'))

driver.get(url="https://www.baidu.com")
driver.close()
