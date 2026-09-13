#!/usr/bin/env python
# coding: utf-8

# # Day 8 Pre-Class Assignment: Python Modules: Numpy and Plots
# <img src="https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Matplotlib_logo.svg/1280px-Matplotlib_logo.svg.png" width="500px">

# ### <p style="text-align: right;"> &#9989; Put your name here</p>

# ### Goals for this pre-class assignment
# By the end of this assignment, you should be able to:
# * Import modules into Python and understand how to use them.
# * Use Python's <code>numpy</code> module to do simple calculations
# * Use <code>matplotlib</code> and the <code>pyplot</code> submodule to make plots.
# 
# ### Assignment instructions
# 
# Watch the videos below, do the readings linked to below the videos, and complete the assigned programming problems.  Please get started early, and come to office hours if you have any questions! Make use of Teams as well!
# 
# **This assignment is due by 11:59 p.m. the day before class,** and should be uploaded into appropriate the "Pre-class assignments" submission folder.  Submission instructions can be found at the end of the notebook.

# ---
# ### Some possibly useful links
# 
# Before we dive into the pre-class assignment, here are some links that might be useful if you're looking to learn some extra iPython (which is what the Jupyter Notebooks are built on) and Jupyter Notebook skills:  
# 
# * [IPython tutorial](http://ipython.readthedocs.org/en/stable/interactive/tutorial.html) -- this contains some *very* useful suggestions about IPython commands that allow you to get help on Python, figure out what specific variables or objects do, and many other things.
# 
# * [Jupyter notebook tips and tricks](http://blog.dominodatalab.com/lesser-known-ways-of-using-notebooks/) -- some clever things you can do with Jupyter notebooks
# 
# These are not things you _have_ to learn, but for those looking to push their limits, these pages might be useful!

# ---
# ## Python Modules
# The following video introduces the concept of Python "modules" which are extra software libraries that you can import into your Python environment in order to add new functionality to Python that it doesn't have by default. Python modules are often created because they include commonly used and generally useful code, like mathematical functions or plotting routines. You may have noticed that we've actually already been using one module quite regularly, the <code>YouTubeVideo</code> module.
# 
# Watch the video and then answer the questions below. (If the YouTube video work won't, try the [MediaSpace version](https://mediaspace.msu.edu/media/Modules+in+python/1_wdxtzbr2))

# In[1]:


# Imports the functionality that we need to display YouTube videos in a Jupyter Notebook.  
# You need to run this cell before you run ANY of the YouTube videos.
from IPython.display import YouTubeVideo

# Video on Modules in Python
# Make sure to watch it in full-screen mode!
YouTubeVideo("chBLLNBGoEE",width=640,height=360)  # modules and pyplot


# ---
# ### The `numpy` Module
# 
# In the video above, we reference the `math` module. While it is a useful and powerful module, we are going to put it aside in favor of an even more powerful module, "NumPy" or `numpy`. The `numpy` module has many purposes beyond doing calculations that we will explore in later classes, but for now, we will only use it for numbers.
# 
# **Watch this video on [MediaSpace](https://mediaspace.msu.edu/media/The+numpy+Module+for+Doing+Math/1_h1lnbsug) for a brief introduction to using `numpy` for calculations** (you might notice it is very similar to the `math` module for this purpose!).
# 
# https://mediaspace.msu.edu/media/The+numpy+Module+for+Doing+Math/1_h1lnbsug

# In[2]:


YouTubeVideo("e0WUrM-P9QI",width=640,height=360)


# ### Useful references:
# In addition to the video, the following references may be useful for your pre-class and in-class assignments:
# 
# * [The Python NumPY module](https://numpy.org/doc/stable/reference/routines.math.html) - contains a list of numpy mathematics commands
# * [The matplotlib website](http://matplotlib.org/stable) - where you can find all information about the matplotlib package
# * [The matplotlib gallery](https://matplotlib.org/stable/gallery/index.html) - lots of cool visualizations that can be made with matplotlib
# * [The Pyplot tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html) - the pyplot tutorial.  A good place to get started.
# * [A summary of pyplot commands](https://matplotlib.org/stable/api/pyplot_summary.html) - more extensive documentation on pyplot.

