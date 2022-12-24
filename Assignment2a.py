#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from
#a given list of non-empty tuples
list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def element(tuple_item):
    return tuple_item[-1]

list2 = sorted(list1, key=element)
print(list2)


# In[ ]:




