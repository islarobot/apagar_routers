#!/usr/bin/env python

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait




driver = webdriver.Chrome()

driver.get('http://admin:238500@192.168.0.2')


juan = driver.find_element_by_name('bottomLeftFrame')

driver.switch_to_frame(juan)

click = driver.find_element_by_id("a45")
click.click()

click = driver.find_element_by_id("a51")
click.click()
driver.switch_to.default_content()

wait = WebDriverWait(driver, 5)


juan1 = driver.find_element_by_name('mainFrame')

driver.switch_to_frame(juan1)


reboot = driver.find_element_by_name("Reboot")
reboot.click()

obj = driver.switch_to.alert
obj.accept()

#driver.close()
