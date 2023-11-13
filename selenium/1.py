from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# op = webdriver.EdgeOptions()
# op.add_experimental_option("detach" , True)
# browser = webdriver.Edge(options=op)
# browser.get('https://www.baidu.com')

# op = webdriver.ChromeOptions()
# op.add_experimental_option('detach',True)

# 初始化操作
# 绕过滑块
op = webdriver.ChromeOptions()
# 设置不被检测
op.add_argument('--disable-blink-features=AutomationControlled')
# 无头模式----不弹出浏览器窗口
# op.add_argument('-headless')
# 隐藏‘正在收到控制’
op.add_experimental_option('useAutomationExtension',False)
op.add_experimental_option('excludeSwitches',['enable-automation'])


path=r'D:\python\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path,chrome_options=op)
# browser.get('https://mmzztt.com')
# 窗口放大
browser.maximize_window()
# 设置宽高
# browser.set_window_size(400,900)
browser.get('https://baidu.com')

# 后退
# browser.back()

# 前进
# browser.forward()

kw =  browser.find_element_by_id('kw')
su = browser.find_element_by_id('su')
kw.send_keys('美女')
# 直接回车
kw.send_keys(Keys.ENTER)
# su.click()
print(kw)

# time.sleep(5)
# browser.quit()