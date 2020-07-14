#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.


# In[ ]:


number=int(input("please enter a number to check if it is a prime number or not:"))
    
for i in range (2,number):
    if (number % i == 0):
        print("it is not a prime number")
    else:
        print("it is a prime number")
    break

