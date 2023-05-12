#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
rankings_colname=['label','title','text']
agnews_train = pd.read_csv('train.csv',encoding='utf-8',engine='python',header=None,names=rankings_colname)
agnews_train  


# In[16]:


import re
def text_clear(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]',' ',text)    #clean
    text = re.sub(r' +',' ',text)   # replace space
    text = text.strip()     #delete space
    return text


# In[17]:


import csv
import numpy as np
agnews_label = []
agnews_title = []
agnews_text = []

agnews_train = csv.reader(open('train.csv','r'))
for line in agnews_train:
     ## for number and text
     #print(line)
     agnews_label.append(np.float32(line[0]))
     agnews_title.append(line[1])
     agnews_text.append(text_clear(line[2]))
merge = pd.DataFrame({
    'label':agnews_label,
    'title':agnews_title,
    'text':agnews_text
})
merge  


# In[18]:


merge.to_csv('cleaned_data.csv', index=False)


# In[ ]:




