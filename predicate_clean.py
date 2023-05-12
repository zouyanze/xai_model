#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import re

input_file = 'predicates_test.csv'  
output_file = 'predicate.csv'  


pattern = r'\d+|\.'


with open(input_file, 'r') as f_in, open(output_file, 'w', newline='') as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)

    for row in reader:
        processed_row = []
        for cell in row:
            # delete number and .
            processed_cell = re.sub(pattern, '', cell)
            processed_row.append(processed_cell)

        writer.writerow(processed_row)



# In[ ]:




