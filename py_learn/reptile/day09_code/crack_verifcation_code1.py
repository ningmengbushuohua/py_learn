# 网站破解验证码1

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 只要是破解验证码，必须使用selenium
# 验证码接入网站：https://www.chaojiying.com/

# 一. 破解文字验证码
# 1. 创建浏览器对象
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
brower = webdriver.Chrome(service=Service(executable_path=r'../day06_code/driver/chromedriver.exe'),options=options)
# 隐式等待写的创建完浏览器对象之后，即可全局生效
# 隐式等待：implicityly_wait(等待时间)
# 隐式等待设置一次，全局生效，只要寻找页面上的元素，如果没找到，会先等待设置的时间。超过设置时间没等到，报错
brower.implicitly_wait(30)

url = 'http://mail.1000phone.com/'
brower.get(url=url)

# 2. 寻找输入账号的输入框
# 如果输入账号、密码的位置处于iframe 的标签内，我们需要先告知selenium 需要先切换到iframe 标签内
# 有几层iframe 标签，就切换几次
# a. 切换iframe 标签
first_iframe = brower.find_element(By.CSS_SELECTOR,'#page > div.content.bg_default > div > div > iframe')
brower.switch_to.frame(first_iframe)
# b. 输入框填写账号
brower.find_element(By.CSS_SELECTOR,'#rc-tabs-0-panel-mail > div > div > input').send_keys('342131213')

# 3. 密码框输入密码
brower.find_element(By.CSS_SELECTOR,'#rc-tabs-0-panel-mail > div > div > span > input').send_keys('342131213')

#rc-tabs-0-panel-mail > div > div > button

# 4.点击登录
brower.find_element(By.CSS_SELECTOR, '#rc-tabs-0-panel-mail > div > div > button').click()

# 5.按照此网站特性，此时验证码应该出现
# 文字验证码出现，截图、识别，填入验证码输入框
# screenshot(): 截图方法，selenium 找到那个元素，screenshot截取那一部分，并保存到本地
brower.find_element(By.CSS_SELECTOR, '#rc-tabs-0-panel-mail > div > div > div:nth-child(5) > div > div > img').screenshot(r'temp/capture_pic.png')

# 6.处理得到验证码（使用第三方服务）

# 导入超级鹰提供的模块
from chaojiying import Chaojiying_Client
# 创建能连接超级鹰服务的对象
chaojiying = Chaojiying_Client('jiangliang7', 'Missing3', '950670')
# 按照超级鹰要求，读取图片的二进制形式
im = open(r'temp/capture_pic.png','rb').read()
# 将读取的图片二进制上传到超级鹰服务器，识别并说明类型
result = chaojiying.PostPic(im,1004)
print(result)
# 从打印结果中将结果提取出来，填入输入框
code = result['pic_str']

# 7.填入输入框
brower.find_element(By.CSS_SELECTOR, '#rc-tabs-0-panel-mail > div > div > div:nth-child(5) > input').send_keys(code)

# 输入完账号、密码、验证码、点击登录