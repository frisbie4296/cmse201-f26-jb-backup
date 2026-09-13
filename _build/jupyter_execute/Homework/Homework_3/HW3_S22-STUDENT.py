#!/usr/bin/env python
# coding: utf-8

# # Homework 3: Pandas data analysis

# ### <p style="text-align: right;"> &#9989; **Put your name here** </p>

# # __CMSE  201 &ndash; Spring 2022__
# 
# <img src="https://cmse.msu.edu/sites/_cmse/assets/Image/image002.jpg"
#      alt="CMSE Logo"
#      align="right" 
#      height="100" 
#      width="100" />
# 
# 
# 
# ## Learning Goals
# 
# * Load data into notebooks using Pandas
# * Determine the components of the data
# * Make meaningful visual representations of the data
# * Draw conclusions from statistical analysis 
# 
# ___

# ## Assignment instructions
# 
# Work through the following assignment, making sure to follow all of the directions and answer all of the questions.
# 
# **This assignment is due at 11:59pm on Friday, Feb. 25th** 
# 
# It should be uploaded into D2L Homework #3.  Submission instructions can be found at the end of the notebook.

# ## Grading
# 
# - Academic integrity statement: 1 pt
# - Part 0: Revisit plotting in HW2: 6 pts
# - Part 1: Reading, Describing, and Cleaning the Data: 22 pts
# - Part 2: Data analysis: 21 pts
# 
# **Total:** 50 pts
# 

# ## Academic integrity statement (1 point)
# 
# In the markdown cell below, paste your personal academic integrity statement. By including this statement, you are confirming that you are submitting this as your own work and not that of someone else.

# <font size=6 color="#009600">&#9998;</font> *Put your personal academic integrity statement here.*

# Before we read in the data and begin working with it, let's import the libraries that we would typically use for this task. You can always come back to this cell and import additional libraries that you need.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Part 0: Revisit plotting in HW2 (6 total points)

# In question 4 of HW2, we consider two equations that give the (x,y) points for values of k (ranging from 0 to 9000). When all 9000 points are plotted, you will see that it draws out a flower design.
# 
# $x(k) = \mathrm{cos}\Big(\frac{14 \pi k}{9000}\Big)\Big(1-\frac{3}{4}\mathrm{sin}\Big(\frac{20\pi k}{9000}\Big)-\frac{1}{4}\mathrm{cos}\Big(\frac{60 \pi k}{9000}\Big)\Big)$
# 
# $y(k) = \mathrm{sin}\Big(\frac{14 \pi k}{9000}\Big)\Big(1-\frac{3}{4}\mathrm{sin}\Big(\frac{20\pi k}{9000}\Big)-\frac{1}{4}\mathrm{cos}\Big(\frac{60 \pi k}{9000}\Big)\Big)$
# 
# The goal here is to revisit this problem, and achieve the same purpose by using numpy arrary and functions. Now the code will be much shorter. (Note: in this question, you are not allowed to use `list` and you no longer need to define `draw_flower_points` function.)
# 
# <font size=8 color="#009600">&#9998;</font> Do This - Write a piece of code to define `k` as a numpy array ranging from 0 to 9000 with 500 points. (2 points) Use `np.sin` and `np.cos` to define `x_k` and `y_k` as the corresponding numpy. (3 points) Then plot the final flower design. (1 point)
# 

# In[15]:


## your code here


# ### Part 1: Reading, Describing, and Cleaning the Data (22 total points)
# 

# The United Nations compiles an annual publication called the [World Happiness Report](https://en.wikipedia.org/wiki/World_Happiness_Report) that ranks countries by the "happiness score" or "life ladder". These scores are based on a surveys of citizens of each country on a variety of factors such as:
# * Gross Domestic Product (GDP) per capita
# * Perceptions of social support
# * Life expectancy
# * Freedom of choice
# 
# [Data from the UN](https://worldhappiness.report/) is available from 2005-2019, which we have downloaded in a `.csv` format. The survey has changed over time, so that some factors and questions have been omitted. So some of the data is incomplete or missing.
# 
# ### 1.1 Read the data (4 points)
# 
# <font size=8 color="#009600">&#9998;</font> Do This - Read in the survey data from `happiness_index.csv` into a DataFrame and print the `.head()` of the data, use `describe` to get a feel of this dataset.

# In[ ]:


## your code here


