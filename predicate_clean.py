#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import re

input_file = 'predicates_test.csv'  # 输入表格文件名
output_file = 'predicate.csv'  # 输出表格文件名

# 定义正则表达式模式，用于匹配数字和点号
pattern = r'\d+|\.'

# 读取输入表格文件并处理数据
with open(input_file, 'r') as f_in, open(output_file, 'w', newline='') as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)

    for row in reader:
        processed_row = []
        for cell in row:
            # 去除数字和点号
            processed_cell = re.sub(pattern, '', cell)
            processed_row.append(processed_cell)

        writer.writerow(processed_row)

print("处理完成，结果保存到output.csv文件中。")


# In[ ]:




