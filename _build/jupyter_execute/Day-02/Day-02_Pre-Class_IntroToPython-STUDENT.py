#!/usr/bin/env python
# coding: utf-8

# # Day 2 Pre-class Assignment: Intro to Python

# <p style="text-align: right;"> &#9989; Put your name here</p>

# ## Goals for today's pre-class assignment
# 
# * Explore the nature of flipped classrooms and why we used a flipped classroom model in CMSE 201
# * Learn more about Jupyter notebooks and Markdown 
# * Write a Python program to make simple calculations
# * Work with number and string data types
# * Work with the list data type
# * Learn how to do order-of-magnitude approximations

# **This assignment is due by 11:59 p.m. the day before class,** and should be uploaded into the appropriate "Pre-Class Assignments" submission folder on D2L.  Submission instructions can be found at the end of the notebook.

# ---
# ## NOW PAUSE AND READ THIS!
# The following cell must be executed in order for YouTube video to run within the notebook. If you ever find that your YouTube videos are throwing an error claiming that "`YouTubeVideo is not defined`", it likely means that this little piece of code is either missed or was never executed.

# In[1]:


# Imports the functionality that we need to display YouTube videos in a Jupyter notebook.  
# You need to run this cell before you run ANY of the YouTube videos.
from IPython.display import YouTubeVideo


# &#128721; **STOP!!!** Did you run the cell above (by hitting "shift+enter") as suggested above? Your videos _will not work_ if you do not execute that cell!

# ---
# # Part 1: What is a Flipped Classroom?

# One aspect of CMSE 201 that is very important to understand, aside from Python programming, is understanding how the class is structured. CMSE 201 is being taught using what is known as the "flipped classroom" model. This may or may not be familiar to you, so watch the following video on what a flipped classroom is to help you get up to speed.

# In[2]:


# Watch this short video to get an overview of what a "flipped" classroom is
YouTubeVideo("ojiebVw8O0g",width=640,height=360)


# If the embedded YouTube video isn't working for you, try this link: https://mediaspace.msu.edu/media/The+Flipped+Classroom+Model/1_v550t3pf

# In short, a flipped classroom has students spending time outside of class working through instructional materials developed by the professor known as pre-class assignments. In the context of this course, this will entail things such as watching video lectures made by the instructional staff or found online, reading articles, and working through structured coding activities. One benefit to doing this is it allows students to learn from these materials at their own pace. During a lecture, students must work at the pace of whoever is giving the lecture. But here, one can rewind videos as needed, reread passages, or move past material they feel they have already mastered.
# 
# The main purpose of the work being done at home is so that the time in class can be spent working on what would have traditionally been labeled as “homework assignments” with other students in this class. We will be referring to these as "in-class assignments." During these in-class assignments, the instructional staff are there to provide focused support where needed and help to alleviate any confusion surrounding the material. This model of instruction allows for students to get more one-on-one attention from teachers as well as additional support that comes from working with other people. 
# 
# Need an example of how this works? Here’s an example from our own state! Watch the following video and think about what you’re seeing being done here (And yes, we know vine isn’t a thing anymore).

# In[3]:


# Watch this video for an example of how flipped classrooms are being used right here in Michigan
YouTubeVideo("G_p63W_2F_4",width=640,height=360)


# If the YouTube link is not working for you, try this one: https://mediaspace.msu.edu/media/What+a+%27flipped%27+classroom+looks+like/1_nmznu0q5

# The classroom is “flipped” in the sense that what would have traditionally been done in class (e.g. lecturing) is now being done at home (pre-class assignments), and the aspects that would normally be done at home (in-class assignments) is being worked on during class where the instructional staff can provide needed support.
# 
# The rationale for adopting this model in the specific context of our course is so that time outside of class can be spent learning about the underlying concepts of computational modeling and data analysis, and in-class time can be spent ***doing*** computational modeling and data analysis.
# 
# This approach to learning might be quite different than what you are used to, especially if most of your prior classes have used traditional lecture formats. However, although this classroom experience is different, the end result will still be the same -- you **will** learn the content! In fact, research has shown that there are many benefits to learning in a flipped classroom and many times students learn **more** than they would in a more traditional classroom.
# 
# Of course, in order to get the most of out of the flipped classrooms model used by CMSE 201, **you need to complete the pre-class assignments and fully engage with the in-class activities**. If you don't invest the time before coming to class, you will find that the in-class activities are much more challenging. 
# 
# If you have any questions about the format of CMSE 201, contact your section instructor!

