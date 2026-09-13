#!/usr/bin/env python
# coding: utf-8

# # Day 10 Pre-class Assignment: Computational Models Overview and The Pandas Data Analysis Library
# 
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png" width=400px>

# ### <p style="text-align: right;"> &#9989; Put your name here</p>

# ## Goals for today's pre-class assignment
# 
# * Review some types of Computational Models
# * Use the Pandas module to explore and visualize data
# 
# 
# ## Assignment instructions
# 
# **This assignment is due by 11:59 p.m. the day before class,** and should be uploaded into the appropriate "Pre-class assignments" submission folder.  If you run into issues with your code, make sure to use Slack to help each other out and receive some assistance from the instructors. Submission instructions can be found at the end of the notebook.
# 
# **It is important that you do your best to complete the pre-class assignment!** Going through this assignment and trying to complete it to the best of your ability will help to make sure you're prepared for the content that is covered in class. 

# ---
# # Part 1: Overview of Computational Models
# 
# So far this semester, we looked and and even _built_ a few examples of computational models. Take a moment to think about what we mean when we talk about "models" by watching the following overview video to get an introduction to the definition of **Computational Models**. If the YouTube video doesn't work, try this [MediaSpace link](https://mediaspace.msu.edu/media/Introduction+to+Computational+Models/1_yh81zqwi).
# 
# **Note:** This video references a model for the motion of a snowball that was replaced by the Savings Account In Class assignment for Fall 2021. If you want to learn more about the model, ask your instructor!

# In[1]:


# Video on the Pandas module  
from IPython.display import YouTubeVideo  
YouTubeVideo("7qAunwHsuj8",width=640,height=360)


# &#9989;&nbsp; **Question 1:**  In your own words, decribe what scientific and/or computational models do.

# <font size="+3">&#9998;</font> *Put your answer here*

# &#9989;&nbsp; **Question 2:** What are some of the limitations of scientific and/or computational models?

# <font size="+3">&#9998;</font> *Put your answer here*

# ---
# # Part 2: Working with data in Pandas
# 
# *Pandas* is an extremely useful Python library for reading and analyzing datasets in a variety of formats with a variety of data types. Managing complicated files with only the Python tools we've learned up to this point is often very difficult and at times, may seem impossible. Lucky for you, someone else decided to make your life easier and created Pandas!
# 
# **Watch the following videos** to learn a bit about how you can load and analyze data using this handy library! Pay particular attention to the part of the video that talks about "slicing" the data. If the YouTube video doesn't work, try this [MediaSpace link](https://mediaspace.msu.edu/media/The+Pandas+module/1_yvaobs9w).
# 
# **Note**: In a previous semester of this course, the order of the topics covered was slightly different so there may be references to "future" content that you already have experience with. Also, the version of Python used in this video is a bit older than the version that you have, so the format of the Pandas dataframe might look a bit different in your notebook when you display it in your notebook.
# 
# ---
# 
# ### Video 1

# In[2]:


# Video on the Pandas module  
from IPython.display import YouTubeVideo  
YouTubeVideo("A0InxIMAvlU",width=640,height=360,end=405)


# ### Video 2
# 
# This next video introduces plotting dataframes using the Pandas module. Pandas does have its own plotting functions which you may see referenced from time to time. You are welcome to explore them and use them, but in CMSE 201, we will focus on using Pandas (or numpy) for loading and analyzing data and Matplotlib for visualizing the data!
# 
# **Note**: this video will reference the "blood pressure" dataset, which you will be working with in the code cells below.
# 
# **Access the video using this [MediaSpace Link!](https://mediaspace.msu.edu/media/Plotting+Pandas+Data/1_f4gzgb3v)**
# 
# 

# ### Useful Pandas references
# 
# For this pre-class assignment and the assignments that follow during the next week of the course, these two references might prove to be particularly useful:
# 
# * The [Pandas website](http://pandas.pydata.org/)
# * [10-minute Pandas Tutorial](http://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
# 

# ---
# ## 2.1: Pandas and Plotting 
# 
# Now that we understand a bit of the fundamentals for Pandas dataframes, we're going to use a small database of data taken from patients that were admitted to the hospital with chest pains.  In the dataset, there are several columns. Here are what a few of them correspond to:
# 
# * **age** is patient age
# * **chol** is serum cholesterol in units of mg/dl
# * **trestbps** is the resting blood pressure of the patient upon admission
# * **thalach** is the maximum heart rate achieved
# 
# The cell immediately below this uses Pandas to read in the data, and you should **run that cell before you do anything else and make sure you understand what it's doing!**
# 

# ### Importing Pandas and all of our other useful modules we know up to this point.
# 
# As always, we should make sure we import all of the Python modules we might want to use as we work through the notebook.
# 
# Then, download `heart_disease_data.csv` from the course website. Make sure the file is in the same folder as your notebook! If you are having trouble with the data file, make sure to ask for help!
# 
# **Pay special attention to the new import command for Pandas, it's a bit different than what is shown in the video!**
# 
# Make sure you execute this cell!

# In[4]:


# import numpy
import numpy as np

# import matplotlib and make sure plots show up in the notebook
import matplotlib.pyplot as plt

# Look at the Pandas import -- we take a similar approach to how we import numpy
# "pd" will be the short-hand for accessing Pandas functions.
import pandas as pd

# read in some data on heart disease
# from http://www.datasets.co/dataset/Heart-Disease
heart_disease_data = pd.read_csv('heart_disease_data.csv')


# ## 2.1.1: Checking out the DataFrame
# 
# Now let's see what the data looks like by examining all of the columns labels and the first few rows of data using the `.head()` command that was explained in the video.

# In[5]:


# Check out the top of the data structure
heart_disease_data.head()


# Let's also test out the `.describe()` function to get some details about the data.

# In[6]:


# Check out some of the properties of the data
heart_disease_data.describe()


# ## 2.1.2: Intro to Accessing data in Pandas Dataframes
# 
# To access data in a DataFrame for plotting, there are several different ways. Review the code below to see how you access data by its column header. 
# *Note: In Part 3, we will explore additional ways to access data with more control!*

# In[7]:


heart_disease_data['trestbps'] # accesses the column labeled 'trestbps'


# To access the data by column name, you need to know the labels for each column name. If you need to know what strings pandas is using for column headers, you can find out using the `.keys()` command. Run the cell below to get the column header names for `heart_disease_data`.
# 
# **Note:** Using `.keys()` is particularly useful when there are extra spaces or other attributes of the column names that you can't see with the standard dataframe display. Remember this if you decide to use data for your semester project!

# In[8]:


heart_disease_data.keys()


# &#9989;&nbsp; In the cell below, print another one of the columns of `heart_disease_data`

# In[9]:


# put your answer here


# ---
# ## 2.2 Visualizing the data
# 
# The following questions give you a chance to try visualizing the pandas dataframe using some of the functions you were shown in the video and one you weren't.
# 
# 
# ### Note:
# In this section, you will be plotting using `matplotlib.pyplot` as shown in **Video 2**.

# &#9989;&nbsp; **Question 1:**  Using `matplotlib.pyplot`, make a histogram (using `plt.hist()`) of the resting blood pressure of the patient upon admission. Make sure to include axis labels and a title indicating what you're looking at.  

# In[11]:


# Put your code here


# &#9989;&nbsp; **Question 2:**  Make a `scatter` plot of the resting blood pressure ('trestbps') versus age. Make sure you put the right variables on the $x$ and $y$ axes.
# 
# Think back to (or refer to) the Great Lakes in-class assignment we did previously in the course and remind yourself about correlations. Do you think these values are correlated?

# In[13]:


# Put your code here


# &#9989;&nbsp; **Question 3:**  Make a [boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.htmll) for the resting blood pressure. The code structure of `boxplot` is slightly different than the previous two plots. 

# In[15]:


# Put your code here


# ---
# # Part 3: Accessing Parts of Dataframes
# 
# What if we want to access dataframes by something other than the column headers? 
# 
# The code below creates a dataframe from scratch. Review the code and, when necessary, use the internet to learn what the following Pandas methods/attributes are used for (e.g. `.index` and `.columns`) and **comment on what each line of code is doing below.**

# In[17]:


Example_DataFrame = pd.DataFrame([['A',0,1,2,3],['B',4,5,6,7],['C',8,9,10,11],['D',12,13,14,15]]) # put comment here

Example_DataFrame.index = Example_DataFrame[0] # put comment here

Example_DataFrame = Example_DataFrame.iloc[:,1:] # put comment here 

Example_DataFrame.index.name = None # This line is removing the column header for the index column

Example_DataFrame.columns = ['Col_1', 'Col_2', 'Col_3','Col_4'] # put comment here 

Example_DataFrame


# Now that we've created this Pandas dataframe, the following image should serve as a reference for how one can access information within it.
# 
# <img src="https://i.ibb.co/M1H3MsS/DFExamp.png" alt="Dataframe Example" border="0" width=500px>

# ## 3.1: Examples of using .iloc and .loc to access data
# 
#  Have you figured out the difference yet? 
#  * If you want to access data by its label or name, we use `.loc`
#  * If you want to access data by its indices or position, we use `.iloc`
# 
# Now, here are some examples that require us to index Pandas dataframes: 
# 
# &#9989;&nbsp; __Example 1__: Access information in the second column of Example_Dataframe. 
#    -  __Information Needed__: 
#    Look at the above image and in your mind 'highlight' the information we want to access. We want the values under `Col_2`.
#    - __Available Tools__:  
#         * We notice that since we want all the information in the column, we can access it by the column name. 
#         * However, we can also simply retreive the values in that column using `.iloc`. We want all the rows in the column at the 1 index. 

# In[18]:


#Index Col_2 by name
print(Example_DataFrame['Col_2'])

#Index Col_2 by .iloc, pay special attention to the use of ":" -- what's going on there?
print(Example_DataFrame.iloc[:,1])


# __Check your code__: Look at the gif below. Is this the image you pictured earlier? We can check that the code we used was correct by comparing the output with the column highlighted in the original dataframe. 

# <img src=https://media.giphy.com/media/Z8vwrf8OuKhSKuPk6r/giphy.gif width="600" height="300" align="center">

# &#9989;&nbsp; **Example 2:** We access the information in the second row in a similar manner. 

# In[ ]:


#Index Row B with loc
print(Example_DataFrame.loc['B'])

#Index Row B with .iloc
print(Example_DataFrame.iloc[1])
#Or
#Index Row B with .iloc
print(Example_DataFrame.iloc[1,:])


# <img src=https://media.giphy.com/media/8pxXDtD429GhQpto4B/giphy.gif width="600" height="300" align="center">

# Now, we have a slightly more complicated task. We are going to access single entries or multiple entries in a single column.  
# 
# &#9989;&nbsp; **Example 3**: Access the top left element of the Example_Dataframe.
#    -  __Information Needed__: Look at Example_Dataframe and in your mind 'highlight' the information we want to access.  We want the value 0. 
#    - __Available Tools__:  
#         * Since we want a single value, we can combine the column and row access we used before, by using both the column name and `.loc` with the row name. 
#         * Or we could use the indices to retreive the value using `.iloc`. We want the entry in the 0th row and 0th column.  

# In[ ]:


#Index Value 0 with .loc
print(Example_DataFrame['Col_1'].loc['A'])

#Index Value 0 with .iloc
print(Example_DataFrame.iloc[0,0])


# We can also access multiples entries. In the final example, we want to access the entries 1,2,3 or the entries in the 0th row and the 1st, 2nd, 3rd columns.

# In[ ]:


Example_DataFrame
Example_DataFrame.iloc[0,1:]


# __Check your code__: Look at the gif below. We can check that the code we used was correct, by comparing the output with the column highlighted in the original dataframe. 

# <img src=https://media.giphy.com/media/O9WnZetfXl4K9vCLSL/giphy.gif width="600" height="300" align="center">

# ## 3.2: Let's practice different ways to index using both `.iloc` and `.loc` 
# 
# Examine the Example_Dataframe and complete the questions below. For each question, follow the same process we did above: What is the task? What information do you need? What tools can you use? Make sure to check that the output matches what you expected from the original Dataframe. For the __Available Tools__ portion in Tasks 1 and 3, make sure to describe the differences between the two methods. 

# &#9989;&nbsp; **Question 1:** Using `.loc` and `.iloc`, access the row of data containing [8,9,10,11] from the example dataframe. 
#    -  __Information Needed__:??
#    - __Available Tools__:  
#         * ??
#         * ??
# 

# In[ ]:


# 1


# &#9989;&nbsp; __Question 2__: Using `.iloc`, access just the values [6,10,14] from the example dataframe.
#    -  __Information Needed__:??
#    - __Available Tools__:  
#         * ??

# In[ ]:


#2


# &#9989;&nbsp; __Question 3__: Using `.loc` and `.iloc`, access the value "10" from the example dataframe.
# 
#    -  __Information Needed__:??
#    - __Available Tools__:  
#         * ??
#         * ??

# In[ ]:


#3


# &#9989;&nbsp; __Question 4__: Print out the column names and index names.

# In[ ]:


#4


# ## 3.3: Understanding the Pandas Dataframes default
# 
# By default, when you load a dataset with Pandas or create a dataframe from scratch, Pandas will define the row indices to just be numbers rather than a unique set of labels that match your data. This is how we will commonly interact with Pandas dataframes.
# 
# &#9989;&nbsp; Review the following code that constructs a dataframe without providing specific row index names and **comment what each line of code is doing.** Indexing will be similiar to before but now the row names are just integers representing row numbers.

# In[ ]:


DF_NoIndex = pd.DataFrame([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]) #Comment here
DF_NoIndex.columns = ['Col_1', 'Col_2', 'Col_3','Col_4'] # Comment here

DF_NoIndex


# In[ ]:


#Index the third row by .loc
print(DF_NoIndex.loc[2])

#Index the third row by .iloc
print(DF_NoIndex.iloc[2])


# In[ ]:


#Index the first and second row by loc
print(DF_NoIndex.loc[0:1])

#Index the first and second row by .iloc
print(DF_NoIndex.iloc[0:2,:])


# ---
# ## Assignment wrap-up
# 
# Please fill out the form that appears when you run the code below.  **You must completely fill this out in order to receive credit for the assignment!**

# In[ ]:


from IPython.display import HTML
HTML(
"""
<iframe 
	src="https://cmse.msu.edu/cmse201-pc-survey" 
	width="800px" 
	height="600px" 
	frameborder="0" 
	marginheight="0" 
	marginwidth="0">
	Loading...
</iframe>
"""
)


# ### Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "Pre-class assignments" folder, find the appropriate submission link, and upload it there.
# 
# See you in class!

# &#169; Copyright 2023,  The Department of Computational Mathematics, Science and Engineering at Michigan State University
