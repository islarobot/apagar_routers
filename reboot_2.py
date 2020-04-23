#!/usr/bin/env python
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")

chrome_options.add_argument("--disable-gpu")

chrome_options.add_argument("--headless")

chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)


#driver = webdriver.Chrome()

driver.get('http://admin:238500@192.168.0.2')

time.sleep(3)

juan = driver.find_element_by_name('bottomLeftFrame')

driver.switch_to_frame(juan)

time.sleep(1)
print("switch to bottomleftframe")



click = driver.find_element_by_id("a45")
#print(click)
click.click()


print("click a45")

time.sleep(2)

click = driver.find_element_by_id("a51")
click.click()

print("click a51")

time.sleep(2)

driver.switch_to.default_content()

print("go to top")

#wait = WebDriverWait(driver, 5)

print("wait 5s")

time.sleep(2)

juan1 = driver.find_element_by_name('mainFrame')

driver.switch_to_frame(juan1)

print("switch to main")

#wait = WebDriverWait(driver, 2)

time.sleep(2)

reboot = driver.find_element_by_name("Reboot")

print("find reboot")

reboot.click()

print("click reboot")

#wait = WebDriverWait(driver, 2)

time.sleep(2)

obj = driver.switch_to.alert
obj.accept()

print("accept popup")

time.sleep(3)

driver.close()
