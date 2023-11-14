from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,random

op = webdriver.ChromeOptions()
op.add_argument('--disable-blink-features=AutomationControlled')
path =r'D:\PY\python-3.11.5-embed-amd64\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path,chrome_options=op)

browser.maximize_window()
browser.get('https://www.yiwugo.com/')

inp = browser.find_element(By.ID,'inputkey')
inp.send_keys('围巾')
inp.send_keys(Keys.ENTER)

total_list_img=[]
total_list_title=[]

def getImageList():
    imgs = browser.find_elements(By.CSS_SELECTOR,'div.pro_list_product_img2>p>span>a>img')
    img_list=[]
    for i in imgs:
        url = i.get_attribute("data-url")
        if url.count('http')==0:
            url = 'http:'+url
        img_list.append(url)
    total_list_img.extend(img_list)
    # print(img_list)
    # print(len(img_list))

def getTitleList():
    titles = browser.find_elements(By.CSS_SELECTOR,'div.pro_list_product_img2>ul>li.font_tit>a')
    tit_list=[]
    for i in titles:
        t = i.get_attribute("title")
        if t:
            tit_list.append(t)
    # print(tit_list)
    # print(len(tit_list))
    total_list_title.extend(tit_list)

def getData():
    getImageList()
    time.sleep(random.randint(100,300)*0.05)
    getTitleList()


for i in range(1,4):
    if i==1:
        getData()
        time.sleep(1)
    else:
        btn = browser.find_element(By.CSS_SELECTOR,'span.page_yes+a')
        btn.click()
        time.sleep(1)
        getData()

print(total_list_img)
print(len(total_list_img))
print(total_list_title)
print(len(total_list_title))
browser.quit()