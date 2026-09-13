#!/usr/bin/env python
# coding: utf-8

# # Day 4 Pre-class Assignment: Introduction to Data Ethics: Data and Algorithmic Bias

# ### <p style="text-align: right;"> &#9989; Put your name here</p>

# ## Goals for today's assignment
# 
# By the end of this assignment, you should be able to:
# * Identify how bias occurs in data and algorithms
# * Understand the impact data and algorithmic bias has on people
# * Apply practices to look for and minimize bias in your work and others
# * Construct your personal academic integrity statement
# * Practice with lists and loops

# # 1. Introduction

# Data and algorithms are everywhere, and we encounter them everyday. Streaming services use the information you've provided on previous shows and movies you've watched to give more accurate recommendations. Advertisements are customized to us based on our search histories. As students dealing with data and constructing your own algorithms, you'll have even more involvement in these processes. 

# &#9989;&nbsp; **Question**: 
# 
# **Give an example when you've interacted with data or algorithms outside of this class:**

# <font size="+3">&#9998;</font> *Write your response here*

# We give a lot of power to data and algorithms. Perhaps you've heard someone say, "look at the data/numbers," or "it's just fact." Data-driven and evidence-based thinking is a very important skill that can lead to well-informed, insightful decisions. However, we must also recognize limitations data may have. 
# 
# While using data, it is important to ask ourselves:
# 
# 1) **Who collected this data, and do they have a motivation to highlight a certain perspective?**
#   * This is similar to watching the news- each network has it's own bias and leanings. Several news channels might tell the same news story very differently. It is our job to tease out the most complete story we can. Data is not neutral.
#   
# 2) **Who/What does this data exclude?** 
#   * Often times people who have been historically marginalized find themselves erased in data. For example, in data that includes race, indigenous people may find themselves grouped in the "others" category, and data including gender may not take into account those who do not identify as male or female. In dealing with human data, it is important to remember that it cannot fully capture the complexity of the people a dataset includes. Especially with sensitive data, the trauma and full stories are missing, so understanding context is vital.
#  
# 

# # 2. What is data bias?

# <img src="https://images.prismic.io/sketchplanations/f2fdb7cb-f126-4897-ad78-4fd11c743172_SP+723+-+Sampling+bias.png?auto=format&ixlib=react-9.0.3&h=1887.6833845104059&w=1600&q=50&dpr=2" width=325px>
# 
# Image from: https://sketchplanations.com/sampling-bias 

# Bias is defined to be "*prejudice in favor of or against one thing, person, or group compared with another, usually in a way considered to be unfair.*" Data bias occurs when parts of a dataset are overemphasized, underemphasized, or are completely nonexistent. 
# 
# ---
# &#9989;&nbsp;**Task**:
# 
# **Read the article at [this link](https://towardsdatascience.com/types-of-biases-in-data-cafc4f2634fb) that highlights different types of data bias**. While this is discussing machine learning, it is applicable to anyone collecting, using, and visualizing data. Don't be discouraged if you are unclear about machine learning.
# 
# 

# &#9989;&nbsp; **Question**:
# 
# **How has (data) bias affected you? This does not have to include you doing data science, but in your everyday life as a person, consumer, fan, etc. Give an example.**
# 
# 

# <font size="+3">&#9998;</font> *Write your response here*

# **Data bias can lead to well intentioned algorithms outputting biased results. When those results and biased data are used in the algorithm, it perpetuates a cycle of bias.**

# # 3. Data Bias and Algorithmic Bias in the Real World

# <img src="https://beeckcenter.georgetown.edu/wp-content/uploads/2022/03/Getting-to-the-Root-1024x662.png" width=700px>
# 
# source: https://beeckcenter.georgetown.edu/foundation-of-a-successful-data-project-identify-and-mitigating-bias/

# &#9989;&nbsp;**Task**:
# 
# **Watch the videos below and answer the reflection questions after each video.**

# In[1]:


# Imports the functionality that we need to display YouTube videos in a Jupyter Notebook.  
# You need to run this cell before you run ANY of the YouTube videos.

from IPython.display import YouTubeVideo  


# In[2]:


# Video on how algorithms spread bias

YouTubeVideo("1z9KsNoAmFA",width=640,height=360)  


# &#9989;&nbsp;**Question**:
# 
# **Write a paragraph reflecting on the video. Be prepared to discuss these videos and your reflections in class. Consider answering the questions below, but you are not limited to them:**
# 
# 1. Which example of data and algorithmic bias was most impactful and surprising to you? Why?
# 
# 2. If you were explaining this video to a friend who hadn't watched it, what would you tell them? What are the major takeaways?
# 
# 3. Will this change how you engage with data and algorithms going forward? If so, why and how? If not, why not?
# 
# 4. What is something you can do to fight against bias in algorithms? Both as a user of algorithms, and someone who could help create algorithms in the future.

# <font size="+3">&#9998;</font> *Write your response here*

# In[3]:


# Video on fighting bias in algorithms

YouTubeVideo("UG_X_7g63rY",width=640,height=360)  


# &#9989;&nbsp;**Question**:
# 
# **Write a paragraph reflecting on the video. Be prepared to discuss these videos and your reflections in class. Consider answering the questions, but you are not limited to them:**
# 
# 1. Have algorithms ever not worked as you imagined it was, or misrepresented you? If so, how? If not, what do you think your reaction would be?
# 
# 2. Why was Joy's face not recognized by the software?
# 
# 3. What can you do to improve how you work with data and algorithms? How would you advise the larger data science community on improving their work by minimizing bias?

# <font size="+3">&#9998;</font> *Write your response here*

# ---
# # 4. Craft Your Personal Academic Integrity Statement
# 
# After spending some time thinking about data and algorithm bias and some of the ethical implications of that bias, it's worth spending sometime thinking about how you, personally, are going to approach your development as a user of data and computational tools, especially in the context of your work in this course.
# 
# As you work to develop your computational skills and learn to write evermore complex code, you will like find yourself searching the internet for help. **This is a completely authentic part of becoming a computational professional**. However, **it is important that you use the resources you find on the internet in transparent and honest ways**. This includes being thoughtful about how to give credit to the code authors and websites you lean on when you need to figure out something new.
# 
# Along these lines, the Spartan Code of Honor Academic Pledge was adopted by the [Associated Students
# of Michigan State University (ASMU)](http://asmsu.msu.edu/ASMSU) on March 3, 2016, endorsed by Academic Governance on March 22, 2016, and recognized by the Provost, President, and Board of Trustees on April 15, 2016.   It is important for you to be aware of this pledge as it acknowledges some of our shared code of ethics as members of MSU.  Academic integrity is the foundation for university success and future success. Learning how to express original ideas, cite works, work independently, and report results accurately and honestly are skills that carry students beyond their academic career.
# 
# ---
# **The Spartan Code of Honor Academic Pledge:**
# 
# *As a Spartan, I will strive to uphold values of the highest ethical standard. I will practice honesty in my work, foster honesty in my peers, and take pride in knowing that honor in ownership is worth more than grades. I will carry these values beyond my time as a student at Michigan State University, continuing the endeavor to build personal integrity in all that I do.*
# 
# ---
# 
# 

# &#9989;&nbsp; **Activity**: In the cell below, craft a personal statement of commitment to academic honesty and integrity. As part of this statement, address the following components:
# 1. Why is integrity important to you?
# 2. What values motivate the work that you do?
# 3. Commitment to conducting yourself with integrity
# 4. Acknowledgement that you are aware of the MSU ethical standards for integrity
# 
# 
# **IMPORTANT:** This personal integrity statement will be placed on all of your major homework and exams. (You will be asked to paste your statement into each assignment as an acknowledgement of your committment to ethical behavior).
# 
# Your personal statement may share elements with those of your peers, but it should also, ideally, be unique to you. Try to make something that has personal meaning!

# ---------------
# <font size="+3" color="#009600">&#9998;</font> *Put your statement here*
# 
# I, `_________`, commit to `_______`
# 
# -------------

