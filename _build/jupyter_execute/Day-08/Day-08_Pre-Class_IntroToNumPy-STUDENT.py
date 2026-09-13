#!/usr/bin/env python
# coding: utf-8

# # Day 8 Pre-Class: Introduction to NumPy
# <img src="https://www.kdnuggets.com/wp-content/uploads/numpy-logo.jpg" width=300px>

# ### <p style="text-align: right;"> &#9989; Put your name here</p>

# ### Goals for this pre-class assignment
# By the end of this assignment, you should be able to:
# * Import NumPy into Python and create an manipulate NumPy arrays.
# * Use NumPy to do simple calculations with arrays
# 
# ### Assignment instructions
# 
# Watch the videos below, do the readings linked to below the videos, and complete the assigned programming problems.  Please get started early, and come to office hours if you have any questions! Make use of Slack as well!
# 
# **This assignment is due by 11:59 p.m. the day before class,** and should be uploaded into the appropriate "Pre-class assignments" submission folder.  Submission instructions can be found at the end of the notebook.

# ___
# ### A brief aside on Jupyter notebooks
# Before you get started with this notebook, take a few minutes to make sure you are feeling comfortable with **Jupyter notebooks** at this point in the course. 
# 
# * If you still have any questions about how they work, or how to better use them, post your thoughts on our Slack channel. 
# * It is really important to keep in mind that Jupyter notebooks are based on cells. This is a markdown cell, for example. Because you can execute the cells in any order you wish, *it is up to you to keep track of what has been done, or not*. If it helps, you can make an initial habit of running all cells from the top down, although there will be cases where you won't want to do that. 
# * It is worth taking a few minutes to get better at keyboard shortcuts, which will make using the notebooks much more efficient; and, learning some markdown is also helpful. Both are in this [webpage](https://murillogroupmsu.com/introduction-to-jupyter-notebooks/), and you can also do a web search to find other tutorials on these topics. 
# * One of the best things about the notebooks is **rapid prototyping of code**. This means: try something quickly, delete it and move on. With the keyboard shortcuts, this becomes quite fast. Suppose you want to know what "4 + 5 * 3" will give. The steps are simple: create a new cell, type that expression in, shift-enter, examine the result, delete that cell, use the result. If you learn the keyboard shortcuts, this prototyping/debugging is fast:
#     * press "esc" to get out of the cell you are in (go into command mode)
#     * press "b" to create a cell below (or "a" for above - your choice)
#     * press "return" to enter/activate the cell (go into edit mode)
#     * type in your test (e.g., 4 + 5 * 3)
#     * press "shift-enter"
#     * press "esc" to get out of the interior of the cell (go from edit to command mode)
#     * press "x" to delete that temporary cell
#     
# This may seem like a lot of steps, but once you memorize the shortcuts, you can rapidly create, use and delete cells. When you have an error, this is best way to quickly isolate parts of the code to test them.
# 
# Try it now!

# ___
# ## Getting familiar with NumPy
# 
# Okay, now let's get to the subject of this pre-class assignment: **NumPy**. 
# 
# As you learned in the previous course material, Python comes with a large number of extremely useful libraries. In fact, Python itself is a rather small language on its own; it's true power is the myriad of libraries developed for it. In our realm of computational modeling, a core library is [NumPy](https://en.wikipedia.org/wiki/NumPy), which translates to "Numerical Python". NumPy allows you to do mathematical operations both more easily (from a coding perspective) and faster (in the sense of how long you need to wait for the result). 
# 
# As with other libraries, you include NumPy through an import command. Execute the next cell.

# In[3]:


import numpy as np


# Note that NumPy gets imported, but also gets renamed as "np". You don't need to use "np" if you don't want to; but,  in the Python community, everyone else does and it makes it easier for people to read each other's code if we all use the same conventions. NumPy is vast. We will be learning aspects of NumPy throughout the entire semester, and this assignment is just the beginning of that journey. 
# 
# Why do we have the dot notation in which we will make calls to libraries with `np.`? The reason is that Python is huge and some of the libraries have overlapping functionalities. For example, you may find that NumPy contains libraries that *also* exist in other modules you learn later in the semester. By using the dot notation, you can be sure you are using the library of _your_ choice, and _you_ are free to switch between them throughout your code. Sometimes you will use dots _twice_, as in `np.random.randn(500)`.
# 
# For now, we will focus on the key element of NumPy: the **array**.