# ---
# ## Working with matplotlib
# 
# &#9989;&nbsp; **Question 1:**
# The cell below contains **four** lists of data, which correspond to two sets of X and Y values.  Use matplotlib to make a plot of these datasets. Make your plot with the following guidelines:
# 
# * The first pair of lists (x1, y1) should be drawn with a ***thick*, blue, dashed line**.
# * The second pair of lists (x2, y2) should be drawn with **red diamonds**.
# * Make the width of the plot extend from 0 to 20 and height of the plot extend from 6 to 16. This will help make the image bit easier to see.
# * Add axis labels to the x and y axes, with whatever text you like.
# 
# Use the [Pyplot Tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html) for inspiration, and in particular you can find instructions on how to create different types of characters and line types in the [pyplot 'plot' command documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot).
# 
# **Note**: It is important to remember that any time you need a module, you **need to import it**. A good coding practice is to put all of your import commands at the top of your code block. Try to get into the habit of always importing the modules you are going to need **first**, before writing the rest of your code. If you realize you need another module, add it to your list at the top, don't just insert it into the body of the code randomly.
# 
# **Another Note**: Your plots might look different than the ones in the video because <code>matplotlib</code> has been updated to a new version since that video was made.

# In[ ]:


# ensures that the plots made by matplotlib/pyplot show up in the notebook!
get_ipython().run_line_magic('matplotlib', 'inline')

# imports the pyplot module from matplotlib
import matplotlib.pyplot as plt    

x1 = [2,4,6,8,10,12,14,16,18]
y1 = [10,8.25,7.5,7,6.75,7,7.5,8.25,10]

x2 = [5, 15]
y2 = [15, 15]

# put your plotting commands below this comment!


# ## Using the numpy module to compute new values and matplotlib to plot them
# 
# Now we want you to try to use various components of everything you just learned in the video, and things you've learned in class up to this point, to make a new plot. This will require that you use the `numpy` module, the `pyplot` module, and probably loop (or two).
# 
# Just like with `matplotlib`, when you need/want to use `numpy`, you need to import that as well, we normally use `import numpy as np` -- make sure to put this in your code cell below!
# 
# &#9989;&nbsp; **Question 2**: Using the values from the `x1` list above, make a plot of $f(x) = \sin(x)$ using a green line and $f(x) = \cos(x)$ using an orange line. Label your plot so that the x-axis reads "x", and the y-axis reads "f(x)".
# 
# **Hint**: The first step will be to figure out a way to calculate the sine and cosine values of `x1` and store them. For calculating sine and cosine values, you can use `np.sin()` and `np.cos()`. For storing these new values in your list, you might want to review how the `append()` function works for lists.
# 
# **Extra challenge**: See if you can figure out how to use the `label` parameter in the `plt.plot()` function and the `plt.legend()` command to add a legend your plot that identifies each line appropriately.

# In[ ]:


# put your python commands here, make sure to include comments in your code using the "#" symbol


# &#9989;&nbsp; **Question 3**: Now that you've been able to plot some functions that _look_ like sine and cosine, we want to make them look __more__ like sine and cosine by calculating more data points for our curves. One way of doing this is to create a more dense list of values that we will pass to the sine or cosine function. We created a list called `x1` for you that you used for the plots you made above, but it didn't have enough values to make the curves look very smooth (we fired the person that made that list).
# 
# Your goal is to create a list called `x_list` of $x$-values from 0 to $2\pi$ with a spacing of 0.1 between each value (you might want to use the numpy module for obtaining a value for $\pi$, which can be accessed with `np.pi`). Then plot cosine and sine over this interval with the same axis labels and colors as the plot you made above. 
# 
# **Hint**: To create your list, consider using a while-loop, that stops once the increment has surpassed $2\pi$. The while-loop should  _append_ new values to `x_list`, starting at 0 and adding 0.1, appending that to the list, then adding 0.1 to the previous value, appending that value to the list, and so on. We will see other methods of creating lists like this in the future by some other very helpful modules. (Please do not hard code the values of your list by hand. If you get stuck, just ask one of the instructors for help via Teams.)

# In[ ]:


# put your python commands here, make sure to include comments in your code using the "#" symbol


