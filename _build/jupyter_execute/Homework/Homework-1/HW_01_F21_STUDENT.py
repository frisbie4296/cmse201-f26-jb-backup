#!/usr/bin/env python
# coding: utf-8

# # Homework 1: Introduction to Loops, Lists, and Dictionaries

# ### <p style="text-align: right;"> &#9989; **Put your name here** </p>

# # __CMSE  201 &ndash; Fall 2021__
# 
# <img src="https://cmse.msu.edu/sites/_cmse/assets/Image/image002.jpg"
#      alt="CMSE Logo"
#      align="right" 
#      height="100" 
#      width="100" />
# 
# # Homework 1: Introduction to Loops, Lists, and Dictionaries
# 
# ## Learning Goals
# 
# ### Content Goals
# - **Write code to execute simple mathematical operations.**
# - **Utilize lists to store data**
# - **Utilize loops to store, access, and manipulate data in a multiple lists**
# 
# 
# ### Practice Goals
# - **Debugging practices**
#   - *Isolate and interpret the relevant information in an error code*
#   - *Use print statements to determine the outcome of operations*
# - **Describe code and bugs using plain language**
# 
# 
# ___

# ## Assignment instructions
# 
# Work through the following assignment, making sure to follow all the directions and answer all the questions.
# 
# **This assignment is due at 11:59 pm on Friday, Sept 17th.** It should be uploaded into the "Homework Assignments" submission folder for Homework #1.  Submission instructions can be found at the end of the notebook.

# # 0. Version check
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
# * Practice/Introductory Problems: Lists (5 points)
# * Practice/Introductory Problems: Dictionaries (4 points)
# * Debugging Other People's Code: Buggy Code 1 (4 Points)
# * Debugging Other People's Code: Buggy Code 2 (4 Points)
# * Debugging YOUR Code: Buggy Code 1 (4 Points)
# * Debugging YOUR Code: Buggy Code 1 (4 Points)
# * Coding A Cash Register: Create your Own Test Lists (2 Points)
# * Coding A Cash Register: Calculating Sum (3 Points)
# * Coding A Cash Register: Printing Names and Cost (4)
# * Coding A Cash Register: Multiple Items: Create a New Test List (1 Points)
# * Coding A Cash Register: Multiple Items: Modiyfing Code to Include Copies (5 Points)
# * Coding A Cash Register: Test Your Code (2 Points)
# Total points possible: **42**
# 
# ---

# ---
# # 1. Practice Problems (9 Points)
# 
# ## 1.1 Lists (5 Points)
# 
# You have already seen Python "lists" in some of your previous work. 
# 
# ### &#9989;&nbsp; 1.1.1 Task
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


# ## 1.2 Dictionaries (4 Points)
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
# ### &#9989;&nbsp; 1.2.1 Task 
# 
# **Choose three or four words and look up their definitions. Construct a dictionary whose keys are the words and whose values are the definitions.** 

# In[ ]:


# Put your code here


# # 2. Debugging Other People's Code (8 Points)
# 
# A large part of learning how to code is finding strategies for troubleshooting problems/bugs when they arise. The following exercises will test your ability to identify and solve problems in your code.
# 
# ## An Aside: Turning on Line Numbers
# The errors that Python will throw at you will usually tell you the ***Line Number*** where the error occurred. However, Jupyter notebooks don't always show line numbers by default, so it will be useful to turn them on.
# 
# ### To Turn Line Numbers
# 1. Go up to **view** (right next *Edit* and *Insert*)
# 2. Click **Toggle Line Numbers**
# 
# You should now see line numbers on the left side of your cell(s) when you're editing them.
# 
# ## 2.1 Buggy Code 1 (4 Points)
# 
# **Note:** The first thing you should always do when there is an error is to **look at the line number provided and the specific error code.** You can use these two pieces of information to solve bugs *without needing to understand what the code is doing.* 
# 
# 
# ### &#9989;&nbsp; 2.1.1 Fixing the Code (2 Points)
# The code below is supposed to take a list of protein values, add 10 to each value, and make a histogram.
# 
# **Rewrite the code below so that it achieves the task it is supposed to.**

# In[ ]:


# Buggy Code 1
import matplotlib.pyplot as plt

protein = [32,12,15,34,32,36,28,29,27,32,6,6,27,8,32,3,33,14,38]

for jj in range(len(protein)):
    protein[jj] = protein[jj]+'10'

