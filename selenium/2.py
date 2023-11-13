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

browser.get('https://taobao.com')

search = browser.find_element_by_id('q')
search.send_keys('辣条')
search.send_keys(Keys.ENTER)