# **Now**, watch the following video to learn about the basics of *NumPy arrays* and how they differ from *lists*, which have been your main tool for storing information up to this point. (If the YouTube version doesn't work, try the [MediaSpace link](https://mediaspace.msu.edu/media/An+Introduction+to+NumPy+ArraysA+NumPy+Array+Basics/1_fz4bh3ng))

# In[4]:


from IPython.display import YouTubeVideo
YouTubeVideo("g7epZeDA_lQ",width=640,height=360)


# &#9989;&nbsp; **Question**: Explain, in your own words, some of the similarities and differences between standard Python lists and the NumPy arrays.

# <font size="+3">&#9998;</font> *Put your answer here!*

# ---
# ## Manipulating NumPy arrays and performing mathematical operations
# 
# Now that you understand a bit more about the NumPy array object in Python, watch the following video to understand how we can manipulate NumPy arrays and use them to perform mathematical operations, which is precisely what NumPy arrays were built for! (If the YouTube video doesn't work, try the [MediaSpace link](https://mediaspace.msu.edu/media/An+Introduction+to+NumPy+ArraysA+Operations+and+Arrays/1_qu3lpypx))

# In[2]:


from IPython.display import YouTubeVideo
YouTubeVideo("V2C9expTF1o",width=640,height=360)


# &#9989;&nbsp; **Question**: If you had two arrays of the same length and wanted to create a new array that is the product of the first two, how would you do that?

# <font size="+3">&#9998;</font> *Put your answer here*

# &#9989;&nbsp; **Question**: What functions can I use to find the sum, minimum value, maximum value, and average value of a NumPy array? How do I call these functions? (Provide some example code in your response).

# <font size="+3">&#9998;</font> *Put your answer here*

# ___
# ## 1. Working with NumPy Arrays ##
# ___
# 
# As you've learned at this point, at the core of NumPy is a data type called an array. An array is like a Python list, but has some very different features. It is best to not confuse them, even if sometimes they might be interchangable. All other opertions in NumPy, and many other Python libraries used for computations, will assume you are using this array type.
# 
# The first thing you need to learn to do is create an array, and there are several ways of doing this depending on your goals. Let's learn two related methods now.

# ___
# ### 1.1 np.arange
# ___
# 
# The `np.arange` function is similar to the `range` function: it creates an array where the entries go from a minimum to a maximum value using an even step size.  The arguments are:
# 
# 1. The minimum value
# 2. The maximum value
# 3. The step size
# 
# so the following command:

# In[ ]:


np.arange(0,100,5)


# creates an array that goes from `0` to `100` in steps of `5`.  **Note that like the `range` command, it does not include the maximum value as an entry in the array.**

# ___
# ### 1.2 np.linspace
# ___
# 
# The `np.linspace` function is similar, in that it creates an array where the entries are *linearly spaced*.  But it has one important difference.  Its three arguments are:
# 
# 1. The minimum value
# 2. The maximum value
# 3. *The number of elements*
# 
# so the following command:

# In[ ]:


np.linspace(0.1,1,10)


# creates an array with 10 elements, linearly (or evenly) spaced, from `0.1` to `1.0`. **Note that, unlike the `range` function, this is inclusive of the endpoints.** In other words, it includes entries for both the minimum and maximum values.  **Note also that this is good for dealing with floats!** So, now, say, to create a set of $x$ values spanning $[0,2 \pi]$, you can use `np.linspace` instead of a `while` loop!

# Note that there is a lot of documentation on the web, such as [this](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html).  **These "doc pages" can also be accessed directly in Jupyter using "?":**

# In[ ]:


get_ipython().run_line_magic('pinfo', 'np.linspace')


# **Since these functions are so similar**, it is important not to get them mixed up!  Look at the example code below and answer the questions about the differences between `np.arange` and `np.linspace`:

# In[ ]:


# comparing arange to linspace
my_array_range = np.arange(0,10,1) # Make sure you understand how this line is different...
my_array_linspace = np.linspace(0,9,10) # ... than this line
print("Using arange I get:", my_array_range)
print("Using linspace I get:", my_array_linspace)


# Now, in your own words, describe what these functions do. When do you think you would chose to use one over the other? Write your answer in this markdown cell.

# <font size="+3">&#9998;</font> *Put your answer here.*

# ___
# ### 1.3 np.zeros and np.ones
# ___
# 
# Believe it or not, a common way to initialize numpy arrays is by filling them with zeros.  For this you can use the `np.zeros` function:

# In[ ]:


np.zeros(10)


# which gives us an array of 10 elements, each one equal to zero.  Similarly, we could use the `np.ones` function:

# In[ ]:


np.ones(10)


# to give us an array full of ones.

# ___
# ### 1.4 No mixed data types!
# ___
# 
# The arrays look a lot like lists. But, a key difference is that you **cannot** have mixed types inside of the array. For example, try this code:

# In[ ]:


my_list = [1, 3.1415, 'CMSE'] # this list has three different types in it: integer, float and string
conv_to_array = np.array(my_list) # this converts a list to an array
print(conv_to_array)


# What are the types of the elements in the new array? Are they the same as the original list? Are they all the same as each other?
# 
# &#9989;&nbsp; Try modifying the list with different initial variables types to see if you can figure out the rule Python uses for setting the element type in the array when the conversion step happens.

# In[ ]:


# code to examine different types of lists to see what np.array does to them


# ___
# ### 1.5 Mathematical operations
# ___
# 
# **One of the greatest parts of numpy arrays is that you can change all elements using a single line of code!** This greatly simplifies a lot of the work we've been doing with lists and loops.
# 
# 
# Let's try some mathematical operations on arrays. 
# 
# &#9989;&nbsp; Make an array that contains the numbers $0$ through $9$.  Multiply all the elements by 3, then subtract 7.

# In[ ]:


# Put your code here.`


# &#9989;&nbsp; Make an array of the first 100 positive integers and **save it as `first_100`**. Compute and print the square of the array as `print(first_100**2)`.

# In[ ]:


# Put your code here


# ___
# ### 1.6 Numpy functions
# ___
# 
# Numpy also contains its own math libraries, highly tuned to be used with NumPy arrays. As always, to access those you need to use the "dot notation". For example, run this cell:

# In[ ]:


# This code cell uses four NumPy methods:
# linspace, pi, sin and cos
x_values = np.linspace(0, 2*np.pi, 200)
sin_times_10sin = np.sin(x_values) * np.sin(10*x_values)
print( sin_times_10sin )


# &#9989;&nbsp; Describe what you see:
# 
# *I see......*

# We recently learned another library: `matplotlib`. Let's combine them. The first thing you need to do is `import` that library:

# In[ ]:


import matplotlib.pyplot as plt


# &#9989;&nbsp; Now, plot the `sin_times_10sin` array versus your original `x_values` array.  **Don't worry**, matplotlib's `plt.plot` function can accept numpy arrays as arguments! 

# In[ ]:


# plot of my function
# (be sure to include axis labels!)


# ___
# ### 1.7 Some numpy statistics operations
# ___
# 
# Finally, let's learn just a few of the easy operations in NumPy for doing statistics. The cell below shows how easy it is to compute the sum, mean, median and standard deviation of a dataset:

# In[ ]:


ages_dataset = np.array([1,1,2,3,3,5,7,8,9,10,10,11,11,13,13,15,16,17,18,18,
18,19,20,21,21,23,24,24,25,25,25,25,26,26,26,27,27,27,27,27,
29,30,30,31,33,34,34,34,35,36,36,37,37,38,38,39,40,41,41,42,
43,44,45,45,46,47,48,48,49,50,51,52,53,54,55,55,56,57,58,60,
61,63,64,65,66,68,70,71,72,74,75,77,81,83,84,87,89,90,90,91])

