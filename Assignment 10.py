#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print ('How old are you?')

age= int(input())

print ('Do you smoke? (Yes or No)')

cigarette=input()

print('Is your immune system too weak?(Yes or No)')

immune_system = input()

if age > 75 :

    age = True

else:

    age = False

if cigarette == False :

    cigarette = True

else:

    cigarette=False

if immune_system == False:

    immune_system = True

else:

    immune_system = False

    

bool_val= age or cigarette or immune_system

print(bool_val)


# In[ ]:


#Task : Estimating the risk of death from coronavirus. Write a program that;

#Takes "Yes" or "No" from the user as an answer to the following questions :

#Are you a cigarette addict older than 75 years old? Variable → age

#Do you have a severe chronic disease? Variable → chronic

#Is your immune system too weak? Variable → immune

#Set a logical algorithm using boolean logic operators (and/or) and use if-statements with the given variables 
#in order to print out us a message : "You are in risky group"(if True ) or "You are not in risky group" (if False).

