#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.


# In[32]:


n1=0
n2=1
count=0

while n1 <= 56:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count +=1
    

