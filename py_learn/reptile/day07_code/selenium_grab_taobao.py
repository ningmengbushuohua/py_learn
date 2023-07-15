# selenium 爬取淘宝
# 如何登录淘宝，搜索商品，提取信息

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait       # 显式等待模块
from selenium.webdriver.support import expected_conditions as EC    # 期望模块

# selenium  模块的学习： https://liushilive.github.io/github_selenium_docs_api_py/index.html

option =webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
option.add_argument('blink-settings=imagesEnabled=false')   # 图片不加载

browser = webdriver.Chrome(service=Service(executable_path='../day06_code/driver/chromedriver.exe'),options=option)
url = 'https://www.taobao.com/'
browser.get(url=url)
print(browser.window_handles)

# 1.寻找登录按钮并点击
login_btn = browser.find_element(
    By.CSS_SELECTOR, 'body > div.screen-outer.clearfix > div.main > div.main-inner.clearfix > div.col-right > div.tbh-user.J_Module > div > div.member-ft > div.member-logout.J_UserMemberLogout > a.btn-login.ml1.tb-bg.weight')
# click: 点击事件
login_btn.click()

'''
点击登录按钮后，浏览器自动打开新的标签页。加载登录界面
selenium 不会自动切换标签页，最初打开的是那个页面，就默认停留在哪个页面
window_handles: 查看目前浏览器存在的标签页
'''
print(browser.window_handles)

# 2. selenium 切换到新打开的登录标签页, switch_to.window---> 切换标签页
browser.switch_to.window(browser.window_handles[-1])

# 3. 点击登录界面的二维码，登录
browser.find_element(By.CSS_SELECTOR, '#login > div.corner-icon-view.view-type-qrcode > i').click()
'''
    注意：登录成功： 登录成功以后淘宝页面一定会有 你的淘宝用户名
        登录成功前，需要等待扫码。
        使用休眠、显式等待还是隐式等待：
            休眠：time.sleep() ---> 优点：写法简单。缺点：必须等待设置的时间
            隐式等待：优点：只需要写一次，即可全局设置成功
                    缺点：等待页面“完全”加载完才算结束（实际等标签前面那个加载的图标消失）
            显式等待：优点：可以指定等待某元素加载出来立即停止等待。缺点：写法麻烦。
'''

# 4. 显式等待淘宝首页出现用户名，立即停止等待
# 显式等待浏览器中的元素100s,直到某个期望的元素出现，立即结束等待执行下一步
# 如果100s 没有出现期望的元素，报错
WebDriverWait(browser,30).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR,'body > div.screen-outer.clearfix > div.main > div.main-inner.clearfix > div.col-right > div.tbh-user.J_Module > div > div.member-bd > a > span > strong'),
        'mini粽子763'
    )
)
print('登录成功')

# 5. 登录成功以后获取cookie,将cookie 保存到文件cookie.txt中
# cookie 是字典，cookies 是cookie 的复数，是一个列表，cookie 保存了用户的账号、密码信息
'''
    例如：网页登录账号，记住密码、下次自动登录
    如果勾选中，浏览器就会将账号、密码保存下载，下次再登录该网页时，检测本地有无相关账号信息，如果有，自动登录
'''
cookie = browser.get_cookies()

with open(r'cookie.txt','w',encoding='utf-8') as f:
    f.write(str(cookie))
    print(f'cookie写入完成')
browser.quit()