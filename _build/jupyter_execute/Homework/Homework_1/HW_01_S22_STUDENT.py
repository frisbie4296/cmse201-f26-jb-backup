#!/usr/bin/env python
# coding: utf-8

# # Homework 1: Introduction to Loops, Lists, and Dictionaries

# ### <p style="text-align: right;"> &#9989; **Put your name here** </p>

# # __CMSE  201 &ndash; Spring 2022__
# 
# <img src="https://cmse.msu.edu/sites/_cmse/assets/Image/image002.jpg"
#      alt="CMSE Logo"
#      align="right" 
#      height="100" 
#      width="100" />
# 
# 
# ## Learning Goals
# 
# ### Content Goals
# - **Utilize loops to store, access, and manipulate data in a multiple lists**
# - **Write code to execute simple mathematical operations**
# - **Utilize lists and dictionaries to store data**
# 
# 
# ### Practice Goals
# - **Evaluate different ways to solve problems using code**
# - **Diagnose and debug code provided to you**
# 
# 
# ___

# ## Assignment instructions
# 
# Work through the following assignment, making sure to follow all the directions and answer all the questions.
# 
# **This assignment is due at 11:59 pm on Friday, January 28th.** It should be uploaded into the "Homework Assignments" submission folder for Homework #1.  Submission instructions can be found at the end of the notebook.

# # Version check
# 
# Before you begin, make sure your Jupyter kernel is Python3. There are significant differences between Python2 and Python3, and we will use Python3 in this course. The kernel type at the upper-right corner should say "Python3", and the following code should show a version 3.x.y.
# 
# If your kernel is Python2, try selecting Python3 from the Kernel menu above under the submenu "Change kernel". If that does not work, consult the Slack help channel for assistance.

# In[ ]:


import sys
print(sys.version)


# ---
# ## Grading
# 
# Academic integrity statement (1 Point)
# 
# 0. Going to Office Hours (8 Points) 
# 1. Looping by Index (10 Points)
# 2. Looping by Value (10 Points)
# 3. Working with Lists and Dictionaries (9 Points)
# 4. Debugging Dictionary Construction (12 Points)
# 
# Total points possible: **50**
# 
# ---

# ## Academic integrity statement (1 Point)
# 
# In the markdown cell below, paste your personal academic integrity statement. By including this statement, you are confirming that you are submitting this as your own work and not that of someone else.
# 

# <font size=6 color="#009600">&#9998;</font> *Put your personal academic integrity statement here.*

# ## 0. Going to Office Hours (8 Points)
# 
# ### Why are we doing this?
# We want to make sure that everyone knows how to access the resources
# available to you. One of the best resources you have at your disposal is office hours.
# 
# ### What will you do?
# (At minimum) Go to one office hour session ​(it doesn’t matter which one you go to). Come with one question that you would like to talk about. It can be big or small. Ask your question. All of the instructors for CMSE 201 (section leads, TAs, and LAs) will be adding to a running list of folks that we see during office hours; as long as your name appears on the list, you’ll get credit for this part of homework 1.
# 
# **NOTE:** The day when the homework is due (Friday, January 28th) will be the busiest time for folks to go to office hours. You are **STRONGLY** encouraged to go to office hours before Friday to get credit for this part of this assignment. (You should still feel free to go to office hours on Friday for help, though!)
# 
# You can find the office hours calendar on the [course website](https://cmse.msu.edu/cmse201).

# ---
# ## 1. Looping by Index (10 Points)
# 
# It’s important to understand how to use the indices to access elements of a list and how to use loop variables in `for` loops. For the following exercises, we’ll be focusing on **"looping by index."**
# 
# **Note:** Each of these problems provides you with a bit of starter code. You *must* use the provided starter code to answer the questions.
# 
# Below are two lists (`letters` and `indices`), which you will use to answer the subsequent questions.

# In[15]:


letters = ["A","B","C","D","E"]
indices = [1,0,3]


# ### &#9989;&nbsp; 1.1 Task (1 Point)
# 
# Use the following starter code to print out all of the values in the `letters list.

# In[ ]:


for j in range(len(letters)):
    #Write your code here


# ### &#9989;&nbsp; 1.2 Task (1 Point)
# 
# Use the following starter code to print out all of the values in the `indices` list.

# In[ ]:


for a in range(len(indices)):
    #Write your code here


# ### &#9989;&nbsp; 1.3 Task (2 Points)
# 
# Use the following starter code to print out all of the values in the `indices` list **AND** the **first three values in the** `letters` **list**. I.e., your final result should look like:
# 
# ```
# 1 A
# 0 B
# 3 C
# ```

# In[ ]:


for b in range(len(indices)):
    #Write your code here


# ### &#9989;&nbsp; 1.4 Task (3 Points)
# 
# Use the following starter code, as well as both the `indices` and `letters` list, to print out the word `BAD`. I.e., your final result should be:
# ```
# B
# A
# D
# ```

# In[ ]:


for c in range(len(indices)):
    #Write your code here


# ### &#9989;&nbsp; 1.5 Task (3 Points)
# 
# Finally, make a new `indices` list and use the following starter code (and the `letters` list) to print out `ACE`. I.e., your final result should be:
# ```
# A
# C
# E
# ```

