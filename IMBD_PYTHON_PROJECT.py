#!/usr/bin/env python
# coding: utf-8

# # IMBD_PYTHON_PROJECT.

# In[31]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[32]:


df = pd.read_csv("movies.csv").head(10)
print(df)


# In[33]:


df.describe()


# In[34]:


df.info()


# # 1. plot a graph to show the distribution of genre in the top 20 movies.

# In[35]:


df1 = df.groupby("genre").agg({"movie_id":"count"})
print(df1)


# In[57]:


plt.pie(data = df1,x = 'movie_id', autopct = '%1.2f%%',explode=[0,0,0,0,0.1,0],labels=df1.index,shadow=True,radius=1.2,pctdistance=0.7)
plt.title("Distribution of genre 10 movies.",pad=35)
plt.show()


# # CONCLUSIN
# #In conclusion, the data analysis reveals a strong viewer preference for crime dramas, signaling a significant interest in narratives involving criminal activities and intense drama. This finding has valuable implications for content creators, enabling them to develop targeted and captivating content that aligns with audience preferences.
# 

# # 2. find out which movie has the maximum number of votes and which genre it belongs to and its duration.

# In[ ]:


# change the "imbd_votes" value string to Int.
df["imbd_votes"]=df["imbd_votes"].astype(str).str.replace(",","").astype(int)
df.info()


# In[72]:


_df = df['imbd_votes'].idxmax()
new_df = df.loc[_df]
title = new_df['title']
genre = new_df['genre']
duration = new_df['duration']
print("Title :",title)
print("Genre :",genre)
print("Duration :",duration)


# # 3. find out which movie has the minimum number of votes and which genre it belongs to and its duration.
# 

# In[76]:


m_df = df['imbd_votes'].idxmin()
mini = df.loc[m_df]
title_ = mini['title']
genre_ = mini['genre']
duration_ = mini['duration']
print("Title :",title_)
print("Genre :",genre_)
print("Duration :",duration)


# # 4. find out movies of each genre which has maximum number of votes. 

# In[78]:


max_genre = df.groupby('genre').agg({"imbd_votes":"max"})
print(max_genre)


# In[102]:


max_genre_sorted = max_genre.sort_values(by="imbd_votes", ascending=False)
colors = sns.color_palette("Set3", len(max_genre_sorted))
plt.figure(figsize=(10, 6))
plt.bar(max_genre_sorted.index, max_genre_sorted["imbd_votes"], color=colors)
plt.xlabel("Genre")
plt.ylabel("Maximum Number of Votes")
plt.title("Movies of Each Genre with Maximum Votes")
plt.xticks(rotation=90)
plt.show()


# # Conclusion
# The bar chart analysis showcases genres with the highest votes, offering valuable insights for content creators and industry professionals. This information aids in understanding audience preferences and informs targeted content development strategies.
