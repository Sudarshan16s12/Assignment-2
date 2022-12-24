#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should
#be corresponding ASCII values
dict = {}
alfa = range(97,123)
for i in alfa:
    dict[chr(i)] = str(i)
print(dict)

