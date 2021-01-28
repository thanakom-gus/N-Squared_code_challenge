
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def get_followers(url):
    ##~ can't use requests because slow web page ~##
    
##    response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
##                            "Connection": "close"})

    prefix = (re.search('com/.*',url)).group()

    ##~ headless ~##
##    chrome_options = webdriver.ChromeOptions()
##    chrome_options.add_argument('--headless')
##    chrome_options.add_argument('--disable-gpu')
##    chrome_options.add_argument('--no-sandbox')
##    chrome_options.add_argument('--disable-dev-shm-usage')
##    driver = webdriver.Chrome("./chromedriver", chrome_options = chrome_options)

    driver = webdriver.Chrome("./chromedriver")
    driver.implicitly_wait(10)
    driver.get(url)
    wait_for_list = driver.find_element_by_class_name('css-9pa8cd') # wait for background
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    followers = soup.find('a', {'href':f'/{prefix[4:]}/followers'})
    driver.quit()
    return followers.text

if __name__ == "__main__":
    # testing
    test_set = ['https://twitter.com/KMbappe',
                'https://twitter.com/Ligue1UberEats',
                'https://twitter.com/MarceloGuedes02']
    for i in test_set:
        test = get_followers(i)
        print(test)

## finished time 00:42:59.34