# In[ ]:


indices = [] #Make a new indices list
for d in range(len(indices)):
    #Write your code here


# ## 2. Looping by Value (10 Points)
# 
# In all of the questions above in the previous problem, we had you **"loop by index."** However, we can also **"loop by value,"** as the example below demonstrates. 

# In[ ]:


for letter in letters:
    print(letter)


# #### &#9989;&nbsp; 2.1 Task (2 Points)
# 
# **In the cell below, try to solve each of the problems above using "loop by value." You don’t have to demonstrate success (or failure) for each problem; just tinker with it and see if you can solve them.**

# In[ ]:


#Try to solve the problems above using loop by value. 
#This cell won't be graded for correctness; it's basically just scratch work


# #### &#9989;&nbsp; 2.2 Task (4 Points)
# 
# **Which problems can be solved using a "loop by value?" Which ones can NOT be solved using a "loop by value?"**

# *Write your answer here*

# #### &#9989;&nbsp; 2.3 Task (4 Points)
# 
# **Is there a problem that could be solved using “loop by value” that could NOT be solved using “loop by index”? If so, give an example in the (code) cell below. If not, explain why not in the (text) cell below.**

# In[ ]:


#Write an example loop here


# *Write your answer here*

# ---
# ## 3. Working with Lists and Dictionaries (9 Points)
# 
# ### 3.1 Lists (5 Points)
# 
# You have already seen Python "lists" in some of your previous work. 
# 
# ### &#9989;&nbsp; 3.1.1 Task
# **Construct two lists, one with your three favorite kinds of fruit, and the other with an explanation of why each fruit is your favorite. Write a `for` loop that prints out the type of fruit and the explanation for why you like it.**
# 
# *For example*
# 
# I like Oranges because They remind me of Holland. 
# 
# I like Grapes because Purple is the best color.
# 
# I like Clementines because They are the Corgis of oranges.

# In[ ]:


# Put your code here


# ### 3.2 Dictionaries (4 Points)
# 
# Dictionaries are new. They're like lists, in that they provide a means to store multiple values in a single compound variable. The main differences are:
# 
# * Dictionaries store values using *keys*, instead of indices (see image below).
# * You create a new dictionary using curly braces, `{}`, instead of square brackets, `[]`.
# 
# 
# <img src="https://bjc.edc.org/bjc-r/img/python/dictionaries_vs_lists.jpg"
#      alt="List V. Dict"
#      align="center" 
#      height="800" 
#      width="800" />
# 
# 
# 
# #### NOTE:
# A more detailed introduction to dictionaries and their functionality can be found at [W3Schools](https://www.w3schools.com/python/python_dictionaries.asp).

# In[ ]:


#Dictionary example 1: Making a dictionary

state_dictionary = {"Name": "Colorado",
                   "Population": 5758736,
                   "Capital": "Denver",
                   "State Bird": "Lark bunting"}

print(state_dictionary["Capital"])


# In[ ]:


#Dictionary example 2: Looping through keys and values in a dictionary

for key in state_dictionary:
    print("Key: ",key,"    Value: ",state_dictionary[key])


# **Now**, think about an actual (non-coding) dictionary. It's a book with many *values* (definitions), and you look up these values using a specific *key* (word).
# 
# ### &#9989;&nbsp; 3.2.1 Task
# 
# **Choose three or four words and look up their definitions. Construct a dictionary whose keys are the words and whose values are the definitions.** 

# In[ ]:


# Put your code here


# ---
# ## 4. Debugging Dictionary Construction (12 Points)
# 
# Below is a piece of code that is meant to create a dictionary of dictionaries. Specifically, it is supposed to create a dictionary for each state (similar to the previous problem), and then add that dictionary to another dictionary (`all_states_dictionary`) using the name of the state as the key. However, the code is not working! There are several bugs in it. 
# 
# ### &#9989;&nbsp; 4.1 Task (6 Points)
# 
# In the empty code cell below, rewrite the buggy code so that it works properly. 

# In[ ]:


names = ["Arizona", "Nevada", "New Mexico", "Utah"]
populations = [7151502,3104614,2120220,3271616]
capitals = ["Phoenix", "Carson City","Santa Fe","Salt Lake City"]
state_birds = ["Cactus wren","Mountain bluebird","Greater roadrunner","California gull"]

all_states_dictionary = {}

for j in range(len(names)):
    temporary_state_dict = {"Population": populations[5],
                           "Capital": capitals[j]}
    all_states_dictionary[names[2]] = temporary_state_dict

print(all_states_dictionary["Arizona"]["Population"])
print(all_states_dictionary["Nevada"]["Capital"])
print(all_states_dictionary["Utah"]["State Bird"])


# ### &#9989;&nbsp; 4.2 Task (6 Points)
# 
# 
# In the empty markdown cell below, detail all of the bugs that you found in the code. For each bug you found, you should include: 
# 1. The line of code that caused the error(s)
# 2. (Where appropriate) The error code
# 3. A plain english description of the error(s) in the code
# 4. How you solved the error(s)
# 
# (Remember that not all bugs in the code will throw errors!)

# *Put your answers here*

# ---
# 
# ### Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "Homework Assignments" section, find the submission folder link for Homework #1, and upload it there.

# In[ ]:




