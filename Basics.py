#!/usr/bin/env python
# coding: utf-8

# # My First Data Science Project

# ## Helicopter Escapes!

# We begin by importing some helper functions.

# In[1]:


from helper import *


# ## Get the Data

# Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# In[2]:


url=("https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes")


# In[3]:


data=data_from_url(url)


# Let's print the first three rows

# In[4]:


for row in data[:3]:
    print(row)


# In[5]:


for row in data:
    row[0] = fetch_year(row[0])
    #row[0] = date


# In[6]:


index = 0
for row in data:
    data[index] = row[:-1]
    index += 1


# In[7]:


print(data[:3])


# In[8]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# In[9]:


print(min_year)
print(max_year)


# In[10]:


years = []
for y in range(min_year, max_year + 1):
    years.append(y)


# In[11]:


print(years)


# In[12]:


attempts_per_year = []
for y in years:
    attempts_per_year.append([y, 0])


# In[13]:


for row in data:
    for ya in attempts_per_year:
        y = ya[0]
        if row[0] == y:
            ya[1] += 1
            
print(attempts_per_year)    


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# In[15]:


countries_frequency = df["Country"].value_counts()


# In[16]:


print_pretty_table(countries_frequency)

