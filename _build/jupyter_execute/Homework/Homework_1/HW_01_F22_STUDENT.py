#!/usr/bin/env python
# coding: utf-8

# # Homework 1: Introduction to Variables, Lists, and Loops

# ### <p style="text-align: right;"> &#9989; **Put your name here** </p>

# # __CMSE  201 &ndash; Fall 2022__
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
# - **Utilize variables and lists to store data**
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
# **This assignment is due at 11:59 pm on Sunday, September 18th.** It should be uploaded into the "Homework Assignments" submission folder for Homework #1.  Submission instructions can be found at the end of the notebook.

# # Version check
# 
# Before you begin, make sure your Jupyter kernel is Python3. There are significant differences between Python2 and Python3, and we will use Python3 in this course. The kernel type at the upper-right corner should say "Python3", and the following code should show a version 3.x.y.
# 
# If your kernel is Python2, try selecting Python3 from the Kernel menu above under the submenu "Change kernel". If that does not work, consult the Slack help channel for assistance.

# In[1]:


import sys
print(sys.version)


# ---
# ## Grading
# 
# Academic integrity statement (2 Points)
# 
# 0. Going to Office Hours (8 Points) 
# 1. Looping by Index (10 Points)
# 2. Looping by Value (10 Points)
# 3. While loops (10 Points)
# 4. Debugging with Lists and Loops (10 Points)
# 
# Total points possible: **50**
# 
# ---

# ## Academic integrity statement (2 Points)
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
# (At minimum) Go to one office hour session ​(it doesn’t matter which one you go to). Come with one question that you would like to talk about. It can be big or small. Ask your question. All of the instructors for CMSE 201 (section leads, TAs, and LAs) will be adding to a running list of folks that we see during office hours; as long as your name appears on the list, you’ll get credit for this part of Homework 1.
# 
# **NOTE:** The day when the homework is due (**Friday, September 16**) will be the busiest time for folks to go to office hours. You are **STRONGLY** encouraged to go to office hours before Friday to get credit for this part of this assignment. (You should still feel free to go to office hours on Friday for help, though!)
# 
# You can find the office hours calendar on the [course website](https://cmse.msu.edu/cmse201).

# ---
# ## 1. Looping by Index (10 Points)
# 
# It’s important to understand how to use the indices to access elements of a list and how to use loop variables in `for` loops. For the following exercises, we’ll be focusing on **"looping by index."**
# 
# **Note:** Each of these problems provides you with a bit of starter code. You *must* use the provided starter code to answer the questions.
# 
# Below is a list (`animals`), which you will use to answer the subsequent questions.

# In[4]:


animals = ["Cat", "Dog", "Bird", "Pig", "Cow"]


# ### &#9989;&nbsp; 1.1 Task (2 Points)
# 
# Use the following starter code to print out the indices 0 through 4 **AND** all of the values in the `animals` list. You must loop by index. Your final result should look like:
# 
# ```
# 0 Cat
# 1 Dog
# 2 Bird
# 3 Pig
# 4 Cow
# ```

# In[ ]:


# write your answer here, starting with the given code
for a in range(len(animals)):


# ### &#9989;&nbsp; 1.2 Task (3 Point)
# Now that we know which indicies corresponds to each animal, lets try printing out the same list, but this time switching `Dog` and `Pig` in the print statement by changing indices. Use the starter code below. You must loop by index. Your final result should look like:
# ```
# 0 Cat
# 1 Pig
# 2 Bird
# 3 Dog
# 4 Cow
# 
# ```

# In[7]:


# write your answer here, starting with the given code
for b in range(len(animals)):


# ### &#9989;&nbsp; 1.3 Task (3 Points)
# 
# Lets try slicing an array. For this task, we are going to be printing the same output that you did in question 1.1, only this time, it will be backwards. You must loop by index. Your final result should look like this:
# ```
# 4 Cow
# 3 Pig
# 2 Bird
# 1 Dog
# 0 Cat
# 
# ```

# In[36]:


# write your answer here, starting with the given code
for c in range(len(animals)):


# ### &#9989;&nbsp; 1.4 Task (2 Points)
# 
# Now we are going to only extract one value and index. Try to only print out **bird** from the `animals` list.

# In[1]:


# write your answer here


# ---
# ## 2. Looping by Value (10 Points)
# 
# ### Example (goes with Part 1)
# 
# In all of the questions above in the previous problem, we had you **"loop by index."** However, we can also **"loop by value,"** as the example below demonstrates.

# In[34]:


for animal in animals:
    print(animal)


# ### &#9989;&nbsp; 2.1 Task (2 Points)
# 
# **In the cell below, try to solve each of the problems above using "loop by value." You don’t have to demonstrate success (or failure) for each problem; just tinker with it and see if you can solve them.**

# In[1]:


#Try to solve the problems above using loop by value. 
#This cell won't be graded for correctness; it's basically just scratch work


# ### &#9989;&nbsp; 2.2 Task (4 Points)
# 
# **Which problems can be solved using a "loop by value?" Which ones can NOT be solved using a "loop by value?"**

# *Write your answer here*

# ### &#9989;&nbsp; 2.3 Task (4 Points)
# 
# **Is there a problem that could be solved using “loop by value” that could NOT be solved using “loop by index”? If so, give an example in the (code) cell below. If not, explain why not in the (text) cell below.**

# In[ ]:


# write an example here


# *Write your answer here*

# ---
# 
# ## 3. While Loops (10 Points)

# Your friend has convinced you to help her out with her catsitting business this weekend. She has a bunch of clients who are out of town and need their cats to be fed. You offered to tag along, help drive to different locations, and keep track of the tasks she'll have to do. She gave you some relevant information for the day: the names of cats and the number of cans of food they'll need to eat. The lists below show this information in the same order as the feeding schedule for this weekend.

# In[27]:


cats = ["Steve", "Meowmers", "Leon", "Alexandria", "Mrs. Sneakypaws", "Rudolph", "Lord of the Pineapple", "Sweet Pea", "Olive", "Kanye", "Babette", "Winston", "Gracie", "Longbottom", "Sparty", "Chloe", "White Claw", "Queen Maureen", "Penelope", "The Gobbler"]
cans = [4, 2, 1, 4, 2, 3, 5, 1, 1, 2, 4, 3, 2, 2, 1, 4, 3, 1, 2, 8]


# ### 3.1 Using loops to show information
# 
# You have been given **three** lists, `cats` and `cans`. Write a `for` loop that loops over the lists and prints out the name and number of cans for each cat. You can assume that the elements in the lists correspond to each other (i.e. the 0-th element of `cats` corresponds to the 0-th element of `cans`).

# In[18]:


# write your answer here


# ### 3.2 Using loops to identify an event
# 
# As you look through the list of cats and their diets, you notice that this is a lot of cans of cat food. Your friend is meant to supply the food herself, and as you embark on your journey, you learn that she only has a single 24-pack of cat food cans. She is definitely going to run out of food, and she will need to buy more from the store. 
# 
# Using a `while` loop, print out the name of the cat who will finish the 24-pack.

# In[19]:


# write your answer here


# ### 3.3 Using loops to identify a pattern
# 
# Your friend would also like to know when a cat will be eating the same number of cans as the cat who ate right beforehand. Write a `while` loop to print out the name of the first cat who eats the same amount of food as the cat before.

# In[20]:


# write your answer here


# ---
# ## 4. Debugging with Lists and Loops (10 Points)
# 
# ### 4.1 What is wrong with my code? (5 points)
# 
# In the cell below, there is a piece of code that isn't working. Describe the source of the bug, how you figured it out (Did you Google it? Read the error message? Try random things?), and then fix the bug!

# *Write your answer in this cell. Fix the bug in the cell below.*

# In[2]:


# code to convert Celcius measurements to Fahrenheit

temps_C = [22, 28, 20, 23, 24, 26, 22, 26, 27, 27] # celcius
temps_F = [] # fahrenheit
for t in temps_C: # loop to convert the temperature measurements
    converted_temp = temps_C[t] * 1.8 + 32
    temps_F.append(converted_temp)


# ### 4.2 The code runs, but the output looks off... (5 points)
# 
# In the cells below, there is a piece of code that runs but is not generating the output we want. Describe the source of the bug, how you figured it out (Did you Google it? Read the error message? Try random things?), and then fix the bug!

# *Write your answer in this cell. Fix the bug in the cell below.*

# In[20]:


# code to calculate years it takes to turn $100 into $1000 via interest

interest = .03 # interest level
amount = 100 # original amount
goal = 1000 # ending amount
years = 0

while amount < goal: # loop to calculate the number of years it takes
    years += 1
    amount += amount * (1 + interest)

print(years)


# ---
# 
# ### Congratulations, you're done! ###
# 
# Submit this assignment by uploading it to the course Desire2Learn web page. Go to the "Homework Assignments" section, find the submission folder link for Homework #1, and upload it there.