print("The sum of the dataset is",np.sum(ages_dataset))
print("The mean of the dataset is",np.mean(ages_dataset))
print("The median of the dataset is",np.median(ages_dataset))
print("The standard deviation of the dataset is",np.std(ages_dataset))


# One useful way to visualize a dataset is with a **histogram**. A histogram is constructed by "binning" data. For example, the data above could be binned into a number of age intervals (0-5, 5-10, 10-15, etc.). The x-axis of a histogram are the bins chosen for the data set, and the y-axis is the number of observations that fall into each bin. In Python, we can use the `plt.hist()` function from matplotlib to make one-dimensional histograms:

# In[ ]:


# a histogram of the ages with the data binned into increments of 10
plt.hist(ages_dataset,bins=10) 
plt.xlabel('Age')
plt.ylabel('Frequency')


# &#9989;&nbsp;  Try changing the bin size in the example below and note what happens to the data. 
# 

# In[ ]:


# Put your commented code here:


# ---
# 
# ## 2. Reading in Data: Population of Michigan
# 
# We'll be using Numpy to read in data from files in class, so let's get some practice with that now. Along with this pre-class assignment, you should have also downloaded a file called `michigan_pop.csv`. 
# 
# When we read in data from a file, Python needs to know where that file is. **Therefore, it is crucial that `michigan_pop.csv` is in the same folder as this pre-class notebook.** For example, if this notebook file is in your downloads folder, make sure that `michigan_pop.csv` is also in your downloads folder.
# 
# ### 2.1 Examining the Data
# 
# * Take a moment to look at the contents of this file (`michigan_pop.csv`) with an editor on your computer.  For example, `*.csv` files open with Excel or a simple text editor like NotePad or TextEdit. You can also open it inside the Jupyter interface.
# 
# &#9989;&nbsp; **Question**: Describe the contents of `michigan_pop.csv`. What does the data look like? (E.g., how many columns of data are there, what do the different columns of data represent, what kind of values/datatypes are in each column, etc.)

# <font size="+3">&#9998;</font> *Put your response here*

# ### 2.2 Loading the Data
# 
# We are going to use NumPy to read in data from files and look at the data. The standard method for doing this in NumPy is `loadtxt`. In principle, `loadtxt` is simple - it loads your data into NumPy arrays for you to use them. Unfortunately, data seldom comes in an entirely clean form, and you will need to give many options that are file dependent. 

# In[ ]:


import numpy as np

alldata = np.loadtxt("michigan_pop.csv", usecols = (0,1), skiprows = 1, delimiter=',') # example for the michigan population file

print(alldata)


# The first argument in `np.loadtxt` (`michigan_pop.csv`) specifies the name of the file we're loading. What do the other arguments specify? What happens if you change them?
# 
# &#9989;&nbsp; **Task** In the cell below, try out the following:
# - Change `usecols` to be equal to `(0)` and print the results. Then change it to `(1)` and print out the results. Describe what changing this variable does to `alldata`.
# - Change `skiprows` to be equal to `3` and print the results. Then change it to `5` and print out the results. Describe what changing this variable does to `alldata`.

# In[ ]:


# Write code for experimenting here


# - *Describe what changing `usecols` does*
# 
# 
# 
# - *Describe what changing `skiprows` does*

# The data is currently in the form of a 2D Numpy array, which is less than ideal. We can deal with this by *unpacking* the data into two variables. We unpack the variables using another command line argument, like so.

# In[ ]:


#Unpacking the data into two separate variables

pop_dates, pop_numbers = np.loadtxt("michigan_pop.csv", usecols = (0,1), unpack=True, skiprows = 1, delimiter=',') # example for the mhu.csv file


# ### Plotting the Data
# 
# &#9989;&nbsp; **Task**  In the cell below, make a plot showing the data you read in from `michigan_pop.csv`. Use the dates for your x values and the total population for your y values.

# In[ ]:


# Write plotting code here


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

# &#169; Copyright 2018,  Michigan State University Board of Trustees
