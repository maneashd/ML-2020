#!/usr/bin/env python
# coding: utf-8

# Data for pandas practice https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv

# In[52]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp


# the data

# In[53]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'


# read the file

# In[89]:


df = pd.read_csv(url, sep= '\t', engine='python')


# Print first five records

# In[90]:


df.head(5)


# pront last 7 records

# In[91]:


df.tail(7)


# print total records

# In[92]:


df.info()


# In[93]:


df.shape[0]


# In[94]:


df.columns


# In[95]:


df.index


# which was the most ordered item? and how many items were orderd?

# In[96]:


c = df.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)


# what was the most orderd item in the choice_description column?

# In[97]:


c = df.groupby('choice_description').sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)


# In[102]:


# delete the duplicates in item_name and quantity
filtered = df.drop_duplicates(['item_name','quantity'])
# select only the products with quantity equals to 1
one_prod = filtered[filtered.quantity == 1]
# select only the item_name and item_price columns
price_per_item = one_prod[['item_name', 'item_price']]
# sort the values from the most to less expensive
price_per_item.sort_values(by = "item_price", ascending = False)


# In[103]:


#What was the quantity of the most expensive item ordered?
df.sort_values(by = "item_price", ascending = False).head(1)


# In[104]:


#How many times were a Veggie Salad Bowl ordered?


# In[105]:


df[df.item_name =='Veggie Salad Bowl']


# In[ ]:




