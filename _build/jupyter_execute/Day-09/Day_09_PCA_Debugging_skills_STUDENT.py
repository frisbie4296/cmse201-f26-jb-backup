#!/usr/bin/env python
# coding: utf-8

# # Day 9 Pre-class Assignment: Tools for Debugging Code
# 
# 

# ### <p style="text-align: right;"> &#9989; Put your name here</p>

# ## Goals for today's pre-class assignment
# 
# * Understand the important pieces of information found in a thrown error
# * Use Google to understand the error code being thrown
# * Come up with tests to ensure your code is working correctly. 
# 
# 
# ## Assignment instructions
# 
# **This assignment is due by 11:59 p.m. the day before class,** and should be uploaded into the appropriate "Pre-class assignments" submission folder.  If you run into issues with your code, make sure to use Slack to help each other out and receive some assistance from the instructors. Submission instructions can be found at the end of the notebook.
# 
# **It is important that you do your best to complete the pre-class assignment!** Going through this assignment and trying to complete it to the best of your ability will help to make sure you're prepared for the content that is covered in class. 

# ---
# Knowing how to code means being able to interpret bugs and errors in your code. Learning how to solve problems as they come up will allow you to do just about anything with code.
# 
# In this pre-class assignment, we’ll be talking about two broad topics related to debugging code, which I am calling: Troubleshooting and Testing. Troubleshooting is what you will use when the code itself throws an error at you, while Testing is what you will do when it doesn’t throw an error at you (I.e., ensuring that your code is doing what it’s supposed to!).
# 
# 
# 
# 
# 
# # Part 1: Troubleshooting
# 
# ## 1.1: Understanding Thrown Errors
# 
# For the first part of the assignment, we will dive into the different pieces of an error that Python throws. The following video walks you through those pieces. 
# 
# [MediaSpace link to video](https://mediaspace.msu.edu/media/Debugging_Code_Video/1_ap7gr6o5).

# &#9989;&nbsp; **Question 1:**  What are the two most important pieces of information in a thrown error?

# <font size="+3">&#9998;</font> *Put your answer here*

# &#9989;&nbsp; **Question 2:**  In the video, why did we google `range()`? How did it help us solve the problem?

# <font size="+3">&#9998;</font> *Put your answer here*

# &#9989;&nbsp; **Question 3:**  The following bit of code throws an error when it's run. Do a write-up for the error that gets thrown (I.e., identify the line number, identify the error code, give a plain English description of the error, and say how you fixed the issue).

# In[ ]:


straw_hats = ["Luffy", "Zoro", "Sanji", "Jimbei", "Franky", "Nami"]

for i in straw_hats:
    print(straw_hats[i])


# In[ ]:


#Put the fixed code here


# <font size="+3">&#9998;</font> *Put your answer here*

# ## 1.2 Using Google to Understand Error Messages
# 
# The most powerful tool we have at our disposal for debugging is Google. In this section, we'll discuss how to use Google to make sense of error messages that we may not understand. The following video shows an example of this.
# 
# 
# [MediaSpace link to video](https://mediaspace.msu.edu/media/Debugging_Code_With_Google/1_hnfr14ta).

# The following bit of code is supposed to plot the quantity of materials against the price of the materials. However, it throws an error. 

# In[ ]:


import matplotlib.pyplot as plt

materials_names = ["Eggplant", "Roast Beef", "Eggs", "Strawberries", "Pasta", "Parmesan Cheese"]
materials_quantity = [100, 50, 500, 2500, 100, 10]
materials_prices = [2.5, 25.0, 0.1, 0.20, 12, 30, 4]

plt.plot(materials_quantity,materials_prices)


# &#9989;&nbsp; **Question 4:**  Google the error message that you get and find a site online that gives an explanation for the source of the error. Do a write-up for the error that gets thrown--I.e., identify the line number, identify the error code, give a plain English description of the error, describe how you might fix the issue, **and provide a link to the website you used**.

# <font size="+3">&#9998;</font> *Put your answer here*

# # 2. Testing your code

# The last tool we’ll talk about in this pre-class assignment is code testing. Code testing is where we run little experiments to try to ensure that our code is working correctly. The following video walks through an example of code testing.
# 
# [MediaSpace link to video](https://mediaspace.msu.edu/media/Debugging_Code_Testing/1_gv51qkb3).

# &#9989;&nbsp; **Question 5:**  What is the most common tool we can use for code testing?

# <font size="+3">&#9998;</font> *Put your answer here*

# &#9989;&nbsp; **Question 6:**  The code below has a list of calories from different foods and is supposed to multiply each value by two and sum them together. So, for instance, if we had a list that was `[120, 65, 220]`, then the code should return `(120*2) + (65*2) + (220*2) = 810`. Use testing to ensure this code is working correctly.

# In[ ]:


calories = [270,75,375,475,235,345,340,190]

for ii in range(len(calories)):
    sum_of_cals = 2.0*calories[ii]


# In[ ]:


#Put your code here


# # 3. Debugging your Code
# 
# For this last problem, you will use an error that you have encountered in your work--in your pre-class assignments, in-class assignments, homework assignments, or literally anything else. This isn't meant to be something that you're necessarily stuck on; just an example of how you debug code. 
# 
# &#9989;&nbsp; **Question 7:**  Copy over your buggy piece of code.

# In[ ]:


# Put your buggy code here


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

# &#169; Copyright 2019,  Michigan State University Board of Trustees
