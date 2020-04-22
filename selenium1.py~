#!/usr/bin/env python

import unittest
from selenium import webdriver


driver = webdriver.Firefox()
driver.get('http://192.168.0.1')

#print(driver.page_source)

driver.switch_to.frame('fPanel')

print(driver.page_source)

driver.switch_to.frame('fInfo')

print(driver.page_source)