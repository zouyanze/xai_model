#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai

openai.organization = "org-NZgIWsu3pZWTFDSQiEgY2RDL"
openai.api_key = "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"
res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You're a news editor."},
        {"role": "user", "content": "Can you give 100 predicates for each of the different categories of news?"},
        {"role": "assistant", "content": "Yes,but can you tell me which categories there are?"},
        {"role": "user", "content": "There are four categories of news: Business, Sci/Tech, World and Sports.Please format the predicate similarly:  is talking about politics or is related to Iraq"},
    ]
)
print(res['choices'][0]['message']['content'])


# In[2]:


import pandas as pd

# extract predicate
predicates = res['choices'][0]['message']['content'].split('\n')

# build DataFrame
df = pd.DataFrame({'Predicate': predicates})

# save
df.to_csv('predicates.csv', index=False)

print(f"Predicates saved to predicates.csv.")

