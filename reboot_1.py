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
driver.get('http://192.168.0.1')

#print(driver.page_source)

pepe = driver.find_element_by_name('fInfo')

driver.switch_to_frame(pepe)

time.sleep(2)

username = driver.find_element_by_name("txtUser")
password = driver.find_element_by_name("txtPassword")
click = driver.find_element_by_id("login_1")

username.send_keys("")
password.send_keys("238500")

#wait = WebDriverWait(driver, 10)


click.click()

#wait = WebDriverWait(driver, 2)

time.sleep(2)

frame1 = driver.find_element_by_name('fInfo')
driver.switch_to_frame(frame1)

time.sleep(2)

system = driver.find_element_by_id("sys_menu_href")



system.click()

time.sleep(2)

reboot_menu = driver.find_element_by_id("tools_backup_setting_href")

reboot_menu.click()



#wait = WebDriverWait(driver, 5)

time.sleep(2)

reboot_button = driver.find_element_by_id("reboot")
reboot_button.click()

time.sleep(2)

obj = driver.switch_to.alert
obj.accept()

time.sleep(2)
#wait = WebDriverWait(driver, 2)

obj = driver.switch_to.alert
obj.accept()

time.sleep(2)

driver.close()