# ### 1.2 Clean the data (8 total points)
# 
# #### 1.2.1 Remove and track excess data (2 points)
# 
# We need to remove the excess features that are not present in every year's data. 
# 
# <font size=8 color="#009600">&#9998;</font> Do This - Drop the columns that are not the following:
# * Country name
# * year
# * Life Ladder
# * Log GDP per capita
# * Social support
# * Healthy life expectancy at birth
# * Freedom to make life choices
# * Generosity
# * Perceptions of corruption
# * Positive affect
# * Negative affect
# * Confidence in national government
# * Democratic Quality
# * Delivery Quality
# 
# Make sure to make a list of the columns that you dropped. This is important if you need to report what you didn't consider in the model. Print the `.head()` of the DataFrame after dropping the unneeded columns.

# In[ ]:


## your code here


# #### 1.2.2 Focus on the 2018 data (3 points)
# 
# Your data should include scores for a variety of years (2005-2019) for each country. Let's focus on a single year: 2018. 
# 
# <font size=8 color="#009600">&#9998;</font> Do This - Use mask to filter your data to focus only on the latest available data from 2018. Print the `.head()` of that DataFrame.

# In[ ]:


## your code here


# #### 1.2.3 Missing data (3 points)
# 
# Not all the countries have reported values for every feature. You should check if any countries have missing data. We could impute these missing data in a variety of ways, but instead to make our work a little simpler, we will simply drop a country if it has any missing data.  
# 
# <font size=8 color="#009600">&#9998;</font> Do This - Drop any country from the data that is missing data.

# In[ ]:


## your code here


# ### 1.3 Describe the data (10 points)
# 
# Now that you have a cleaned data set, let's look into the data. We can start that by describing the data and making histograms of it. 
# 
# <font size=8 color="#009600">&#9998;</font> Do This - Focusing on the data collected in the survey (i.e., not the country name or year), *describe* the data by using the `describe` function in pandas. (2 points)

# In[ ]:


## your code here


# <font size=8 color="#009600">&#9998;</font> Do This - We can use numpy functions to verify what we have obtained in the description in the previous part. Define a Numpy array to be the same as the column of data corresponding to the feature 'Life Ladder'. Use Numpy functions to compute the mean and the standard deviation of this array. Does it agree with what you had from the previous question? (4 points)

# In[ ]:


## your code here


# <font size=8 color="#009600">&#9998;</font> Do This -Make histograms describing the distributions of all the features. (4 points)

# In[ ]:


## your code here


# ## Part 2: Data analysis (21 total points)
# 
# Now  we will analyze the cleaned dataset.
# 
# ### 2.1 The ranking (12 points)
# 
# The rankings of national happiness are based on a Cantril ladder survey. Nationally representative samples of respondents are asked to think of a ladder, with the best possible life for them being a 10, and the worst possible life being a 0.  This is represented by 'Life Ladder' in the dataset.
# 
# 
# <font size=8 color="#009600">&#9998;</font> Do This - Reorder the dataframe   according to descending values of the 'Life Ladder' score using `sort_values` (Refer to  (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values). Which are the top 3 happiest  countries? (4 points)

# In[ ]:


## your code here


# <font size=8 color="#009600">&#9998;</font> Do This -  Replace the index of the sorted dataframe to be the ranking of the ranking of the country. (4 points)

# In[ ]:


## your code here


# <font size=8 color="#009600">&#9998;</font> Do this - Use mask to find the United States in this ranking. What's the ranking of the U.S.? (4 points)

# In[ ]:


## your code here


# ### 2.2 Determining which features will matter (9 points)
# 
# We want to understand what variables matters for people's happiness. We will do this by starting the correlation of the features with `Life Ladder`.
# 
# <font size=8 color="#009600">&#9998;</font> Do this - Make   `scatter` plots of `Life Ladder` vs. all other features. (5 points)  

# In[ ]:


## your code here


# <font size=8 color="#009600">&#9998;</font> Do this -  Look at your plots, for each feature, is it correlated to `Life Ladder`? If so, is it positively or negatively correlated? Explain your reasoning (4 points)

# <font size=6 color="#009600">&#9998;</font> Write your answer here

# ---
# 
# ### Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "Homework Assignments" section, find the submission folder link for Homework #3, and upload it there.

# &#169; Copyright Michigan State University Board of Trustees
