#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load Dataset
data = pd.read_csv("E:\Internship\Data.csv")


# In[3]:


# Display the first 10 rows of the dataset
print(data.head(10))


# In[4]:


## Analyze the Relationship Between Cuisine Types and Restaurant Ratings
## Identify the Top 10 Cuisines


# In[5]:


# Identify the top 10 most frequent cuisines
top_cuisines = data['Cuisine Style'].value_counts().head(10).index.tolist()


# In[6]:


# Filter the dataset to include only the top 10 cuisines
data_top_cuisines = data[data['Cuisine Style'].isin(top_cuisines)]


# In[8]:


# Visualize the distribution of ratings for each cuisine type (top 10) using a box plot
plt.figure(figsize=(12, 8))
sns.boxplot(x='Cuisine Style', y='Rating', data=data_top_cuisines)
plt.xticks(rotation=45)
plt.xlabel('Cuisine Type')
plt.ylabel('Rating')
plt.title('Rating Distribution by Cuisine Type')
plt.show()


# In[9]:


# Group the data by cuisine type and calculate the total number of votes for each cuisine
popular_cuisines = data.groupby('Cuisine Style')['Number of Votes'].sum().reset_index()


# In[10]:


# Sort the cuisines by total votes in descending order
popular_cuisines = popular_cuisines.sort_values(by='Number of Votes', ascending=False)


# In[11]:


# Display the top 10 most popular cuisines based on total votes
print(popular_cuisines.head(10))


# In[12]:


# Calculate the average rating for each cuisine type
average_ratings = data.groupby('Cuisine Style')['Rating'].mean().reset_index()


# In[13]:


# Sort the cuisines by average rating in descending order
average_ratings = average_ratings.sort_values(by='Rating', ascending=False)


# In[14]:


# Display the top 10 cuisines with the highest average ratings
print(average_ratings.head(10))

