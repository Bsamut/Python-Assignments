#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a Python program that;
#takes a positive integer number from the user,
#checks the entered number if it is Armstrong,
#consider the negative, float and any entries other than numeric values then display a warning message to the user.


# In[ ]:


number=int(input("Please input a positive integer number:"))

if type(number)==float:
    print ("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    number=input("Please input a positive integer number:")
else:

    n=len(str(number))
    i=0
    sum=0

    for i in range(0,n):
        a=str(number)
        a[i]

        b=int(a[i])
        us=int(a[i])**n
        sum = sum + us
        if sum == number :
            print("it is an amstrong number")
        else:
            print("it is not an amstrong number")