plt.hist(protein)
plt.show()


# In[ ]:


# Write your solution here


# ### &#9989;&nbsp; 2.1.2 Explaining the Problem and the Solution (2 Points)
# 
# In the space below, explain the problem and your solution. You should include the following information:
# 1. The line of code that caused the error(s)
# 2. (Where appropriate) The error code
# 3. A plain english description of the error(s) in the code
# 4. How you solved the error(s)

# *Explain the problem and solution here*

# ## 2.2 Buggy Code 2 (4 Points)
# 
# **Note** Sometimes the code that you get won't throw an error. *That does not mean it is running correctly.* **You should always check to make sure that your code is running correctly.**
# 
# ### &#9989;&nbsp; 2.2.1 Fixing the Code (2 Points)
# The code below has a list of calories from different foods and is supposed to multiply each value by two and sum them together. So, for instance, if we had a list that was `[120, 65, 220]`, then the code should return `(120*2) + (65*2) + (220*2) = 810`.
# 
# **Rewrite the code below so that it achieves the task it is supposed to.**

# In[ ]:


#Buggy code 2

calories = [270,75,375,475,235,345,340,190]

for ii in range(len(calories)):
    sum_of_cals = 2.0*calories[ii]

print(sum_of_cals)


# In[ ]:


# Write your solution here


# ### &#9989;&nbsp; 2.2.2 Explaining the Problem and the Solution (2 Points)
# 
# In the space below, explain the problem and your solution. You should include the following information:
# 1. The line of code that caused the error(s)
# 2. (Where appropriate) The error code
# 3. A plain english description of the error(s) in the code
# 4. How you solved the error(s)

# *Explain the problem and solution here*

# # 3. Debugging YOUR Code (8 Points)
# 
# For this problem, you will be using two errors that you have encountered in your work--in your pre-class assignments, in-class assignments, or even this homework assignment. **NOTE:** each of your pieces of buggy code should have ***different error codes***. (For example, if your first buggy code has a `TypeError` error code, then your second buggy code must have a *different* error code.)
# 
# ## 3.1 Your Buggy Code 1 (4 Points)
# 
# ### &#9989;&nbsp; 3.1.1 The Buggy Code (1 Points) 
# **Copy over your buggy piece of code. Include a comment at the top indicating which assignment the code came from.**
# 
# 

# In[ ]:


# Put your buggy code here
# INCLUDE A COMMENT HERE INDICATING WHICH ASSIGNMENT THE CODE CAME FROM


# ### &#9989;&nbsp; 3.1.2 Fixing the Code (1 Points)
# **Rewrite the buggy code so that it achieves the task it is supposed to.**

# In[ ]:


# Write your fixed code here


# ### &#9989;&nbsp; 3.1.3 Explaining the Problem and the Solution (2 Points)
# 
# In the space below, explain the problem and your solution. You should include the following information:
# 1. The line of code that caused the error(s)
# 2. (Where appropriate) The error code
# 3. A plain english description of the error(s) in the code
# 4. How you solved the error(s)

# *Explain the problem and solution here*

# ## 3.2 Your Buggy Code 2 (4 Points)
# **Reminder** that your second piece of buggy code must have a ***different error code*** than your first piece of buggy code.
# 
# ### &#9989;&nbsp; 3.2.1 The Buggy Code (1 Points) 
# **Copy your buggy piece of code. Include a comment at the top indicating which assignment the code came from.**

# In[ ]:


# Put your buggy code here
# INCLUDE A COMMENT HERE INDICATING WHICH ASSIGNMENT THE CODE CAME FROM


# ### &#9989;&nbsp; 3.2.2 Fixing the Code (1 Points)
# **Rewrite the buggy code so that it achieves the task it is supposed to.**

# In[ ]:


# Write your fixed code here


# ### &#9989;&nbsp; 3.2.3 Explaining the Problem and the Solution (2 Points)
# 
# In the space below, explain the problem and your solution. You should include the following information:
# 1. The line of code that caused the error(s)
# 2. (Where appropriate) The error code
# 3. A plain english description of the error(s) in the code
# 4. How you solved the error(s)

# *Explain the problem and solution here*

# # 4. Coding A Cash Register
# You work for a company that makes cash registers, and you’ve been tasked with writing a piece of code for printing out receipts. 
# As items are being rung up at checkout, two pieces of information are stored:
# 1. The name of the item
# 2. The cost (per unit) of the item.
# These two pieces of information are stored in separate lists (see the example below).

