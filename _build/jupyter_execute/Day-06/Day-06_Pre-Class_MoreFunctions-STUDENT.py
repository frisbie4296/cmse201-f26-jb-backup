#!/usr/bin/env python
# coding: utf-8

# # Day 6 Pre-class Assignment: Thinking more about functions

# ### <p style="text-align: right;"> &#9989; Put your name here</p>

# ### Goals for Today's Pre-Class Assignment
# By the end of this assignment, you should be able to:
# * More easily define and use functions in Python.
# 
# ### Assignment instructions
# 
# Watch any videos below, read all included and linked to content, and complete any assigned programming problems.  Please get started early, and come to office hours if you have any questions and make use of Teams!
# 
# **This assignment is due by 11:59 p.m. the day before class,** and should be uploaded into the appropriate "Pre-class assignments" submission folder.  Submission instructions can be found at the end of the notebook.

# ---
# ## 1. Basic function structure
# 
# The following short video serves as a reminder of the basic structure of a function and how you call functions that you write.<br>
# (If the YouTube video doesn't work, you can access a back-up version on [MediaSpace](https://mediaspace.msu.edu/media/Python+3+Programming+Tutorial+-+Functions/1_px44pw5v))

# In[1]:


# Don't forget to watch the video in full-screen mode!
from IPython.display import YouTubeVideo  
YouTubeVideo("owglNL1KQf0",width=640,height=360)  # Writing functions


# ---
# ## 2. Defining function input parameters
# 
# Here's another short video that reminds you how to define input parameters in Python. The video also points out how you can be specific about defining your input variable to be exactly what you want them to be, without worrying about the specific order of the variables. <br>
# (If the YouTube video doesn't work, you can access a back-up version on [MediaSpace](https://mediaspace.msu.edu/media/Python+3+Programming+Tutorial+-+Function+Parameters/1_kz2894rs))

# In[2]:


# Don't forget to watch the video in full-screen mode!
from IPython.display import YouTubeVideo  
YouTubeVideo("CGRKqnoQGgM",width=640,height=360)  # Defining function inputs


# ---
# ## 3. Setting default function values
# 
# Now that we're comfortable with writing functions and defining our input variables, this next video will show us how to define defaults for our input variables so that we don't always have to define every single input value. This can be useful if we want a function to have a default mode of operation that works *most* of the time, but we still want to be able to change the values of some of the variables when necessary.<br>
# (If the YouTube video doesn't work, you can access a back-up version on [MediaSpace](https://mediaspace.msu.edu/media/Python+3+Programming+Tutorial+-+Function+Parameter+Defaults/1_ahwj3l0l))

# In[3]:


# Don't forget to watch the video in full-screen mode!
from IPython.display import YouTubeVideo  
YouTubeVideo("KeRxe9rll2Q",width=640,height=360)  # Default function parameters


# Now let's try to incorporate the things we learned in the last three videos into one small function.
# 
# &#9989;&nbsp; **Question:** Create a function that takes a person's name as a string input and prints
# 
# `Happy Birthday to < name >`
# 
# where "< name >" is the person's name that is given to the function. **Set up the function so that if no name is given, it just says "Happy Birthday to you!"**. You can give the function any name you want, but you should try to pick a function name that makes sense to someone else who might be using the function! Also, make sure to comment the function to explain what it does!

# In[ ]:


# Put your code here


# ___
# ## 4. Writing functions that Return Values
# 
# The previous three videos focused on defining the input variables for function, giving them defaults, and walking you through different ways to feed your input values into your functions, but they didn't talk about **returning** variables from functions. In Python, we commonly want to write functions that not only take in a variety of input values, but we also want the function to return some new values when the function exits. For example, I might have a bit of code that looks like this:

# In[ ]:


def concatenate_strings(s1, s2, s3):
    combined = s1 + ' ' + s2 + ' ' + s3 + '.'
    return combined


# This function takes in three values, `s1`, `s2`, and `s3`, concatenates (adds together) the three strings into a sentence, and then **returns** that sentence.  That means when I call the function, I can assign a new variable to be the value that is **returned** by the function. Specifically, I might do something that looks like this:  

# In[ ]:


my_sentence = concatenate_strings('otters are','my favorite', 'animal')
print(my_sentence)


