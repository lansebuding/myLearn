from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
op = webdriver.ChromeOptions()
# 设置不被检测
op.add_argument('--disable-blink-features=AutomationControlled')
op.add_experimental_option('useAutomationExtension',False)
op.add_experimental_option('excludeSwitches',['enable-automation'])


path=r'D:\python\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path,chrome_options=op)
browser.maximize_window()

browser.get('https://pic.netbian.top/')
browser.execute_script('window.open()')
# browser.get('https://mmzztt.com')
browser.switch_to.window(browser.window_handles[1])
browser.get('https://mmzztt.com')

time.sleep(2)
browser.switch_to.window(browser.window_handles[0])

print(browser.window_handles)