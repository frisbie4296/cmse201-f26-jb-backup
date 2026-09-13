#!/usr/bin/env python
# coding: utf-8

# # Day 20 Pre-Class Assignment: Random Numbers

# ### <p style="text-align: right;"> &#9989; Put your name here</p>

# <img src="https://cdn-images-1.medium.com/max/1600/1*B7d5Fr27lsH3uHvzF720IA.png" width=300px>
# 
# ## Goals for today's pre-class assignment
# 
# * Practice using different methods for random number generation
# * Using random numbers to solve problems
# 
# The theme of this week is creating and using random numbers to do a wide range of things, such as modeling randomness that naturally needs to be in our models, or using them to solve problems that would otherwise be too difficult to solve. 

# ## Assignment instructions
# 
# **This assignment is due by 11:59pm the day before class,** and should be uploaded into the appropriate "Pre-class assignments"  submission folder.  Submission instructions can be found at the end of the notebook.

# ---
# ## Revisiting random numbers
# 
# We've already been using random numbers in a variety of ways in this course, but we will use random numbers for another modeling context.  If you need a reminder of some of the ways we can access random numbers in Python, re-watch the following video.
# 
# If the YouTube video doesn't work, try this [MediaSpace link](https://mediaspace.msu.edu/media/random+numbers/1_0ico6hit).

# In[ ]:


# You are encourage to watch the video in full-screen mode
from IPython.display import YouTubeVideo
YouTubeVideo("fF841G53fGo",width=640,height=360)  # random numbers


# Here are some of the imports we will use in this assignment. Notice that we're importing both `random` *and* `numpy`, which also has a `random` module.  There is also an example for how you can set a specific seed for the `random` module and the `np.random` module, which can be useful for testing code to ensure that you understand the results. **Note**: If you want to use a specific seed, you need to make sure the call to the `seed` function is before the command that is generating the random numbers.

# In[ ]:


import random
import matplotlib.pyplot as plt
import timeit
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

random.seed(1) # this initializes the seed - see question 6 below
np.random.seed(1)


# ### Practicing random number generation
# 
# The following questions are designed to give you a bit of practice with generating a variety of random numbers. Make sure you are able to accomplish all the tasks included below.

# &#9989;&nbsp;  **Question 1**: Write code below to generate a set of 100 random **floats** uniformly distributed between 0 and 1. Do this with either the `random.random()` function or the `np.random.random()` function. Compute the minimum, maximum and average value for this set of numbers.

# In[ ]:


# your code here


# &#9989;&nbsp;  **Question 2**: Using either the `random.randint()` function, or the `np.random.randint()` function, generate an array with 100 random **integers** equal to 1, 2 or 3. Determine how many of each there are. 

# In[ ]:


# your code here


# &#9989;&nbsp; **Question 3**: Using `np.random.uniform()`, write code below to generate 10, 100, 1000, and 10000 random floats in the interval $[-5,5]$ and make a histogram for each case. Create a markdown cell after the code and comment on what patterns you see. 

# In[ ]:


# your code here


# /your observations here/

# &#9989;&nbsp;  **Question 4**:  The following numpy array contains the heights (in feet) of 100 players in the NBA:

# In[ ]:


nba_heights = np.array([6.666666667,6.416666667,6,6.416666667,6.416666667,6.75,6.5,7,6.416666667,7,6.666666667,6.833333333,6.583333333,6.833333333,6.5,6.583333333,6.25,6.833333333,6.333333333,6.25,6.333333333,6.75,6.25,6.75,7.25,6.833333333,6.5,6.583333333,7.166666667,6.166666667,6.25,6.333333333,6.5,6.666666667,6.666666667,7,6.333333333,6.75,6.166666667,6.333333333,6.5,6.25,6.5,6.416666667,6.666666667,6.25,6.666666667,6.083333333,6.5,6.583333333,6.583333333,6.5,6.75,6.75,6.75,5.916666667,6.416666667,6,6.75,6.5,6.833333333,6.5,6.916666667,6.083333333,6.25,6.5,6.25,6.333333333,5.916666667,6.583333333,6.916666667,6.166666667,6.416666667,6.75,6.75,6.833333333,6.5,6.5,6.666666667,6.083333333,6.333333333,6.416666667,6,6.833333333,6.75,6.25,6.666666667,6.166666667,6.916666667,6.416666667,6.416666667,6.5,6.75,6.916666667,6.333333333,6.416666667,6.75,6.083333333,6.166666667,6.333333333])
plt.hist(nba_heights,bins=20)
plt.xlabel("Height (ft)")
plt.ylabel("Count")


# Compute the mean and standard deviation of this array and use the `np.random.normal()` function using the mean and standard deviation you just computed to generate a new array with 100, 1000, and 10000 samples. Plot the results to see if it converges to a "bell curve" as you increase the number of samples.

# ### Using random numbers to calculate $\pi$
# 
# A very neat demonstration of the power of random numbers to solve problems is to use them to calculate $\pi$.  This technique is called [Monte Carlo integration](https://en.wikipedia.org/wiki/Monte_Carlo_integration) and is broadly useful to compute integrals that are too hard to solve otherwise.
# 
# Here we will use this technique to solve for the lovable constant $\pi = 3.14159265358979...$.
# 
# First let's use the `np.random.random()` function to generate 1000 pairs of random numbers.

# In[ ]:


random_pairs = np.random.random((2,1000))
random_x = random_pairs[0]
random_y = random_pairs[1]
plt.figure(figsize=(5,5))
plt.plot(random_x,random_y,'ro')
plt.xlabel("x")
plt.ylabel("y")


# Now let's imagine a circle centered at (0,0) with diameter 1.  We can plot one quarter of it in the square like this:

# In[ ]:


plt.figure(figsize=(5,5))
plt.plot(random_pairs[0],random_pairs[1],'ro')
plt.xlabel("x")
plt.ylabel("y")

# make some linearly spaced x values
x = np.linspace(0,1,100)
# compute a set of y values for the quarter circle
y = np.sqrt(1-x**2)
# plot them
plt.plot(x,y)


# The next step is to figure out how many of these points are inside the quarter circle.  We can do this by computing their distance to (0,0).  
# 
# &#9989;&nbsp;  For each point, calculate $r = \sqrt{x^2 + y^2}$ and count how many points are inside the circle (i.e. $r < 1$):

# In[ ]:


# your code here


# Now the area of the whole square is 1.0.  We know the area of a circle is $\pi * r^2$, or just $\pi$ because our circle has a radius of 1.0.  That means if we take the area of the quarter circle and multiply it by 4 we should get $\pi$. 
# 
# &#9989;&nbsp;  **Use the fraction of points inside the circle as your estimate for the area, multiply it by 4 and see if you have a good estimate for $\pi$!**

# In[ ]:


# your code here


# **Were you close?**
# 
# &#9989;&nbsp;  **Try increasing the number of random points above (leave out the plotting step) and see if your estimate gets closer**
# 

# In[ ]:


# your code here


# ---
# ## Assignment wrapup
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
