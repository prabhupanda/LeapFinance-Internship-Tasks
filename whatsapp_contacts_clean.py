#!/usr/bin/env python
# coding: utf-8

# In[1]:


def contact_exported(file):
    import re
    import pandas as pd
    f=open(file,'r')
    num=[]
    for i in f:
        num.append(i)
    text=num[0]
    filename=str(file)
    #delete spaces
    unspaced_text=text.replace(" ","")
    
    #remove +91 tags
#     untagged_text1=unspaced_text.replace("+1","")
    untagged_text=unspaced_text.replace("+91","")
    unhyphenated_text=untagged_text.replace('-',"")
    
    #extract comma-separated text into list
    split_list=unhyphenated_text.split(",")
    
    #store list data in pd DataFrame
    df=pd.DataFrame({'Contact No.':split_list})
    
    #exporting df into xlsx format
    df.to_excel(filename+str('.xlsx'),index=False)
    


# In[ ]:


'''V.V.Imp The Text file must be renamed as confile.txt for the script to work'''
contact_exported('confile.txt')

