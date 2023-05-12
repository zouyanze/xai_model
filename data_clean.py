#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
rankings_colname=['label','title','text']
agnews_train = pd.read_csv('train.csv',encoding='utf-8',engine='python',header=None,names=rankings_colname)
agnews_train  ##结果如下图


# In[16]:


import re
def text_clear(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]',' ',text)    #用空格替换非标准字符，^为求反操作
    text = re.sub(r' +',' ',text)   # 替换多重空格为单空格
    text = text.strip()     #去除首尾空格
    return text


# In[17]:


import csv
import numpy as np
agnews_label = []
agnews_title = []
agnews_text = []
## 便于处理数据
agnews_train = csv.reader(open('train.csv','r'))
for line in agnews_train:
     ## 对于数字，得数字化转换；对于文字，得格式处理
     #print(line)
     agnews_label.append(np.float32(line[0]))
     agnews_title.append(line[1])
     agnews_text.append(text_clear(line[2]))
merge = pd.DataFrame({
    'label':agnews_label,
    'title':agnews_title,
    'text':agnews_text
})
merge  ##可观察到处理后的数据与原始数据的不同


# In[18]:


merge.to_csv('cleaned_data.csv', index=False)


# In[ ]:




