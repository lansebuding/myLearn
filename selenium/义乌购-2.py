import pymongo

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,random

# op = webdriver.ChromeOptions()
# op.add_argument('--disable-blink-features=AutomationControlled')
# path =r'D:\PY\python-3.11.5-embed-amd64\chromedriver.exe'
# browser = webdriver.Chrome(executable_path=path,chrome_options=op)

# browser.maximize_window()
# browser.get('https://www.yiwugo.com/')

# 连接
# client = pymongo.MongoClient('127.0.0.1',27017)
# datas = client['py_test']['my']

def get_print():
    db= pymongo.MongoClient('127.0.0.1',27017)['py_test']['my']
    res = db.find({})
    # res = db.find({'title':{'$regex':'超百搭韩版围巾'}})
    # ii = 0
    # for i in res:
    #     ii+=1
    #     print(i)
    # print(ii)
    list1 = list(res)
    print(list1)
    print(len(list1))


class My_Test:
    """
    爬取义乌购页面数据练习
    """
    def __init__(self) -> None:
        self.browser= self.init_browser()
        self.db,self.client = self.get_client()
        pass

    # 连接mongodb
    def get_client(self):
        client = pymongo.MongoClient('127.0.0.1',27017)
        datas = client['py_test']['my']
        return datas,client

    # 初始化selenium连接
    def init_browser(self):
        op = webdriver.ChromeOptions()
        op.add_argument('--disable-blink-features=AutomationControlled')
        path =r'D:\PY\python-3.11.5-embed-amd64\chromedriver.exe'
        browser = webdriver.Chrome(executable_path=path,chrome_options=op)
        return browser
    
    # 入口
    def get_connect(self):
        self.browser.maximize_window()
        self.browser.get('https://www.yiwugo.com/')
        inp = self.browser.find_element(By.ID,'inputkey')
        inp.send_keys('围巾')
        inp.send_keys(Keys.ENTER)
        time.sleep(.5)
        self.get_datas()
        # self.browser.quit()

    # 滑动
    def swiper(self):
        for i in range(1,11):
            time.sleep(random.randint(500,1000)*0.001)
            self.browser.execute_script(f'document.documentElement.scrollTop=document.documentElement.scrollHeight*{i*0.1}')

    # 每页数据处理
    def get_datas(self):
        self.swiper()
        elements = self.browser.find_elements(By.CSS_SELECTOR,'div.pro_list_product_img2')
        # db=self.get_client()
        for i in elements:
            title = i.find_element(By.CSS_SELECTOR,'a.productloc').get_attribute("title")
            num1 = i.find_element(By.CSS_SELECTOR,'span.pri-left').find_elements(By.TAG_NAME,'font')[0].text
            num2 = i.find_element(By.CSS_SELECTOR,'span.pri-left').find_elements(By.TAG_NAME,'font')[1].text
            start:str = i.find_element(By.CSS_SELECTOR,'span.pri-right>span').text
            store:str = i.find_element(By.CSS_SELECTOR,'li.product13_company>font>a').text
            address:str = i.find_element(By.CSS_SELECTOR,'li.shshopname').text
            dic = {'title':title,'price':f'{str(num1)+"."+str(num2)}元','start':start.strip(),'store':store.strip(),'address':address.strip(),'createTime':int(time.time())}
            self.db.insert_one(dic)
        self.page_change()

    # 分页
    def page_change(self):
        try:
            element = self.browser.find_element(By.CSS_SELECTOR,'a.page_next_yes')
            element.send_keys(Keys.ENTER)
            time.sleep(1)
            self.get_datas()
        except Exception as err:
            print('down')
            self.client.close()
            self.browser.quit()

if __name__=='__main__':
    get_print()
    # My_Test().get_connect()