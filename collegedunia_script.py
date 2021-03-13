# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 12:56:01 2021

@author: prabh
Script to Scape collegedunia.com US college-wise data 
"""
import numpy as np
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#get list of all college names
df=pd.read_csv('Colleges_link_final.csv')
college_list=df['Colleges'].unique().tolist()

#initiate chromedriver
browser=webdriver.Chrome('chromedriver.exe')
browser.maximize_window()
#Instantiating the Dataframe
column_name=['College','Course_name','fees_1st_year','duration','course_type']
database=pd.DataFrame(columns=column_name)

#lists to store colleges with no_masters 
no_masters=[]
for i in range(len(college_list)):
    #go to collegedunia.com/USA site
    
    c_link=df['Link'][i]
    browser.get(c_link)

    #search=browser.find_element_by_id('home-search')
    #search.clear()
    #time.sleep(5)
    #search.send_keys(c)      
    #time.sleep(5)
    try:
        #searches=browser.find_element_by_xpath('//div[@class="results_lists"]/ul/li[1]/a')
        #browser.get(searches.get_attribute('href'))
    
        if i==0:
             #WAIT TIME == 30s added to close the POPUP
             time.sleep(5)
             browser.find_element_by_xpath('//button[@class="jsx-1878022974 close bg-white"]').click()
             time.sleep(35)
             browser.find_element_by_xpath('//div[@class="jsx-601813733 lead-close-icon pointer"]').click()
             
        else:
            pass
        prog=browser.find_element_by_xpath('//div[@class="jsx-2373615511 jsx-45449386 position-relative d-flex mx-8 silo-navbar-parent undefined"]/ul/li[2]/a')
        browser.get(prog.get_attribute('href'))
        time.sleep(15)
        try:
            browser.find_element_by_xpath('//label[@for="Levels-Master"]').click()
        
        
        #sort by fees highest to lowest
            browser.find_element_by_xpath('//div/span[@class="jsx-3840022005 pointer position-relative sort-link font-weight-bold "][1]').click()
        
        #courses_names
            courses=browser.find_elements_by_xpath('//h3/a[@class="jsx-2254962254 jsx-2349121475"]')
            course_list=[]
            for p in courses:
                course_list.append(p.text)
        
        #fees 
            fee_list=[]
            fee=browser.find_elements_by_xpath('//div/span[@class="jsx-2254962254 jsx-2349121475 fees font-weight-bolder"]')
            for q in fee:
                fee_list.append(q.text)            
        #filling blank-data w/ NaN
            diff=len(course_list)-len(fee_list)
            for b in range(diff):
                fee_list.append(np.nan)
        
        #duration
            course_duration=[]
            dur=browser.find_elements_by_xpath('//div[@class="jsx-2254962254 jsx-2349121475 d-flex justify-content-between align-items-center"]/div[1]/div/p[@class="jsx-2254962254 jsx-2349121475 item-head m-0 pb-1 text-primary text-lg text-uppercase"]')
            for r in dur:
                course_duration.append(r.text)
        #filling blank-data w/ NaN        
            diff_duration=len(course_list)-len(course_duration)
            for c in range(diff_duration):
                    course_duration.append(np.nan)
        
        #course_type
            course_type=[]
            c_type=browser.find_elements_by_xpath('//div/span[@class="jsx-2254962254 jsx-2349121475 card-subheading text-md text-uppercase"]')
            for s in c_type:
                course_type.append(s.text)
        #filling blank-data w/ NaN        
            diff_type=len(course_list)-len(course_type)
            for d in range(diff_type):
                course_type.append(np.nan)
            
        #college_name list(repaeated values of 1 college name)
            college_name=browser.title
            college=[]
            college.extend([college_name for t in range(len(course_list))])
        
        #instantiating a iterative df
            iter_df=pd.DataFrame({'College':college,
                                  'Course_name':course_list,
                                  'fees_1st_year':fee_list,
                                  'duration':course_duration,
                                  'course_type':course_type})
        
        #adding values to the database dataframe
            database=database.append(iter_df,ignore_index=True)
            
            
        except:
            print('{} does not have Masters'.format(college_list[i]))
            no_masters.append(college_list[i])
    except:
        
        continue
      
#exporting dataframe into .csv
database.to_csv('Main.csv',index=False)

    
    
no_masters
    
        
    
        
   
  