# In[ ]:


#Example lists
item_names = ["Water Bottle"]
item_per_unit_prices = [22.99]


# ## &#9989;&nbsp; 4.1 Create your Own Test Lists (2 Points)
# Before you begin, it’s best to have some example data for testing your code. Check [Amazon](https://www.amazon.com/), [Target](https://www.target.com/), [Walmart](https://www.walmart.com/), or anywhere else to find three or four items and their prices. Turn them into lists that you can use to test your code. 
# 

# In[ ]:


#Add your lists here


# ## &#9989;&nbsp; 4.2 Calculating Sum (3 Points)
# 
# As a first step, **create a loop that calculates the sum total of the price of each item. Your final code should print out the total cost of all of the items.**

# In[ ]:


#Write your code for calculating sum here


# ## &#9989;&nbsp; 4.3 Printing Names and Cost (4 Points)
# **Now modify your code from the previous part so that it *also* prints the name and price of each item. That is, your code should print out:**
# 
# ***The item name  ,   The cost of the item***
# 
# As well as the sum total at the end.

# In[ ]:


#Write your code for calculating sum AND printing out name and price here


# ## 4.4 Multiple Items
# People will often buy more than one copy of a single item (e.g., two 1 gallon jugs of milk or six copies of Shrek on Blu Ray). Each copy of an item doesn’t get its own line; there’s only one line, and we put how many copies were purchased. This means we need a new piece of information; how many copies were purchased. Let’s put this in a new list.

# In[ ]:


#Example lists
item_names = ["Water Bottle"]
item_copies = [2]
item_per_unit_prices = [22.99]


# ### &#9989;&nbsp; 4.4.1 Create a New Test List (1 Points)
# 
# **Add a new list that includes the number of copies of each item being purchased.**

# In[ ]:


#Add your lists here


# ### &#9989;&nbsp; 4.4.2 Modiyfing Code to Include Copies (5 Points)

# **Modify your code from the previous part, so it takes into account how many copies are purchased. Your final code should print out:**
# 
# ***How many copies were purchased   The item name   The total cost of all copies of this item***
# 
# As well as the sum total at the end.

# In[ ]:


#Write your code for calculating sum AND printing out number of copies, the name, and price here


# ### &#9989;&nbsp; 4.5 Test Your Code (2 Points)
# Below we have provided an example set of lists to test your code and make sure it runs correctly.

# In[ ]:


item_names = ["Water Bottle","Orange Juice","Litebrite","Ceramic Pig Bowl","Crocs","Marine Iguana Plush Toy","Glitter Bunny Ears Throw Pillow","Lil Sloth 100 Piece Animal-Shaped Jigsaw Puzzle","Robot UnicornBot Kit","JoJo Siwa Unicorn LED Nightlight Pink","Antsy Pants Unicorn Lawn Bowling Set"]
item_copies = [2,2,1,2,9,3,15,5,2,12,1]
item_per_unit_prices = [22.99,4.29,12.79,32.4,19.99,21.99,29.99,33.99,99.99,25.15,24.99]


# In[ ]:


#Test your code here


# ---
# ## Assignment Wrap-up
# 
# Please fill out the following Google Form before you submit your assignment. **You must completely fill this out in order to receive credit for the assignment!**
# 
# **COMPLETE THIS SURVEY through [this link](https://forms.office.com/Pages/ResponsePage.aspx?id=MHEXIi9k2UGSEXQjetVofWtNmJF3VV1Ko4OWA1RPCNZUMldQTUc2Tk9WNFBONUxURFhHT0hWTlNFWS4u) or through cell below.**
# 

# In[ ]:


from IPython.display import HTML
HTML(
"""
<iframe 
	src="https://forms.office.com/Pages/ResponsePage.aspx?id=MHEXIi9k2UGSEXQjetVofWtNmJF3VV1Ko4OWA1RPCNZUMldQTUc2Tk9WNFBONUxURFhHT0hWTlNFWS4u" 
	width="80%" 
	height="1200px" 
	frameborder="0" 
	marginheight="0" 
	marginwidth="0">
	Loading...
</iframe>
"""
)


# ---
# 
# ### Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "Homework Assignments" section, find the submission folder link for Homework #1, and upload it there.

# In[ ]:




