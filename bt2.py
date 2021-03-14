#!/usr/bin/env python
# coding: utf-8

# THỰC HÀNH VẼ BIỂU ĐỒ CHO DỮ LIỆU ĐỊNH LƯỢNG

# In[3]:


#Nhập các thư viện cần thiết
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# In[4]:


#Đọc dữ liệu
mb_df = pd.read_csv("microbiome.csv")
mb_df.head()


# Vẽ Box plot

# In[5]:


mb_df['Tissue'].plot(kind='box')


# Bài tập: Hãy cải tiến biểu đồ box plot trên để đẹp hơn

# In[8]:


sns.boxplot(data =mb_df['Tissue'])


# VẼ SCATTER PLOT VỚI 2 TRỤC LÀ TISSUE - STOOL

# In[9]:


mb_df_2 = mb_df[['Tissue', 'Stool']]
mb_df_2.head()


# In[10]:


mb_df_2.plot.scatter(x = 'Tissue', y = 'Stool')


# Bài tập: Hãy chỉnh sửa để biểu đồ đẹp hơn

# In[16]:


sns.jointplot(x = 'Tissue', y = 'Stool', data = mb_df, kind = 'kde', color = 'green')


# VẼ HISTOGRAM

# In[17]:


mb_df['Stool'].plot(kind='hist')


# In[18]:


mb_df['Stool'].plot(kind='hist', cumulative= True)


# In[19]:


mb_df['Stool'].plot(kind='hist', cumulative= True, bins = 50)


# Bài tập: Hãy làm đẹp biểu đồ trên

# In[24]:


sns.displot(mb_df['Stool'],bins = 5,kde = True, rug = True)


# In[ ]:




