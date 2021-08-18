# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 17:28:15 2021

@author: prabh
"""
import numpy as np
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

df=pd.read_csv('leap_finance_bids.csv')
bid_links=df['Lender link'].values
#print(bid_links)

browser=webdriver.Chrome('chromedriver.exe')
browser.maximize_window()
time.sleep(5)
bid_al=[]
for i in range(df.shape[0]):
    try:
        time.sleep(5)
        browser.get(df['Lender link'][i])
        loan_amount=browser.find_element_by_xpath('//*[@id="max_loan_amount"]')
        loan_amount.send_keys('75')
    
        init_int=browser.find_element_by_xpath('//*[@id="min_interest_rate"]')
        init_int.send_keys('9')
        
        max_int=browser.find_element_by_xpath('//*[@id="max_interest_rate"]')
        max_int.send_keys('10.25')
    
        tenure=browser.find_element_by_xpath('//*[@id="max_loan_tennure"]')
        tenure.send_keys('13')
    
        dropdown=browser.find_element_by_xpath('//*[@id="collateral_required"]/option[2]').click()
    
        browser.find_element_by_xpath('//*[@id="submit_offer"]').click()
    
        df['Bid Status'][i]='Done'
    except:
        print("Already bid for {}".format(i))
        df['Bid Status'][i]='Already Done'
        
   
    
    
    
    
    