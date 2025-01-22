from bs4 import BeautifulSoup
from selenium import webdriver

def scrape_workshops():
    url = "https://unstop.com/workshops-webinars"
    driver_path = "C:/Users/tejes/Desktop/chromedriver.exe"
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # print(soup)
    driver.quit()
    with open('temp.txt', 'w+', encoding='utf-8') as w:
        w.write(str(soup))
scrape_workshops()
