#!/usr/bin/env python
# coding: utf-8

# In[2]:


def make_resistance(data):
    data['코로나저항력'] = (data['물섭취빈도']*np.random.randint(1,4)) + (data['손세척빈도']*np.random.randint(1,4)) + (data['마스크착용빈도']*np.random.randint(1,4)) + (data['스마트폰사용빈도']*np.random.randint(0,1))+ (data['운동빈도']*np.random.randint(1,4))
    return data


# In[4]:


def make_resistance(data):
    data['코로나저항력'] = (data['물섭취빈도']*1.5) + (data['손세척빈도']*2) + (data['마스크착용빈도']*3) + (data['스마트폰사용빈도']*0.9)+ (data['운동빈도']*2)
    return data


# In[ ]:




