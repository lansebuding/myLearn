from selenium import webdriver


# op = webdriver.EdgeOptions()
# op.add_experimental_option("detach" , True)
# browser = webdriver.Edge(options=op)
# browser.get('https://www.baidu.com')

# op = webdriver.ChromeOptions()
# op.add_experimental_option('detach',True)
path=r'D:\PY\python-3.11.5-embed-amd64\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
browser.get('https://www.baidu.com')