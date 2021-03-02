#!/usr/bin/env python
# coding: utf-8

# In[2]:


def lead_counter(filepath):
    import pandas as pd
    df=pd.read_csv(filepath,low_memory=False)
    
    #Counselling Lead == 'Yes'
    csly_df=df.loc[df['Counselling Lead']=='Yes']
    
    #retrieve Loan Lead =['No','NaN']
    loan_lead=csly_df.loc[csly_df['Loan Lead']!='Yes']
    #retrieve BA Lead =['No','NaN']
    ba_lead=loan_lead.loc[loan_lead['BA Lead']!='Yes']
    
    #create dataframe storing Lead Source Counts
    count_df=ba_lead['Lead Source'].value_counts(dropna=False).rename_axis("Lead Source").reset_index(name='Counts')
    
    #exporting Datasets into CSV formats
    count_df.to_csv('count_leads.csv',index=False)
    ba_lead.to_csv('lead_2021.csv',index=False)    
    


# In[ ]:


lead_counter('2021.csv')

