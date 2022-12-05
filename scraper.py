from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


s = Service('chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.get('https://www.youtube.com/@TeachMeGrappling/videos')
time.sleep(3)
driver.maximize_window()

x = True
while x == True:
    driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
    time.sleep(2)

    height = driver.execute_script("return document.documentElement.scrollHeight")
    print(height)

    newHeight = driver.execute_script("return document.body.offsetHeight")

    xxx = driver.execute_script("return window.innerHeight")
    print(xxx)
    zzz = driver.execute_script("return window.scrollY")
    print(zzz)

    if xxx + zzz >= height:
        x = False


videos = driver.find_elements(by=By.CLASS_NAME, value='style-scope ytd-rich-grid-media')
contents = []
for video in videos:
    title = video.find_element(by=By.XPATH, value='.//*[@id="video-title"]').text
    views = video.find_element(by=By.XPATH, value='.//*[@id="metadata-line"]/span[1]').text
    when = video.find_element(by=By.XPATH, value='.//*[@id="metadata-line"]/span[2]').text
    href = video.find_element(by=By.XPATH, value='.//*[@id="video-title-link"]').get_attribute('href')
    contents.append({'title': title, 'views': views, 'when': when, 'href': href})



with open('teach_me_grappling.csv', 'w+', newline='', errors="ignore") as file:
    write = csv.DictWriter(file, fieldnames=['title', 'views', 'when', 'href'])
    write.writeheader()
    write.writerows(contents)


driver.close()
