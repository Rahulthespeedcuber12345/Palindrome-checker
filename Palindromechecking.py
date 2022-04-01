#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Author : Rahul Krishnan H
Objective : palindromechecking is a function used for checking whether a string is a palindrome or not.
'''


# In[2]:


def palindromechecking(palindrome):
    firstindex = 0
    lastindex = len(palindrome) - 1
    firstcharacter = palindrome[firstindex]
    lastcharacter = palindrome[lastindex]
        
#below code is to verify whether input is a palindrome
    while firstcharacter == lastcharacter:
        firstindex = firstindex + 1
        lastindex = lastindex - 1
        firstcharacter = palindrome[firstindex]
        lastcharacter = palindrome[lastindex]
    
        if firstindex == lastindex:
            print(f"{palindrome} is a palindrome")
            break
    
#below code is to verify whether input is not a palindrome
        if firstcharacter != lastcharacter:  
            print(f"{palindrome} is not a palindrome")
        


# In[7]:


palindromechecking("malayalam")


# In[ ]:




