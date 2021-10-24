#***TESTED ON UBUNTU 18*******

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import urllib, os, urllib.request
import time

options = webdriver.FirefoxOptions()
options.headless=False

#driver = webdriver.Firefox(options= options)


# fp = webdriver.FirefoxProfile('/home/USER/.mozilla/firefox/9tn0o76g.default-release')
# fp.set_preference("browser.download.folderList",2)
# fp.set_preference("browser.download.dir", os.getcwd())
# driver = webdriver.Firefox(firefox_profile=fp)

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
# ENTER DOWNLOAD PATH HERE:
profile.set_preference("browser.download.dir", "/home/USER/Downloads/")
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")

profile.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(profile, options= options)

driver.maximize_window()

time.sleep(0)

for i in range(1,56): 
    #Insert your own URL
    driver.get("INSERT URL HERE")
    
    #Replace the paths below in quotations with the xpaths of where to click
    driver.find_element_by_xpath('/html/body/div/div[1]/div/main/article/div/div/div/div[6]/div[1]').click() 
    driver.find_element_by_xpath('/html/body/div/div[1]/div/main/article/div/div/div/div[6]/ul/li[24]/div').click() 
    driver.find_element_by_xpath(f'/html/body/div/div[1]/div/main/article/div/div/div/div[6]/ul/li[24]/ul/li[{i}]/a').click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div/main/article/div/div/div/p[1]/a').click()
#https://stackoverflow.com/questions/23800195/auto-download-pdf-in-firefox