# ---
# ## Checking in on prior knowledge
# 
# As we work on learning new things, it can be useful to check-in now and again on some of our previous skills and make sure they're still fresh. **Work through** the following prompts to revisit your knowledge of using lists and loops.
# 
# #### Assigning students to kindergarten
# 
# Imagine that you are working for the school board, and you need to determine which children should enroll in kindergarten. You are given a list below(`children_list`), where each entry is another list with two values: the child's name and the month they were born in. 
# 
# 
# &#9989; **Task**: The cutoff date for enrollment is August, meaning that all children born after July (7th month) should be enrolled in kindergarten. **Write a piece of code that selects the students to be enrolled in kindergarten and appends their names to the list `kinder_students`.**
# 
# Some *optional* starter code has been provided for you.

# In[ ]:


children_list = [['Maxine Reed',1], ['Luz Ryan',10], ['Betty Fleming',9], ['Sherman Powers',6], ['Jerald Santos',8], ['Alberta Flowers',7], ['Lillie Nguyen',3], ['Martha Jackson',8], ['Troy Wilkins',11], ['Eric Mendez',11], ['Violet Ramsey',2], ['Beth Thompson',9], ['Erik Craig',5], ['Hugo Ray',12], ['Linda Nash',2], ['Laura Banks',12], ['Israel Pierce',8], ['Dora Caldwell',5], ['Agnes Matthews',11], ['Norma Fox',9], ['Marian Miller',11], ['Alfredo Cox',9], ['Manuel Black',4], ['Beatrice Sanders',2], ['Bruce Joseph',5], ['Guadalupe Allison',2], ['Sheri Carter',9], ['Floyd Hines',7], ['Abel Hamilton',8], ['Angel Jones',9], ['Carole Webb',6], ['Kelly Brady',9], ['Silvia Mclaughlin',7], ['Jaime Nunez',6], ['Joey Greene',1]]
kinder_students = []

#Write your code here

#Optional starter code (uncomment the line below and use, if you wish)
# for jj in range(len(children_list)):


# #### Talking about code
# 
# Consider the following snippet of code:
# 
# `children_list[3]`
# 
# &#9989; **Task:** In your own words, describe what the square brackets (`[]`) are doing in this code snippet.

# <font size=+3>&#9998;</font> Write your answer here

# &#9989; **Task:** In your own words, describe what the number three (`3`) is doing in this code snippet.

# <font size=+3>&#9998;</font> Write your answer here

# &#9989; **Question:** How would you describe what this code snippet is doing to someone that has never coded before?

# <font size=+3>&#9998;</font> Write your answer here

# ---
# ## An introduction to the CMSE 201 "Code Portfolio"
# 
# As you've probably found already this semester, you often will need to write new code that can be simplified by referencing old code either as a reminder for how something works or as a starting point for your new code. To help you with creating **easily accessible examples** of useful code, you will be expect to develop a "code portfolio" this semester. The details for the code portfolio can be found on the course website, by navigating to the section of the left-hand navigation bar labeled, you guessed it, "Code Portfolio". There is one page that provides a description of the purpose and expectations for the code portfolio ("Code Portfolio Assignment") and another page that provides and example of what a code portfolio might look like ("Code Portfolio Example"). **Go to the course website and check out these two pages**.
# 
# We'll be discussing this portfolio in class and you can use your portfolio as a resource for all of your CMSE 201 quizzes, so **you might want to start building your portfolio as your prepare for Quiz 1**.

# ---
# ## Follow-up Questions
# 
# Copy and paste the following questions into the appropriate box in the assignment survey include below and answer them there. (Note: You'll have to fill out the section number and the assignment number and go to the "NEXT" section of the survey to paste in these questions.)
# 
# 1. What is the `matplotlib` Python package used for? Have you every used this package prior to this assignment? If so, what was the context in which you used it?
# 
# 2. What command do you need to use in your notebook to make sure extra packages like `matplotlib` or `numpy` are available for you to use?

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
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "Pre-class assignments" folder, find the appropriate assignment submission link, and upload it there.
# 
# See you in class!

# &#169; Copyright 2023, The Department of Computational Mathematics, Science and Engineering at Michigan State University.