# 
# If you need a starting place, here is a sample personal statement:
# 
# **Jordan Chen's Integrity Pledge:**
# *I, Jordan Chen, value the opportunity to receive a collegiate education.  Because of this value and the sacrifices of people who have made this possible for me, I commit to studying to the best of my ability, submitting work that is my own, and citing sources when I receive help.  I acknowledge I am aware of the Michigan State University policy concerning academic honesty, plagiarism, and cheating.*
# 
# Additionally, there are numerous examples of such statements on the [internet](https://www.google.com/search?client=firefox-b-1-d&q=personal+academic+integrity+statement). You may find them useful for inspiration.
# 
# ---

# # 5. More Practice With Variables, Lists, and Loops
# ## (Not required, but could be useful for building your skills and providing additional preparation for class)
# 
# If you have some extra time and want some extra practice building on your new Python skills, we encourage you to work through the following examples and exercises. **It is not required that you complete this section to get credit for this pre-class assignment.** However, **you will be writing more lists and loops in class for Day 4**, so if you feel like you need to spend some time practicing this, you may wish to do so.

# ## 5.1 Variables
# 
# Review the following code for examples of how variables can be defined, used, and manipulated.

# In[ ]:


int_var = 7   # Integer variable
float_var = 5.74  # floating point variable
str_var = 'Lightning McQueen'  # string variable

print('1:', 'An integer plus a float works in python:',int_var+float_var)

#You can not do math with strings, but you can concatenate strings (if you turn your variables into strings first)
new_str_var = str_var +' won '+str(int_var)+' Piston Cups.'
print('2:',new_str_var)

# or you can just use a print statement with commas to make meaningful debugging and result statements
print('3:',str_var,'was',float_var+int_var,'times better than any other race car.')

print('4: The value of int_var:', int_var)


# &#9989;&nbsp; **5.1.1 Task**: Write a print statement that concatenates all of the following strings to show the complete quote

# In[ ]:


q1 = 'This grumpy old race car I'
q2 = 'know once told me something,'
q3 = '"It’s an empty cup."'
q4 = '-Lightning McQueen'


# In[ ]:


# put your code here


# ## 5.2 Lists
# 
# A list stores a series of items in a particular order. You access items using an index, or with a `for` loop (ex: `for val in list:`)

# In[ ]:


list_ex = []   # initialize an empty list
list_ex.append('Lightning McQueen')  # append an item to a list
list_ex.append('Doc Hudson')
list_ex.append('Tow Mater')
list_ex.append('Sally Carrera')
print('Print 1:',list_ex)  # print contents of variable or whole blist
list_ex.remove('Tow Mater')  # remove specific entry from list, but only first entry with this value
print('Print 2:',list_ex)  # print contents of variable or list
list_ex.append('Holly Shiftwell')
print('Print 3:',list_ex)
print('Print 4:',list_ex[3])  # print the 4th value in the list 'list_ex'


# **Note:** An important concept with lists is that they have values stored at specific indexes.  It is important to remember the idea of an **Index** (which is the location) and the **Value** (which is the value of the single variable at that index).  
# 
# <img src="https://railsware.com/blog/wp-content/uploads/2018/10/positive-indexes.png" width=800px>
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


# ## 5.3 Loops
# 
# So far, we have learned:
# - `for` loops  (repeats a block of code the number of times described in the "for" statement)
# - `while` loops (repeats a block of code as long as a certain condition is true.)

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


# &#9989;&nbsp; **5.3.1 Task**: Write a loop using one of the types above that prints the entries in list_ex in **reverse order**. There is more than one way to tackle this problem!

# In[ ]:


# Put your code here


# &#9989;&nbsp; **5.3.2 Task**: If you were able to successfully print the list in reverse order, describe how you came up with your solution. If not, describe where you are stuck and what you have tried so far.

# <font size="+3">&#9998;</font> *Write your response here*

# ---
# ## Follow-up Questions
# 
# Copy and paste the following questions into the appropriate box in the assignment survey include below and answer them there. (Note: You'll have to fill out the section number and the assignment number and go to the "NEXT" section of the survey to paste in these questions.)
# 
# 1. In your own words, how would your define algorithmic bias?
# 
# 2. What is one example of something we can do as either users or creators of algorithms and data to help avoid algorithmic bias?
# 
# 3. How are you feeling about your ability to work with lists and loops in Python?

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

# Copyright &#169; 2023, [Department of Computational Mathematics, Science and Engineering](https://cmse.msu.edu/) at Michigan State University, All rights reserved.
