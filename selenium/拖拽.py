from selenium import webdriver
from selenium.webdriver import ActionChains


op = webdriver.ChromeOptions()
op.add_argument('--disable-blink-features=AutomationControlled')
op.add_experimental_option('useAutomationExtension',False)
op.add_experimental_option('excludeSwitches',['enable-automation'])
path=r'D:\python\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path,chrome_options=op)

browser.maximize_window()
browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 切换iframe
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_id('draggable')
target = browser.find_element_by_id('droppable')

actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()