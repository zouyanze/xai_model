#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
import torch
from tqdm import tqdm  # 导入tqdm库

# 从Hugging Face加载AG News数据集
from datasets import load_dataset

agnews_dataset = load_dataset("ag_news")
texts = agnews_dataset["train"]["text"][-10:]  # 获取最后一百条新闻数据
# 加载谓词表格文件
predicate_df = pd.read_csv("predicate.csv")
predicates = predicate_df['predicate'].tolist()

# 加载BERT模型和tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# 创建空的结果矩阵
result_matrix = [[0.0] * len(predicates) for _ in range(len(texts))]

# 遍历文本数据集和谓词列表
for i, text in enumerate(tqdm(texts)):  # 使用tqdm显示进度条
    for j, predicate in enumerate(predicates):
        # 构建问题并进行编码
        question = f"{text} {predicate}, yes or no?"
        inputs = tokenizer.encode_plus(
            question,
            add_special_tokens=True,
            return_tensors="pt"
        )

        # 推理并获取分类结果
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            probabilities = torch.softmax(logits, dim=1)[0]

        # 获取"Yes"和"No"的概率
        yes_probability = probabilities[1].item()
        no_probability = probabilities[0].item()

        # 计算"Yes"和"No"的概率比例
        probability_ratio = yes_probability / no_probability

        # 将比例存储到结果矩阵中
        result_matrix[i][j] = probability_ratio

# 将结果保存为CSV文件
result_df = pd.DataFrame(result_matrix, columns=predicates)
result_df.to_csv('result_matrix_10.csv', index=False)


# In[ ]:




