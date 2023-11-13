from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

op = webdriver.ChromeOptions()
# 设置不被检测
op.add_argument('--disable-blink-features=AutomationControlled')
op.add_experimental_option('useAutomationExtension',False)
op.add_experimental_option('excludeSwitches',['enable-automation'])

path=r'D:\python\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path,chrome_options=op)
browser.maximize_window()
browser.get('https://www.taobao.com')

wait = WebDriverWait(browser,10)
# browser.find_element()
inputs = wait.until(EC.presence_of_element_located((By.ID,'q')))
btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
print(inputs,btn)
print(type(inputs))