# ---
# # Part 2: Working on Python fundamentals and thinking about "Order-of-magnitude" approximations
# 
# ## 2.1 Jupyter notebooks and Markdown
# 
# The following video will provide you with a bit more information about Jupyter notebooks, how they work, and how you can use them to write both code and text. Note that when you execute the cell below, the code will run only a portion of the video, going from ~3:30 to ~11:30. You only need to watch that portion of the video as the rest of the video is related to material from past versions of CMSE 201.

# In[4]:


# Watch this video to learn about Markdown in Jupyter notebooks
# Please get familiar with this, since we will be using these all semester
YouTubeVideo("zSDfRY8-3QE",width=640,height=360,start=202,end=719)


# If the YouTube link doesn't work for you, try this one: https://mediaspace.msu.edu/media/Jupyter+%28markdown%29%2C+Python+and+Variables+%28strings%2C+floats%2C+lists%2C+arrays%29/1_nsf6zsu2?st=210&ed=713

# &#9989; **Question 1:** Create a cell below, write your first name in italics and last name in bold. 

# ## 2.2 Python 101
# 
# Watch the following video to see an example of how to write a very simple piece of code in Python.

# In[5]:


# Write a simple Python program by example 
YouTubeVideo("cCLB1sNpNYo",width=640,height=360)


# If the YouTube video doesn't work, try this link: https://mediaspace.msu.edu/media/Writing+a+simple+Python+program+by+example/1_cvqav1t0

# &#9989;&nbsp; **Question 2:** In the cell below, write a simple program to calculate the area of a rectangle, where you give it the length and width of the rectangle as variables, store the area in a third variable and print it out.  Add comments to each line (using `#`) to explain what you're doing!

# In[ ]:


# Write your Python program here.  Don't forget that you execute your program by holding
# down 'shift' and pressing 'enter'



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 2.3 Variable types 
# 
# Watch the following video to learn a bit about variable types in Python

# In[6]:


# Watch this video to learn about some fundamental Python variable types 
YouTubeVideo("yv7klK57Ezc",width=640,height=360)


# If the YouTube video doesn't work, try this link: https://mediaspace.msu.edu/media/Some+fundamental+python+variable+types/1_sqs5qxoo

# &#9989;&nbsp; **Question 3:** In the cells below, 
# * Create a variable containing a floating-point number and a second variable containing an integer. 
# * Turn both into strings, concatenate them, and store the result in a new variable. 
# * Print out the *last* value in your concatenated variable.  
# You can use more than one cell if you need to print out multiple quantities!

# In[ ]:


# Write your program here, using multiple cells if necessary. Add extra cells using
# the 'Cell' menu at the top of this notebook.  Don't forget that you can execute 
# your program by holding down 'shift' and pressing 'enter' in each cell!




# ## 2.4 Approximation and modeling

# In[7]:


# Watch this video to learn about order-of-magnitude approximation and how to build a model
# We will do more model-building in class; make sure you are comfortable with the concept
YouTubeVideo("rVhV_9YZZXw",width=640,height=360)


# If the YouTube video doesn't work, try this link: https://mediaspace.msu.edu/media/order-of-magnitude+approximation/1_59s5sqk5

# &#9989;&nbsp; **Question 4**
# 
# As a human being, you need water to survive. 
# 
# How many Olympic-sized swimming pools could you fill with 
# the water an average human being will drink in their lifetime? 
# 
# Create a cell below, explain how you would solve this problem and provide 
# an estimate of the answer (and range of possible solutions).
#     

# ### Having problems? 
# 
# If you're running into issues with any parts of this pre-class assignment, **you should trying sending a message in the CMSE 201 "help" channel in Teams**. Some of your fellow students or one of the instructors might be able to lend a hand!

# ---
# # Part 3: Follow-up Questions
# 
# Copy and paste the following questions into the appropriate box in the assignment survey include below and answer them there. (Note: You'll have to fill out the section number and the assignment number and go to the "NEXT" section of the survey to paste in these questions.)
# 
# 1. Why does CMSE 201 use a "flipped classroom"?
# 
# 2. When might you use a "string" variable type versus an "integer" variable type in Python?
# 
# 3. What symbol do you use to include "comments" in your Python code?

# ---
# ### Assignment wrap-up
# 
# Please fill out the form that appears when you run the code below.  **You must completely fill this out in order to receive credit for the assignment!** Press "shift + enter" to execute the cell and bring up the assignment survey.

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
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "Pre-class assignments" folder, find the appropriate submission folder link, and upload it there.
# 
# See you in class!

# &#169; Copyright 2023, Department of Computational Mathematics, Science and Engineering at Michigan State University.
