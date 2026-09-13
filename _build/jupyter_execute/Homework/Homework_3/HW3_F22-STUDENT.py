#!/usr/bin/env python
# coding: utf-8

# # Homework 3: Pandas Data Analysis

# ### <p style="text-align: right;"> &#9989; **Put your name here** </p>

# # __CMSE  201 &ndash; Fall 2022__
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
# **This assignment is due at 11:59pm on Friday, Oct. 28th** 
# 
# It should be uploaded into D2L Homework #3.  Submission instructions can be found at the end of the notebook.

# ## Grading
# 
# - Academic integrity statement: 1 pt
# - Part 1: Reading, Describing, and Cleaning the Data: 24 pts
# - Part 2: Data analysis: 25 pts
# 
# **Total:** 50 pts
# 

# ## Academic integrity statement (1 point)
# 
# In the markdown cell below, paste your personal academic integrity statement. By including this statement, you are confirming that you are submitting this as your own work and not that of someone else.

# <font size=6 color="#009600">&#9998;</font> *Put your personal academic integrity statement here.*

# Before we read in the data and begin working with it, let's import the libraries that we would typically use for this task. You can always come back to this cell and import additional libraries that you need.

# In[50]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Part 1: Reading, Describing, and Cleaning the Data (22 total points)
# 

# Electric Vehicles becomes more and more popular globaly.  [Open EV Charts](https://open-ev-charts.org/) provides a collection of electric car (BEV) registration numbers among different countries, which tracks the adoption of electric cars over time, countries and brands.
# 
# ## 1.1 Read the data (10 points)
# 
# ### 1.1.1 A first try (4 points)
# 
# &#9989;&nbsp; **Task** Read in the sales data from `EV_Sale.csv` into a DataFrame and print the `.head()` of the data. Then, use `describe` to get a feel of this dataset.

# In[51]:


## your code here


# ### 1.1.2 Missing data (4 points)
# 
# Look at the data file itself and the result you got in Question 1.1.1.
# 
# &#9989;&nbsp; **Task** How many columns in the data file and how many columns in the (head and describe) results did you get in 1.1.1?

# <font size=8 color="#009600">&#9998;</font> Put your answer here

# &#9989;&nbsp; **Task** Check the data types of data you loaded in 1.1.1 (for example, the total registration number of Electric Vehicles in Germany in January 2017). Looking at the original data file, what do you want the data types to be? Do they match your current types?  __2 points__

# <font size=8 color="#009600">&#9998;</font> Put your answer here

# ### 1.1.3 Load data again (2 points)
# 
# Load the data correctly.
# 
# &#9989;&nbsp; **Task** Check the usage of `read_csv` function, and focus on the parameter `thousands`. Use that parameter to load the data file correctly.
# 
# **Hint:** You will have proper number of columns when you `describe` the correctly loaded data.

# In[55]:


## your code here


# ## 1.2 Clean the data (10 points)
# 
# ### 1.2.1 Remove and track excess data (2 points)
# 
# We will only focus on the European motor companies, so we need to remove the excess features that from non-European countries.
# 
# &#9989;&nbsp; **Task** Drop the columns that are **NOT** the following:
# * Renault
# * BMW
# * Audi
# * Opel
# * Mercedes-Benz
# * Volkswagen
# 
# Make sure to make a list of the columns that you dropped. This is important if you need to report what you didn't consider in the model. Print the `.head()` of the DataFrame after dropping the unneeded columns. 

# In[57]:


## your code here


# ### 1.2.2 Focus on part of the data (3 points)
# 
# Now we just focus on the data on the most recent years, say 2020, 2021 and 2022.
# 
# &#9989;&nbsp; **Task** Use a mask to filter your data to focus only on the data from the year 2020 to 2022. Print the `.head()` of that DataFrame. 

# In[59]:


## your code here


# ### 1.2.3 Missing data (3 points)
# 
# Not all the countries have reported values for all items. You should check if any countries have missing data. We could include these missing data in a variety of ways, but instead, to make our work a little simpler, we will simply drop that index / row if it has any missing data.  
# 
# &#9989;&nbsp; **Task** Drop any index / row from the data that is missing data.  

# In[61]:


## your code here


# ### 1.2.4 Separate data (2 points)
# 
# Separate the current data frame into three separate dataframes according to the countries (Germany, France, and Norway).
# 
# &#9989;&nbsp; **Task** Separate the current data frame into three, representing the registration numbers in Germany, France, and Norway.

# In[63]:


## your code here


# ## 1.3 Describe the data (4 points)
# 
# Now that you have a cleaned data set, let's look into the data by making histograms of it.
# 
# &#9989;&nbsp; **Task** For one of separated data from Question 1.2.4, make histograms describing the distributions of all the registration numbers. Please describe one histogram in plain English. 
# 

# In[65]:


## your code here


# <font size=8 color="#009600">&#9998;</font> Put your description here

# ## Part 2: Data analysis (25 total points)

# ### 2.1 Sales Performance of Renault (12 points)
# 
# Renault is a French automobile manufacturer that was among the sales leader of electric cars in Europe. 
# As an employee of Renault, you are responsible to monitor the sales performance of your company in France. 
# To do so, you will investigate the performance of Renault over the __past four years__.
# 
# &#9989;&nbsp; **Task**
# 
# Return to the dataframe you loaded in Part 1.1.3. Make sure you have unique variable names! You will first extract the data of France for __2018-2022__ and keep all the brands, __including non-European__.

# In[67]:


## your code here


# &#9989;&nbsp; **Task** As a first attempt, create a `scatter` plot of the number of cars sold by Renault in France versus the number of months. Make sure to include appropriate axis labels! 

# In[69]:


## your code here


# &#9989;&nbsp; **Task** Your boss wants to know if you can monitor Renault sales performace with this plot. Describe why you don't (or do) think it is a useful plot to monitor sales performance.

# <font size=6 color="#009600">&#9998;</font> Write your answer here

# &#9989;&nbsp; **Task**  As a second attempt at visualizing information about sales performance, compute the percent of Renault sales in France for each month. Then create a `scatter` plot of the percent of Renault sales versus the number of months. Make sure to incldue appropriate axis labels!

# In[71]:


# put your code here


# &#9989;&nbsp; **Task** You have decided that this is a better way to viualize sales performance, but you need to convince your boss. Provide reasoning for how this provides more information about Renault sales performance. How would you describe the sales performance of Renault based on this plot? __3 points__

# <font size=6 color="#009600">&#9998;</font> Write your answer here

# ### 2.2 Identifying the Main Competitor (13 points)

# Now you have been asked to identify the main competitor of Renault in France (if one exists) to develop a marketing strategy and hopefully increase the percent of sales in 2023.
# 
# To do so, you will investigate the percent of sales of all the other brands.
# 
# &#9989;&nbsp; **Task** Make multiple `scatter` plots in a single figure (using `plt.subplot()`) that display the percent sales versus the number of months for each brand. Adjust the size of the figure so you can clearly see the plots.Make sure to include appropriate axis labels! 
# 
# __Hint__: you should use the matplotlib function `ylim` that sets the $y$-axis range to have a better understanding of the situation. As an example, `plt.ylim([0 0.5])` displays that data with a $y$ value between 0 and 0.5. 

# In[73]:


# put your code here


# &#9989;&nbsp; **Task** As an additional tool to identify your main competitor, you want to know if there is a correlation between the percent sales of Renault and the other brands.
# 
# Make multiple `scatter` plots in a single figure (using `plt.subplot()`) that displays the percent of Renault sales versus the percent of all the other brands sales. Adjust the size of the figure so you can clearly see the plots. Include appropropriate axis labels and adjust your axes limits with `ylim`.

# In[75]:


# put your answer here


# &#9989;&nbsp; **Task** Using the plots you have made, who is Renault's main competitor in France? Use words and plots to justify your answer!

# <font size=6 color="#009600">&#9998;</font> Write your answer here

# ---
# 
# ### Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "Homework Assignments" section, find the submission folder link for Homework #3, and upload it there.

# &#169; Copyright Michigan State University Board of Trustees
