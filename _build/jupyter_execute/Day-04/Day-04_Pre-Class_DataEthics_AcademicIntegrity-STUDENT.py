#!/usr/bin/env python
# coding: utf-8

# # Day 4 Pre-class Assignment: Introduction to Data Ethics and Practice with Lists and Loops

# ### <p style="text-align: right;"> &#9989; Put your name here</p>

# ### Goals for Today's Pre-Class Assignment
# By the end of this assignment, you should be able to:
# * Articulate in your own words what **data ethics** means
# * Understand expectations for **academic integrity** in this class
# * Recognize what constitutes **cheating** in a coding class
# * Loop through a list of numbers and strings
# 
# ### Assignment instructions
# 
# Watch videos below, read all included and linked to content, and complete any assigned programming problems.  Please get started early, and come to office hours if you have any questions and make use of Slack!
# 
# **This assignment is due by 11:59 p.m. the day before class,** and should be uploaded into the appropriate "Pre-class assignments" submission folder.  Submission instructions can be found at the end of the notebook.

# ---
# ## 1. Data Ethics
# ![ethics_sm.png](attachment:ethics_sm.png)
# 
# Data and how we interact with data are rapidly reshaping daily life and how we interact in the world.  In this course, you are learning methods and tools to interact with and model data.  It is important for you to be aware of the ethical issues in this space.  
# 
# Watch the video below to start thinking about the role ethics may play in your personal and professional life. If the YouTube video doesn't work, try this link: https://mediaspace.msu.edu/media/Introduction+to+Data+Ethics/1_cieharl7

# In[ ]:


# Don't forget to watch the video in full-screen mode!
from IPython.display import YouTubeVideo  
YouTubeVideo("onqBhQ_CeTE",width=640,height=360)


# &#9989;&nbsp; **Question**: What are some of your personal values that motivate you to act ethically?  How would you complete this sentence: *I value `___________`*
# 
# For example, this can be straightforward as: 
# - I value hard work.  
# - I value getting good grades.  
# - I value the respect of my family.

# <font size="6" color="#009600">&#9998;</font> *Put your answer here*

# ---
# ## 2. Data ethics in this course: Plagiarism
# 
# Plagiarim is the practice of taking someone else's work or ideas and passing them off as one's own.  Please review the following video to understand the definition of plagiarism and cheating in this course. If the YouTube video doesn't work, try this link: https://mediaspace.msu.edu/media/Discussion+of+Cheating+in+a+Coding+Class/1_iroh8u4v

# In[ ]:


# Don't forget to watch the video in full-screen mode!
from IPython.display import YouTubeVideo  
YouTubeVideo("P1sDXH4sdCg",width=640,height=360) 


# &#9989;&nbsp; **Exercise**: Read the information at the [Spartan Code of Honor Academic Pledge](http://splife.studentlife.msu.edu/spartan-code-of-honor-academic-pledge).
# 
# Copy and paste the **The Spartan Code of Honor Academic Pledge** below.  This academic pledge is important for your success in this course and at MSU.  During the in-class assignment, we will do a short exercise in writing our own integrity statement.
# 

# <font size="6" color="#009600">&#9998;</font> *Paste pledge here*
# 
# **The Spartan Code of Honor Academic Pledge:**
# 
# "As a Spartan, ..."

# ___
# ## 3. Review of Variables, Lists, and Loops
# 
# Read the following cells and ensure you understand each concept. Complete the empty cells.

# **1. Variables**

# In[ ]:


int_var = 6   # Integer variable
float_var = 5.74  # floating point variable
str_var = 'Hermione'  # string variable

print('1:', 'An integer plus a float works in python:',int_var+float_var)

#You can not do math with strings, but you can concatenate strings (if you turn your variables into strings first)
new_str_var = str_var +' went to Hogwarts for '+str(int_var)+' years.'
print('2:',new_str_var)

# or you can just use a print statement with commas to make meaningful debugging and result statements
print('3:',str_var,' was ',float_var+int_var,' years old when she first went to Hogwarts.')

print('4: The value of int_var:', int_var)


# &#9989;&nbsp; **1.1 Task**: Write a print statement that concatenates all of the following strings to show the complete quote

# In[ ]:


q1 = 'It is our choices,'
q2 = 'that show what we truly are,'
q3 = 'far more than our abilities.'
q4 = '-Albus Dumbledore'


# In[ ]:


# Put your code here


# **2. Lists**
# 
# A list stores a series of items in a particular order. You access items using an index, or with a `for` loop (ex: `for val in list:`)

# In[ ]:


list_ex = []   # initialize an empty list
list_ex.append('Harry')  # append an item to a list
list_ex.append('Hermione')
list_ex.append('Ron')
list_ex.append('Frank')
print('Print 1:',list_ex)  # print contents of variable or whole blist
list_ex.remove('Frank')  # remove specific entry from list, but only first entry with this value
print('Print 2:',list_ex)  # print contents of variable or list
list_ex.append('Luna')
print('Print 3:',list_ex)
print('Print 4:',list_ex[3])  # print the 4th value in the list 'list_ex'


# *Note:* An important concept with lists is that they have values stored a specific indexes.  It is important to remember the idea of an **Index** (which is the location) and the **Value** (which is the value of the single variable at that index).  
# ![positive-indexes.png](attachment:positive-indexes.png)
# 
# <sub>Image from: https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/</sub>
# 
# To access an element by its index we need to use square brackets.
# 
# 

# In[ ]:


# Example of Values and Indexes
index = 1
print(list_ex[index],'is the value at the', index, 'index.')


# **3. Loops**
# 
# So far, we have learned:
# - for loops  (repeats a block of code the number of times described in the "for" statement)
# - while loops (repeats a block of code as long as a certain condition is true.)

# In[ ]:


# First Loop Type 
for value1 in list_ex:   # loop through all the entries in list "list_ex"
    print('Current entry in variable value is:', value1)  # for each iteration, variable named "value1" 
                                                        #      will be assigned the next entry in "list_ex"


# In[ ]:


# Second Loop Type
for index1 in range(len(list_ex)): # loop through integers from 0 to length of list "list_ex"
                                # for each iteration, variable named "index1"
                                #      will be assigned the next integer in 0 to length of list "list_ex"
    str_now = list_ex[index1]   # assign a variable the content of the index1-th entry of list "list_ex"
    print('The',index1,'entry in list_ex is',str_now)


# In[ ]:


# Third Loop Type
index1 = 0
while index1 < len(list_ex):  # perform a while loop until index1 is equal to or greater than the length of list "list_ex"
    str_now = list_ex[index1]
    print('The',index1,'entry in list_ex is',str_now)
    index1 += 1               # increment whatever is in index1 by +1
    # Note this is the identical result as the for loop in cell above


# &#9989;&nbsp; **3.1 Task**: Write a loop using one of the types above that prints the entries in list_ex in **reverse order**. There is more than one way to tackle this problem!

# In[ ]:


# Put your code here


# &#9989;&nbsp; **3.2 Task:** Now, try completing the same task again (print the entries in list_ex in reverse order), but use one of the different types of loops discussed above.

# In[ ]:


# Put your code here


# ## Follow-up Questions
# 
# Copy and paste the following questions into the appropriate box in the assignment survey include below and answer them there. (Note: You'll have to fill out the section number and the assignment number and go to the "NEXT" section of the survey to paste in these questions.)
# 
# 1. What are two different ways of looping through a list?
# 
# 2. Explain a benefit for each.

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
	width="800" 
	height="800px" 
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

# Copyright &#169; 2021, [Department of Computational Mathematics, Science and Engineering](https://cmse.msu.edu/) at Michigan State University, All rights reserved.

# In[ ]:




