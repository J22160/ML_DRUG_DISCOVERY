#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from chembl_webresource_client.new_client import new_client


# In[3]:


target = new_client.target
target_query = target.search('FLT3')
targets = pd.DataFrame.from_dict(target_query)
targets


# In[4]:


selected_target = targets.target_chembl_id[1]
selected_target


# In[5]:


activity = new_client.activity
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")


# In[13]:


df = pd.DataFrame.from_dict(res)


# In[14]:


df.shape


# In[11]:


df2 = df[df.standard_value.notna()]
df2


# In[16]:


df2_nr = df2.drop_duplicates(['canonical_smiles'])
df2_nr


# In[15]:


selection = ['molecule_chembl_id','canonical_smiles','standard_value']
df3 = df2[selection]
df3


# In[17]:


bioactivity_threshold = []
for i in df3.standard_value:
    if float(i) >= 10000:
        bioactivity_threshold.append("inactive")
    elif float(i) <= 1000:
        bioactivity_threshold.append("active")
    else:
        bioactivity_threshold.append("intermediate")


# In[18]:


bioactivity_class = pd.Series(bioactivity_threshold, name='bioactivity')
df5 = pd.concat([df3, bioactivity_class], axis=1)
df5


# In[19]:


df5.bioactivity.value_counts()


# In[20]:


df5.to_csv('TPKR_data2.csv',index=False)

