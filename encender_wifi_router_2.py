#!/usr/bin/env python

import time
import unittest
import sys
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


juan = driver.find_element_by_name('bottomLeftFrame')

driver.switch_to_frame(juan)

time.sleep(2)

click = driver.find_element_by_id("a9")
click.click()

time.sleep(2)

driver.switch_to.default_content()

time.sleep(2)


juan1 = driver.find_element_by_name('mainFrame')

driver.switch_to_frame(juan1)

time.sleep(2)

enable2G = driver.find_element_by_name("ap")
apply_button = driver.find_element_by_id("Save")
if not enable2G.is_selected():
	enable2G.click()
	apply_button.click()

time.sleep(2)

driver.quit()

time.sleep(2)


