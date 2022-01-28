#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import haversine as hs


# In[3]:


store_loc=pd.read_excel('JPLocations.xlsx')
Fran_loc=pd.read_excel("FLocations.xlsx")


# In[4]:


store_loc['coor'] = list(zip(store_loc.Latitude, store_loc.Longitude))
Fran_loc['coor'] = list(zip(Fran_loc.Latitude, Fran_loc.Longitude))


# In[5]:


Fran_loc.head()


# In[6]:


def distance_from(loc1,loc2): 
    dist=hs.haversine(loc1,loc2)
    return round(dist,2)


# In[7]:


for _,row in Fran_loc.iterrows():
    store_loc[row.Fran]=store_loc['coor'].apply(lambda x: distance_from(row.coor,x))


# In[8]:


store_loc.head()


# In[9]:


store_loc.to_excel (r'Pathofyourfile.xlsx', index = False, header=True)


# In[ ]:




