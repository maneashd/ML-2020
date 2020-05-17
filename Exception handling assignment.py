#!/usr/bin/env python
# coding: utf-8

# 1. Write a function to compute 5/0 and use try/except to catch the exceptions.

# In[6]:


def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Do not divide a number by ZERO!!")
except:
    print("Any other exception")


# 2. Implement a Python program to generate all sentences where subject is in
# ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
# ["Baseball","cricket"].

# In[7]:


subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]


sentence_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
 print (sentence)


# In[ ]:




