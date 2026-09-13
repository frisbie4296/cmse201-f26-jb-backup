#!/usr/bin/env python
# coding: utf-8

# # Homework 2: Functions, arrays, and data analysis

# ### <p style="text-align: right;"> &#9989; **Put your name here** </p>

# <img src="https://cmse.msu.edu/sites/_cmse/assets/Image/image002.jpg"
#      alt="CMSE Logo"
#      align="right" 
#      width="100" />
# 
# 
# ## Learning Goals
# 
# ### Content Goals
# - Practice how to define and use functions in Python (including using the `return` statement and default arguments)
# - Use functions, conditional logic, and packages to do calculations with lists / arrays of numbers
# - Practice using NumPy and Matplotlib and use them to read, analyze, visualize, and interpret data
# 
# ### Practice Goals
# - Use the internet as a resource for learning how to write code, learn new things, and troubleshoot problems
# ___
# 

# ## Assignment instructions
# 
# Work through the following assignment, making sure to follow all the directions and answer all the questions.
# 
# **This assignment is due at 11:59 pm on Friday, October 13.** It should be uploaded into the "Homework Assignments" submission folder for Homework #2.  Submission instructions can be found at the end of the notebook.
# 

# ---
# ## Version check
# 
# Before you begin, make sure your Jupyter kernel is Python 3. There are significant differences between Python 2 and Python 3, and we use Python 3 in this course. The kernel type at the upper-right corner should say "Python 3", and the following code should show a version of the form: `3.x.y` (where "x" and "y" are the sub-version numbers).
# 
# If your kernel is Python 2, try selecting Python 3 from the Kernel menu above under the sub-menu "Change kernel". If that does not work, consult the Teams help channel for assistance.

# In[1]:


import sys
print(sys.version)


# ---
# ## 1. Writing functions in Python (20 points)
# 
# Remember, functions are a great programming concept because they are:
# 
# 1. Modular
# 2. Re-usable
# 3. Useful
# 
# While functions can help us to build progressively more sophisticated code, we need to make sure we understand the basic structure of a function to properly write them.

# #### &#9989;&nbsp; Question 1.1 (4 points): Writing a function to sum elements in a list

# Write a function to return the sum of a list of integers.
# 
# Examples:
# - The sum of `[1, 2, 3]` is `1 + 2 + 3 = 6`.
# - The sum of `[-1, 0, 1]` is `-1 + 0 + 1 = 0`.
# 
# Note: Write the function "from scratch" - don't use any built-in Python functions.

# In[2]:


# Your code here.


# #### &#9989;&nbsp; Question 1.2 (2 points): Testing a function is correct

# Python has a built-in function called `sum` which can be used to calculate the value of a list. Compare your function to Python's `sum` on at least one list and show they give the same answer.

# In[4]:


# Your code here.


# #### &#9989;&nbsp; Question 1.3 (2 points): Thinking about edge cases

# What happens if you try to compute the sum of a list of integers with an empty list? This is an example of an *edge case* in programming - it refers to the situation in which the general rule may not apply. This happens quite often in many contexts and is important to keep in mind when writing functions.
# 
# In the cell below, explore what happens when you pass an empty list into your function and what happens when you pass an empty list into Python's `sum` function. After that, reflect on the behavior - are they the same? different? is one more appropriate for certain situations? are there any other options for the behavior of the function on an empty list?
# 
# 

# In[6]:


# Your code here.


# <font size=6 color="#009600">&#9998;</font> *Respond to the questions here.*

# #### &#9989;&nbsp; Question 1.4 (4 points): Counting certain elements in a list

# Write a function to return the number of elements in a list that are greater than or equal some `threshold` value. The function should take the list of numbers and the `threshold` value as input parameters, and set the default value of `threshold` to `0.0`. Include at least one check to show your function is correct.
# 
# Examples: 
# - The number of elements in `[-1.0, 2.1, 5.0]` greater than or equal to `threshold=0.0` is `2`.
# - The number of elements in `[-1.0, 2.1, 5.0]` greater than or equal to `threshold=3.2` is `1`.

# In[8]:


# Your code here.


# #### &#9989;&nbsp; Question 1.5 (6 points): Is this a probability distribution?

# A *probability distribution* is a list of non-negative numbers that sums to one. For example, we can describe a fair coin by the probability distribution `[0.5, 0.5]` corresponding to the probability of heads and tails.
# 
# Write a function that inputs a list of numbers and returns `True` if the list of numbers is a probability distribution, else returns `False`. This function should use at least one of the functions you've written above.
# 
# Examples:
# - `[0, 1/3, 1/3, 1/3]` is a probability distribution.
# - `[-1, 1, 1]` is not a probability distribution because it has a negative number.
# - `[1/2, 1/2, 1/2]` is not a probability distribution because its values don't sum to one.
# 
# Note: Checking if the sum of values is exactly `1` can be unsafe using `==` with floating point numbers.  Instead you should use the function `np.isclose` from the `numpy` library to do this. Reminder: You can get help for a function using the `help` command, or look at documentation online.

# In[10]:


# Your code here.


# In[12]:


assert is_probabiliy_distribution([0, 1 / 3, 1 / 3, 1 / 3])
assert not is_probabiliy_distribution([-1, 1, 1])
assert not is_probabiliy_distribution([1 / 2, 1 / 2, 1 / 2])


# #### &#9989;&nbsp; Question 1.6 (2 points): Code discovery

# Being able to write functions is a must-have skill, but it's also important to be able to search for functions online or in documentation so you don't always have to write everything from scratch.
# 
# Find a function in Python that's either built-in (like `sum`) or in a package (like `np.isclose`) which we have *not* discussed previously, describe what it does below, and show and example of using it.

# <font size=6 color="#009600">&#9998;</font> *Respond to the questions here.*

# In[13]:


# Your code here.


# ---
# ## 2. Computing with arrays (20 points)

# NumPy arrays are very useful ways to store and work with data because they do operations in parallel. In this question you'll practice writing functions to do operations on lists in parallel, then practice using NumPy to do the same task. Finally, you'll use NumPy to read in and analyze data.

# #### &#9989;&nbsp; Question 2.1 (5 points): Are these lists equal?

# Two lists are equal if:
# - They have the same length.
# - Every element is equal.
# 
# Write a function which inputs two lists of numbers and returns `True` if they are equal, else returns `False`. Check your function on at least two example inputs to show its working correctly.

# In[15]:


# Your code here.


# #### &#9989;&nbsp; Question 2.2 (5 points): The sum of two lists

# Given two lists with the same length, we define their sum element-wise. For example, `[1, 2, 3] + [1, 0, 1] = [1 + 1, 2 + 0, 3 + 1] = [2, 2, 4]`.
# 
# Write a function that inputs two lists of numbers and returns the sum of the two lists. You can assume the lists have the same length. Test your function on at least two example inputs to show its working correctly.

# In[17]:


# Your code here.


# #### &#9989;&nbsp; Question 2.3 (3 points): Comparing to NumPy array sum

# NumPy arrays are very convenient because they do operations in parallel. In the cell below, create two NumPy arrays and add them together. Compare this result to your function which computes the element-wise sum of two lists and show they give the same answer.

# In[19]:


# Your code here.


# #### &#9989;&nbsp; Question 2.4 (7 points): Working with NumPy arrays

# There's a file called `random_lists.txt` on the course website along with this homework. This data is two-dimensional: each column of the data is a list, and there are multiple columns. Load this file into a NumPy array and determine the indices of the columns that are probability distributions.

# In[21]:


# Your code here.


# ---
# ## 3. Analyzing and Visualizing Endangered Species Data (30 points) 

# You are a zoologist exploring data from the International Union for Conservation of Nature's (IUCN) Red List, a tool that leverages research and data to provide a comprehensive assessment of an organism's extinction risk. Put simply, the Red List provides a status on nearly all species on Earth as to whether it is doing ok, Vulnerable to extinction, Endangered, or even Extinct ([Source](https://data.world/project-data-viz/iucn-redlist-changes-2002-to-2022-pdv-10-2022/workspace/project-summary?agentid=project-data-viz&datasetid=iucn-redlist-changes-2002-to-2022-pdv-10-2022)). 
# 
# The structure of the data is as follows:
# * Column 0: Year (ranging from 2002-2022)
# * Column 1: Mammal Species Assessed
# * Column 2: Bird Species Assessed
# * Column 3: Reptile Species Assessed
# * Column 4: Amphibian Species Assessed
# * Column 5: Fish Species Assessed
# * Column 6: Insect Species Assessed
# * Column 7: Mollusc Species Assessed
# * Column 8: Other Invertebrate Species Assessed
# * Column 9: Plant Species Assessed
# * Column 10: Fungus & Protist Species Assessed
# * Column 11: Mammal Species Critically Endangered
# * Column 12: Bird Species Critically Endangered
# * Column 13: Reptile Species Critically Endangered
# * Column 14: Amphibian Species Critically Endangered
# * Column 15: Fish Species Critically Endangered
# * Column 16: Insect Species Critically Endangered
# * Column 17: Mollusc Species Critically Endangered
# * Column 18: Other Invertebrate Species Critically Endangered
# * Column 19: Plant Species Critically Endangered
# * Column 20: Fungus & Protist Species Critically Endangered
# * Column 21: Mammal Species  Endangered
# * Column 22: Bird Species Endangered
# * Column 23: Reptile Species Endangered
# * Column 24: Amphibian Species Endangered
# * Column 25: Fish Species Endangered
# * Column 26: Insect Species  Endangered
# * Column 27: Mollusc Species Endangered
# * Column 28: Other Invertebrate Species Endangered
# * Column 29: Plant Species Endangered
# * Column 30: Fungus & Protist Species  Endangered
# * Column 31: Mammal Species Vulnerable
# * Column 32: Bird Species Vulnerable
# * Column 33: Reptile Species Vulnerable
# * Column 34: Amphibian Species Vulnerable
# * Column 35: Fish Species Vulnerable
# * Column 36: Insect Species Vulnerable
# * Column 37: Mollusc Species Vulnerable
# * Column 38: Other Invertebrate Species Vulnerable
# * Column 39: Plant Species Vulnerable
# * Column 40: Fungus & Protist Species Vulnerable

# #### &#9989;&nbsp; Question 3.1 (5 points): Data Context
# 
# Before you examine the data itself, you need to determine the context of the data set. Visit the [IUCN Red List Website](https://www.iucnredlist.org/), and spend at least 15 minutes exploring the website to determine some context for the data set. Some ideas for what to look for are:
# 
# * How IUCN defines the different categories (e.g. "Criticically Endangered" vs. "Endangered").
# * Who collects the data?
# * How is IUCN funded?
# * How often is the data reviewed? Who reviews it?
# 
# For more information or reading on the importance of data context, check out [The Numbers Don't Speak for Themselves](https://data-feminism.mitpress.mit.edu/pub/czq9dfs5/release/3).

# <font size=+3>&#9998;</font> *Your answer here*

# #### &#9989;&nbsp; Question 3.2 (5 points): Reading in the data
# 
# In the cell below, read in the data file `endangered_species_HW2.csv` **with `np.loadtxt()`.** (Yes, you have learned `pandas`, but we're practicing with `numpy` here!) 
# 
# There are 41 columns of data, so you should pick one endangered category (i.e. 'Vulnerable, Endangered, or Critically Endangered) and read in **only those columns along with the Year column and Total Species Assessed columns.** That should result in 21 columns of data. Make sure you double check that you have the columns that you want! 
# 
# Each column should have its own variable name, and you can accomplish this either as you read in the file or by defining the variables after you read them in.

# In[25]:


# Put your code here!


# #### &#9989;&nbsp; Question 3.3 (5 points): Exploring the Data
# 
# When presented with a new data file, the first goal is to understand the data. In the cell(s) below, make at least **four** plots of the data using plt.subplot(). Make sure to include all of the appropriate components and make your plots readable! Then, describe one thing you notice from each plot.

# In[23]:


# Put your code here


# <font size=+3>&#9998;</font> *Your answers here*

# #### &#9989;&nbsp; Question 3.4 (7 points): Analyzing the Data
# 
# Now, it's time to do some statistics to see if we can find some meaning from this data.
# 
# First, choose a species category (e.g. "Mammals") from your existing data. Keep your previously chosen Red List category the same so you don't have to read in new data!
# 
# Then, do the following calculations:
# 
# * Calculate the percentage of your Red List category in the total species assessed category (e.g. (mammals critically endangered / total mammals assessed)  $\times$ 100 )
# * Calculate the Mean, Standard Deviation, and Median of your total species assessed category using the `numpy` functions
# * Calculate the Mean, Standard Deviation, and Median of your Red List species category using the `numpy` functions

# In[37]:


# Put your answer here


# #### &#9989;&nbsp; Question 3.5 (8 points): Visualizing the Data (8 points)
# 
# Now let's visualize our calculations! You are going to create **three plots**:
# 
# 1. Total Species Assessed over time, with mean, standard deviation (plus and minus!), and median plotted as horizontal lines.
# 2. Red List category over time, with mean, standard deviation (plus and minus!), and median plotted as horizontal lines.
# 3. Plot of percentage over time.
# 
# Note: You can use `plt.axhline()` for horizontal lines on plots!
# 
# Then, answer the following questions for **each plot**:
# 
# 1. In plain English, describe how the values are changing with time.
# 2. Is there a difference between the mean and median? If so, what might that indicate?
# 3. Where do the standard deviations lie in relation to the data and the mean and what does that tell us about the data?
# 4. Recall the context you explored early in this problem, how does the context apply here?

# In[38]:


# Put your code here


# <font size=+3>&#9998;</font> *Your answers here*

# ---
# ## Wait! Before you submit your notebook, read the following important recommendations
# 
# When your TA opens your notebook to grade the assignment, it will be really useful if your notebook is saved in a fully executed state so that they can see the output of all your code. Additionally, it may be necessary from time to time for the TA to actually run your notebook, but when they run the notebook, it is important that you are certain that all the code will actually run for them!
# 
# You should get into the following habit: **before you save and submit your final notebook for your assignments, go to the "Kernel" tab at the top of the notebook and select "Restart and Run all".** This will restart your notebook and try to run the code cell-by-cell from the top to the bottom. Once it finished, review you notebook and make sure there weren't any errors that popped up. Sometimes, when working with notebooks, we accidentally change code in one cell that break our code in another cell. If your TA stumbles across code cells that don't work, **they will likely have to give you a zero for those portions of the notebook that don't work**. Testing your notebook one last time is a good way to make sure this doesn't happen.
# 
# **Once you've tested your whole notebook again, make sure you save it one last time before you upload it to D2L.**

# ---
# 
# ### Congratulations, you're done! ###
# 
# Submit this assignment by uploading it to the course Desire2Learn web page. Go to the "Homework Assignments" section, find the submission folder link for Homework #2, and upload it there.

# Copyright &#169; 2023, [Department of Computational Mathematics, Science and Engineering](https://cmse.msu.edu/) at Michigan State University, All rights reserved.
