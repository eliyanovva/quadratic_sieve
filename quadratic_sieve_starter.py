#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
def gcd(a, b):
    if (a==0 or b==0):
        return 0
    r = b%a
    if r==0:
        return b//a
    if r==1:
        return 1
    return gcd(b, r)


# In[3]:


print("gcd of 7 and 14 is: ", str(gcd(7, 14)))
print("gcd of 57 and 768 is: ", str(gcd(57, 768)))


# In[28]:


def eratosthenes(bound):
    start = 2
    marked = []
    unmarked = set([x for x in range(bound)])
    unmarked.remove(0)
    unmarked.remove(1)
    repeat_list = []
    q = 2
    for u in unmarked:
        #print(u)
        if u> int(bound**0.5):      # only check numbers up to sqrt(bound)
            break
        while u*q<= bound:
            repeat_list.append(u*q)
            unmarked = unmarked - set(repeat_list)
            q+=1
        #print(unmarked)
        q = 2

    return (repeat_list, unmarked)


# In[29]:


bound = 25
result = eratosthenes(bound)
print(result)


# In[ ]:


def check_B_smooth(num):
    return True

