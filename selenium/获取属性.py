from selenium import webdriver
from selenium.webdriver.common.by import By
from io import BytesIO
from PIL import Image
import re,time
op = webdriver.ChromeOptions()
# 设置不被检测
op.add_argument('--disable-blink-features=AutomationControlled')
op.add_experimental_option('useAutomationExtension',False)
op.add_experimental_option('excludeSwitches',['enable-automation'])

path=r'D:\python\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path,chrome_options=op)
browser.maximize_window()
browser.get('https://pic.netbian.top/')
# e_list = browser.find_elements(By.CSS_SELECTOR,'ul.clearfix>li>a>span>div.pic')
e_list_one = browser.find_elements(By.CSS_SELECTOR,'ul.clearfix>li>a>span>div.pic')[0]

def get_url():
  e_list = browser.find_elements(By.CSS_SELECTOR,'ul.clearfix>li>a>span>div.pic')
  if(len(e_list)>0):
    for e in e_list:
      url = re.findall('"(.*?)"',e.get_attribute('style'))[0]
      print(url)

# 截图
def spl():
  size = e_list_one.size
  loca = e_list_one.location
  l,r,t,b = loca['x'],loca['x']+size['width'],loca['y'],loca['y']+size['height']
  screen = browser.get_screenshot_as_png()
  screen = Image.open(BytesIO(screen))
  cro=screen.crop((l,t,r,b))
  cro.save('./selenium/split.png')

spl()
time.sleep(5)
browser.quit()
