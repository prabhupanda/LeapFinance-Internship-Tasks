# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 15:48:37 2021

@author: prabh
"""

import numpy as np
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#initiate chromedriver
browser=webdriver.Chrome('chromedriver.exe')
browser.maximize_window()
#Instantiating the Dataframe
df=pd.read_csv('sync2lsq_03.07.csv')
link_list=df['Link'].tolist()

browser.get('https://portal.leapfinance.com/')
time.sleep(150)
issue=[]
for i in range(df.shape[0]):
    ip_link=df['Link'][i]
    try:
        
        browser.get(ip_link)
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="__next"]/nav/div/ul[2]/li/button').click()
    except:
        print(df['appId'][i])
        issue.append(df['appId'][i])
