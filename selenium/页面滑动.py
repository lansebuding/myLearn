from selenium import webdriver
from selenium.webdriver import ActionChains
import time,random


op = webdriver.ChromeOptions()
op.add_argument('--disable-blink-features=AutomationControlled')
op.add_experimental_option('useAutomationExtension',False)
op.add_experimental_option('excludeSwitches',['enable-automation'])
path=r'D:\python\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path,chrome_options=op)

browser.maximize_window()
browser.get('https://search.jd.com/Search?keyword=%E9%81%A5%E6%8E%A7%E9%A3%9E%E6%9C%BA&enc=utf-8&pvid=8a004735002546d18a1fd2adf5a88830')

# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

# 延迟触发，防止检查
def sc():
  for i in range(1,10):
    js = f'document.documentElement.scrollTop = document.documentElement.scrollHeight * {i/10}'
    browser.execute_script(js)
    time.sleep(random.randint(400,800)/1000)