from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#-----------Headless webdriver--------------------
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
#-------------------------------------------------
#driver = webdriver.Chrome()
#-------------------------------------------------
driver.get("http://192.168.1.254/")
while True:
    try:
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/div/table[2]/tbody/tr[1]/td[4]/input').click()
        break
    except:
        pass
driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/div/form/table/tbody/tr/td[2]/input').send_keys('2465405103')
driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/div/form/p[1]/input').click()
