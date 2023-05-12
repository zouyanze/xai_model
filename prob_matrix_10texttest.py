#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
import torch
from tqdm import tqdm  # just for monitor

from datasets import load_dataset

agnews_dataset = load_dataset("ag_news")
texts = agnews_dataset["train"]["text"][-10:]  # last 100 for test

predicate_df = pd.read_csv("predicate.csv")
predicates = predicate_df['predicate'].tolist()

# BERT and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# empty matrix
result_matrix = [[0.0] * len(predicates) for _ in range(len(texts))]


for i, text in enumerate(tqdm(texts)):  
    for j, predicate in enumerate(predicates):
        
        question = f"{text} {predicate}, yes or no?"
        inputs = tokenizer.encode_plus(
            question,
            add_special_tokens=True,
            return_tensors="pt"
        )

        
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            probabilities = torch.softmax(logits, dim=1)[0]

        # get probabilities
        yes_probability = probabilities[1].item()
        no_probability = probabilities[0].item()

        # get ratio
        probability_ratio = yes_probability / no_probability

        # save ratio
        result_matrix[i][j] = probability_ratio


result_df = pd.DataFrame(result_matrix, columns=predicates)
result_df.to_csv('result_matrix_10.csv', index=False)


# In[ ]:




