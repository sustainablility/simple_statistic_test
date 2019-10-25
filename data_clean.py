#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 08:19:42 2018

@author: zzxxq
"""


# In[2]:


from numpy import *
import pandas as pd
import os


# In[3]:


path='./'
filename = "test.json"
#filelist=os.listdir(path)
#filelist=[item for item in filelist if item.endswith('.json')]
#print os.path.exists(path)


# In[4]:


tweet = None
user_info = None


# In[5]:


#for k,item in enumerate(filelist):
#    if k==0:
data=pd.read_json(path+filename)

user_info=data.groupby('userid',as_index=False).first()
#print user_info
#print "======================================================================================="
#print
user_info=user_info[['tweetid','userid','postdate','latitude','longitude',
                     'message','statusescount','friendscount','followerscount']]
#print user_info
#print "======================================================================================="
#print
tweet=data[['userid','tweetid','postdate','statusescount','friendscount','followerscount']]
#print tweet
#print "======================================================================================="
#print
        


# In[6]:


#print tweet
#print
#print user_info


# In[7]:


tweet['tweetid']=tweet['tweetid'].map(lambda x:str(x))
tweet['postdate']=tweet['postdate'].map(lambda x:int(str(x).split('T')[0].split(' ')[0].replace('-','').replace('/','')))


# In[7]:


#print tweet


# In[8]:


date_list=[20170801+i for i in range(31)]+[20170901+i for i in range(30)]
tweet['date_range']=-1


# In[9]:


#print date_list


# In[10]:


for k,date in enumerate(date_list):#range(len(date_list)-1):
    #print k
    #print date
    tweet['day_'+str(k)]=0
    tweet['day_'+str(k)][tweet['postdate']<=date]=1


# In[11]:


#print tweet


# In[12]:


tweet1=tweet[['userid']+['day_'+str(k) for k in range(len(date_list))]].groupby('userid',as_index=False).agg(sum)
user_info=user_info.groupby('userid',as_index=False).first()
user_info=pd.merge(user_info,tweet1,on='userid',how='inner')

#print user_info.head()


# In[14]:


input_data=user_info[['userid','latitude','longitude','statusescount','friendscount','followerscount']+['day_'+str(i) for i in range(60)]]

#with open('input.json', 'w', encoding='utf-8') as file:
input_data.to_json(path+'input.json', force_ascii=False)
#input_data.to_json(path+'input.json',index=False,encoding='utf-8')
#print len(tweet),len(tweet1)
print 'finish!!!'
