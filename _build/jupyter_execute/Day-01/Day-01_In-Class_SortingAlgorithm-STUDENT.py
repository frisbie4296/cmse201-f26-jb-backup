#!/usr/bin/env python
# coding: utf-8

# # Day 1 In-Class Assignment: Introductions and Sorting Algorithms

# ## 🛑 If you are viewing this on the course website it will not be editable.  Download it as an `.ipynb` file using the link on the top right and then open using Jupyter! 🛑

# ### <p style="text-align: right;"> &#9989; **Put your name here** </p>

# ## Goals for today's in-class assignment
# 
# * Get comfortable with the course website
# * Pratice how to use a Jupyter notebook 
# * Get to know your fellow students
# * Start thinking about algorithm design

# ## The course website and Jupyter

# If you have followed the Software Setup Guide (available on the course website and D2L) then you are well on your way to opening and interacting with Jupyter notebooks. You might have figured this out and are reading this in Jupyter already!  If that is the case you can skip this step.
# 
# **Step 1: Open Jupyter in your web browser.**  On a Mac, open the Terminal and type `jupyter notebook`.  In Windows, open the cmd window and type `jupyter notebook`. Jupyter should open in your web browser.
# 
# **Step 2: Select this notebook and open it.** You will probably find this in your Downloads folder, unless you put it someplace else.  

# **That's all!** If you have opened this in Jupyter you should be able to interact with the cells in this notebook, including running the Python cells below.  The second cell below has a YouTube video on Anaconda and the Jupyter program.  Some of this information has since been updated (***e.g. our notebooks aren't found on D2L but on the [class website](https://cmse.msu.edu/cmse201)***), but we include the video here for your reference. 
# 
# **To make notebook cells that have Python code in them do something, hold down the 'shift' key and then press the 'enter' key.** You'll have to do this to get the YouTube videos to run.

# In[1]:


# Imports the functionality that we need to display YouTube videos in a Jupyter Notebook.  
# You need to run this cell before you run ANY of the YouTube videos.

from IPython.display import YouTubeVideo  


# In[2]:


# Video on Modules in Python

YouTubeVideo("5WSQnGmz3IA",width=640,height=360)  


# If for some reason, the YouTube video will not work for you or you are unable to access Youtube in your location, you can try this link as a backup option: https://mediaspace.msu.edu/media/t/0_hkqjufix

# ---
# # Introductions!
# 
# ### Take a moment to introduce yourself to the people in your group! (10-15 Minutes)
# 
# Introduce yourself to the other students in your group. During your introductions, make sure to let each other know:
# 
# * Your name and your pronouns
# * Your major
# * Whether you're new to coding or if you have some previous experience
# * "You wake up tomorrow as an animal. What animal would you *least* want to wake up as?"
# 
# **Make sure you listen to each other when doing the introductions as this is your first opportunity to start to get to know your classmates!**

# <font size=6 color="#009600">&#9998;</font> *Put the information for each of your groups members here.*  (reminder: double-click on this cell to go into "edit mode" and then hit shift+enter when you're done)*
# 
# Member Name1, Pronouns, Major, Coding Experience, Animal
# 
# Member Name2, Pronouns, Major, Coding Experience, Animal
# 
# ...
# 

# ---
# # Background information on algorithms
# 
# This video contains information about what an algorithm is and how they can be used.  We'll watch this as a class before today's in-class activity.

# In[3]:


# Video on Algorithms and Programs
# Watch it in full-screen mode if it's too small for you.

YouTubeVideo("jT0KZ849fak",width=640,height=360)  


# Here is the Mediaspace link if the YouTube link is not working: https://mediaspace.msu.edu/media/1_b20az67d

# ---
# # Today's activity:  Sorting algorithms
# 
# **The goal: Design an algorithm that sorts a group of people by their birthday (Jan 1st to Dec 31st). The catch is that it can only ask the people yes-or-no questions.**
# 
# Details:
# * The "input" to this algorithm is a set of people, in a given (random) order.
# 
# * The "output" of this algorithm is the same set of people, but arranged by birthday.
# 
# * The algorithm can change the order of people in the list and can ask for information, but each person can only respond "yes" or "no".  
# 
# Examples: 
# 
# * "Were you born in July?"
# 
# * "Were you born on February 2nd?"
# 
# ### 1) **As a group,** design a sorting algorithm (20-25 minutes)
#    **Use a real whiteboard or virtual whiteboard app like [Google Jamboard](https://jamboard.google.com/) or the [Aww app](https://awwapp.com/)** to plan out your algorithm by sharing a link with your group. 
#    
# **Write your algorithm in words in the box below:**

# *your text here*

# ### 2) After you've designed your algorithm, test it on your own group. (10-15 Minutes)  
# 
# **How many steps did it take?**

# *your answer here*

# ## &#128721; STOP AND ASK YOUR INSTRUCTOR TO COME OVER
# 
# ### 3) (Time Permitting) Now form larger groups by joining up with 1-2 other groups (15-20 Minutes)
# 
# Each of the original small groups should take turns implementing their algorithm by sorting the combined members of the other groups. 
# 
# **For each algorithm, keep track of how many steps were required to accurately sort everyone below.**

# *your text here*

# ### 4) (Time Permitting) Once each team has tested their algorithm take a few minutes to discuss each other's algorithms and the nature of the process in general
# * What worked well and what didn't?
# * Are there ways to make your algorithm work more efficiently?
# * Which algorithm worked the best and why?
# * What if the individuals that you were trying to sort could ask questions of each other?
#     
# **Answer these questions in the box below**

# *your answer here*

# ---
# ## Assignment wrapup
# 
# Please fill out the form that appears when you run the code below. ***For today's assignment, ignore the part about pre-class assignment.*  You must completely fill this out in order to receive credit for the assignment!** 

# In[ ]:


from IPython.display import HTML
HTML(
"""
<iframe 
	src="https://cmse.msu.edu/cmse201-ic-survey" 
	width="800px" 
	height="600px" 
	frameborder="0" 
	marginheight="0" 
	marginwidth="0">
	Loading...
</iframe>
"""
)


# ---

# ### Submit this assignment by uploading it to the course Desire2Learn web page.  
# Go to the "In-class assignments" folder, find the assignment submission link for Day 1, and upload it there.
# 
# #### Congratulations, you're done!
# 
# Make sure to complete the **Pre-class assignment before next class.** See you next class!

# &#169; Copyright 2023, Department of Computational Mathematics, Science and Engineering at Michigan State University.
