#! python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests, bs4

import time;

#Function 取得網頁
def GetContent(url):

    if url.startswith('//'):
        url = 'https:' + url
    target_url = url

    #print('GetContent(' + target_url+')')

    #pathChromedriver = r'D:\Program\python\study\chromedriver.exe' #你的本地chromedriver
    pathChromedriver = r'chromedriver.exe' #你的本地chromedriver
    
    chrome_options=webdriver.ChromeOptions()
    chrome_options.set_headless()
    chrome_options.add_argument('--disable-gpu')
    driver=webdriver.Chrome(pathChromedriver,options=chrome_options)
    driver.get(target_url)  # 輸入範例網址，交給瀏覽器
    pageSource = driver.page_source  # 取得網頁原始碼
    
    print('GetContent(' + target_url+')' + str(len(pageSource)))
    #print(pageSource) #看結果
    #看匯出
    t=time.strftime("%Y%m%d%H%M%S", time.localtime())
    outFileName='GetContent_{t}.html'.format(t=t)
    outFile = open(outFileName,'w',encoding="utf-8")
    outFile.write(pageSource)
    
    driver.quit()

    #使用BeautifulSoip解析HTML
    soup = bs4.BeautifulSoup(pageSource,'html.parser')

    return soup
#end function