# With that first line of code, I've created a new variable called `my_sentence` that stores the result of my `concatenate_strings` function. It is important to note that if I don't intentionally "catch" the returned value from my function, I won't have access to that value later on because the `combined` variable in my function is ***local*** *to the function*. When we say that a variable is local to the function, it means that it can only be accessed in the place that it was created, inside the function. This means that if we simply do:

# In[ ]:


concatenate_strings('otters are','my favorite', 'animal')


# We aren't actually ***storing*** the value we want. Python will print the value to the screen *because* we didn't catch the value with a variable. Again, if I wanted to access that value later, I don't have any way of doing that. The function concatenated the strings, but we never stored the result anywhere, so calling the function was only useful if we wanted to *see* the sentence but didn't care about *using* the sentence. **Remembering to store the output from your functions is very important when writing code!**

# &#9989;&nbsp; **Task**: Trying it yourself
# 
# In the cell below try writing a function called __check_for_strings__ that takes a value as an input argument and **returns** the Boolean value "`True`" if the value is a string and the Boolean value "`False`" if the value is not. While we have been making use of Boolean `True`/`False` values in a variety of ways in class up to this point, we may not have discussed them explicitly previously. You can learn a bit about the Boolean data type [here](https://realpython.com/python-boolean/). Basically, when we evaluate a conditional statement, we either get a `True` Boolean value or a `False` Boolean value -- it really is that simple.
# 
# **Useful tip:** You can use the built-in [`type()` function](https://docs.python.org/3/library/functions.html#type) to determine the type of a variable. You may wanted to experiment with using the `type()` function to convince yourself how it works.
# 
# Once you've completed your function, **make sure you also test your function to ensure that it works as you intend!**
# 
# **Important reminder**: The moment a function comes across a `return` statement, it will exit the function and ignore any code that comes later in the function. This can actually be kind of useful if you want a function to return a value based on set of conditional statements.

# In[ ]:


#Put your code here 


# ## 5. Putting it All Together
# 
# In this section, we are going to level up what we can do with functions!
# 
# So far, you have practiced writing functions with different kinds of inputs, outputs, and default values, but now we will to explore ways of building more complex (but still compartmentalized and transferable) code by combining functions.
# 
# One particularly useful way to build more complex code is to have **functions that call other functions** inside them. 
# 
# When we call a function inside another function, remember to keep in mind [**variable scope**](https://www.w3schools.com/python/python_scope.asp). Any variables the function you are calling inside another function needs will need to be provided as input arguments in your outer function!
# 
# In the cell below, write a function that combines your `concatenate_strings` and `check_for_strings` functions to:
# 1. Take in 3 values
# 2. Check if those 3 values are strings
# 3. If all three are strings, concatenate those strings into one new string
# 4. Return the new concatenated string
# ---
# **Something to think about**: What will your code do if not all three of the values are strings? Implement a way of handling this in your code.

# In[ ]:


# put your code here


# &#9989;&nbsp; **Questions**: Now that your function runs, try to add some default values to your input arguments. 
# 
# 1. What variables would be most useful to have default arguments for? 
# 
# 2. Give an example of a built-in Python function that uses default arguments. Describe what the function does and what purpose the default arguments serve.

# <font size="+3">&#9998;</font> *Put your answers here*

# In[ ]:


# put any code here


# ---
# ## Follow-up Questions
# 
# Copy and paste the following questions into the appropriate box in the assignment survey include below and answer them there. (Note: You'll have to fill out the section number and the assignment number and go to the "NEXT" section of the survey to paste in these questions.)
# 
# 1. What happens if I don't include a "return" statement when writing a python function?
# 
# 2. Why might it be useful to define a Python function that has default values for your input arguments?
# 
# 2. How are you feeling about writing functons in Python, are there any aspects you're still not feeling confident about?

# ---
# ## Assignment wrap-up
# 
# **For convenience, we're going to include a couple of Python function references again so that you can check them out if you're still looking for more information about functions**:
# * [Tutorial on functions in python](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
# * [More function basics with executable examples](http://www.diveintopython3.net/your-first-python-program.html#declaringfunctions)
# 
# **Now**, please fill out the form that appears when you run the code below.  **You must completely fill this out in order to receive credit for the assignment!**

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
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "Pre-class assignments" folder, find the appropriate dropbox link, and upload it there.
# 
# See you in class!

# &#169; Copyright 2023,  Department of Computational Mathematics, Science and Engineering at Michigan State University
