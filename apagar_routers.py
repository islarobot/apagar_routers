#!/usr/bin/env python

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait




driver = webdriver.Chrome()
driver.get('http://192.168.0.1')

#print(driver.page_source)

pepe = driver.find_element_by_name('fInfo')

driver.switch_to_frame(pepe)

username = driver.find_element_by_name("txtUser")
password = driver.find_element_by_name("txtPassword")
click = driver.find_element_by_id("login_1")

username.send_keys("")
password.send_keys("238500")

#wait = WebDriverWait(driver, 10)


click.click()

wait = WebDriverWait(driver, 2)

frame1 = driver.find_element_by_name('fInfo')
driver.switch_to_frame(frame1)

wifi = driver.find_element_by_id("wifi_menu_href")



wifi.click()

enable2G = driver.find_element_by_name("enablemode")
apply_button = driver.find_element_by_id("apply")
#disable
if(enable2G.is_selected()):
	enable2G.click()
	#apply_button.click()

wait = WebDriverWait(driver, 5)
wifi2G = driver.find_element_by_id("wifi_2g_href")
wifi2G.click()
enable2G_2 = driver.find_element_by_name("enablemode")
apply_button = driver.find_element_by_id("apply")
if(enable2G_2.is_selected()):
	enable2G_2.click()
	#apply_button.click()
	
driver.get('http://admin:238500@192.168.0.2')


juan = driver.find_element_by_name('bottomLeftFrame')

driver.switch_to_frame(juan)

click = driver.find_element_by_id("a9")
click.click()

driver.switch_to.default_content()




juan1 = driver.find_element_by_name('mainFrame')

driver.switch_to_frame(juan1)


enable2G = driver.find_element_by_name("ap")
apply_button = driver.find_element_by_id("Save")
if(enable2G.is_selected()):
	enable2G.click()
	apply_button.click()
