#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#In the Gregorian calendar, three criteria must be taken into account to identify leap years:
#The year must be evenly divisible by 4;
#If the year can also be evenly divided by 100, it is not a leap year; unless...
#The year is also evenly divisible by 400. Then it is a leap year.
#According to these rules, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, 
#and 2500 are not the leap years.
#Write a Python program that prints such as "2020 is a leap year" if the given year by the user 
#is a leap year, prints such as "2019 is not a leap year" otherwise.


# In[1]:


year=int(input('Please enter a year to check if it is leap year: '))

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))


# In[ ]:




