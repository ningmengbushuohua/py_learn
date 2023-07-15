import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
brower = webdriver.Chrome(service=Service(executable_path=r'../day06_code/driver/chromedriver.exe'),options=options)

url = 'https://www.bilibili.com/'
brower.get(url=url)
time.sleep(1)
# 寻找登录按钮，点击
brower.find_element(
    By.CSS_SELECTOR,
    '#i_cecream > div.bili-feed4 > div.bili-header.large-header > div.bili-header__bar > ul.right-entry > li:nth-child(1) > li > div.right-entry__outside.go-login-btn > div'
).click()

# 添加休眠，等待账号密码框
time.sleep(3)
# 寻找账号密码的输入框，输入账号密码，点击登录，等待验证码的加载
brower.find_element(
    By.CSS_SELECTOR,
    'body > div.bili-mini-mask > div > div.bili-mini-login-right-wp >'
    ' div.login-pwd-wp > form > div:nth-child(1) >'
    ' input[type=text]').send_keys('你的b站账号')
brower.find_element(
    By.CSS_SELECTOR,
    'body > div.bili-mini-mask > div >'
    ' div.bili-mini-login-right-wp > div.login-pwd-wp >'
    ' form > div:nth-child(3) > input[type=password]').send_keys('你的b站密码')
brower.find_element(
    By.CSS_SELECTOR,
    'body > div.bili-mini-mask > div > div.bili-mini-login-right-wp >'
    ' div.login-pwd-wp > div.btn_wp > div.btn_primary').click()

time.sleep(3)

# 找到验证码位置
code = brower.find_element(
    By.CSS_SELECTOR,
    'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_panelshowclick > '
    'div.geetest_panel_next > div > div'
)

# 从找到的验证码web元素对象分别获取元素的位置和宽高
location,size = code.location, code.size
print(location,size)        # {'x': 457, 'y': 425} {'height': 408, 'width': 318}
code.screenshot(r'temp/bilibili_cap.png')

# 通过第三方 超级鹰识别
from chaojiying import Chaojiying_Client
chaojiying = Chaojiying_Client('jiangliang7', 'Missing3', '950670')
im = open(r'temp/bilibili_cap.png','rb').read()
# 9004: 坐标多选,返回1~4个坐标,如:x1,y1|x2,y2|x3,y3
result = chaojiying.PostPic(im, 9004)
print(result)

# 提取超级鹰识别的坐标
if result['err_no'] == 0:
    # 通过ActionChains 模拟鼠标移动和点击
    ac = ActionChains(brower)

    pic_location = result['pic_str']
    for item in pic_location.split('|'):
        # x,y 拿到的是分别是两个字的x 坐标和y坐标
        x,y = map(int,item.split(','))
        # 将鼠标移动到验证码上，selenium4.2开始，move_to_element_with_offset的基准位置为指定元素的中心点
        # size: {'height': 408, 'width': 318}
        # 在ActionChains 对象调用操作方法时，操作将存储在ActionChains 对象的队列中，
        # 当调用perform()， 事件将按他们的排队顺序触发
        ac.move_to_element_with_offset(code,x - size['width'] / 2, y - size['height'] / 2).click().perform()
        # 点击一个字，休眠0.5s,避免被识别成机器人（爬虫）
        time.sleep(0.5)

# 所有的字点击完，即可点击登录

brower.quit()
