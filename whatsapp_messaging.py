# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:07:20 2021

@author: prabh
"""

import pywhatkit
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pandas
import time

browser=webdriver.Chrome('chromedriver.exe')
browser.get('https://web.whatsapp.com/')
wait = WebDriverWait(browser, 30)




list=['+917858933120']

for i in list:
    search_box = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    person_title = wait.until(lambda driver:driver.find_element_by_xpath(search_box))
    person_title.clear()
    person_title.send_keys(i)
    time.sleep(3)

    message = 'Hello Vikash, This is Somu from Dhanalakshmi Luxury PG for Gents.Have a Good Night.'
   
    person_title.send_keys(Keys.ENTER)
    actions = ActionChains(browser)
    actions.send_keys(message)
    actions.send_keys(Keys.ENTER)
    actions.perform()
#insert exception when there is no whatsapp account on that number



    



