#!/usr/bin/env python
# coding: utf-8

# # Day 4 In-class Assignment: Academic Integrity and Coding Best Practices
# ![data_cycle.png](attachment:data_cycle.png)

# ### <p style="text-align: right;"> &#9989; Put your name here.
# <p style="text-align: right;"> &#9989; Put your group member names here.

# ## Learning Goals:
# 
# By the end of this assignment you should be able to:
# 
# * Describe your personal commitment to academic integrity 
# * Search on google for snippets of code and compose solutions with integrity
# * Construct variable names following best coding practices
# 

# ---
# ## Part 1: Craft Your Personal Academic Integrity Statement
# 
# As you reviewed in your pre-class assignment, The Spartan Code of Honor Academic Pledge was adopted by the [Associated Students
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

# &#9989;&nbsp; **1.1 Activity**: Work with the members of your group to craft a personal statement of commitment to academic honesty.  As part of this statement, address the following components:
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

# ---
# ## Part 2: Practice searching for snippets of code and constructing your own code
# 
# As stated in the pre-class, we want you to learn how to use the internet as a resource in your coding.  In general, you should practice taking problems and breaking them into sub-problems.  Searching on the internet for solutions to sub-problems is an important skill.
# 
# When you find helpful code from peers or the internet, you should write this code in your words.  Specifically:
# 1. Rename all variables using variable names that make sense **to you**.
# 2. Use your own structure (i.e. order the code in a way that makes the most sense **to you**)
# 3. Add comments to help clarify complicated syntax
# 4. If you received substantive value from another source (for example, complicated syntax or > 5 lines of content), cite the source (Author, URL, and Date Accessed)

# &#9989;&nbsp; **2.1 Question:** Find the sum of all odd numbers from 1 to 301.
# 
# **Remember**, do not place this exact question into google.  We do not want you to find the whole solution to a whole problem because a) **you will not learn how to code on your own**, b) you may feel tempted to plagiarize someone else's complete work, and c) you likely will waste time because the answer for this specific problem is not out there.
# 
# Instead, break this into smaller problems and search for those.
# Potential google search phrases:
# 
# [`python make list of odd numbers`](https://www.google.com/search?q=python+make+list+of+odd+numbers)
# 
# `python loop through odd numbers`
# 
# `python sum of list`
# 
# Notice that when searching for ways to accomplish this task using Python, it is important to include "python" in your search phrase!
# 
# **Talk with your group about other useful search phrases and share the resources you locate!**
# 

# In[ ]:


# Put your code here
# Remember, if you use a source, 
# 1) Rename the variables, 
# 2) Use your own structure, 
# 3) Add comments to help clarify complicated syntax
# 4) Cite the source if it provides substanative value



# &#9989;&nbsp; **2.2 Question**: Construct a list of items and quantities for a grocery list.  Using the following two lists that have been provided, make a new list that contains all string-type variables such that the value at each index `i` in the new list should be the concatenation of the values for index `i` from `list1` and `list2`.  When complete, the final list should be
# 
# `['apples_5', 'oranges_2', 'bananas_4', 'kiwi_1', 'rambutan_10']`

# In[ ]:


list1 = ['apples','oranges','bananas','kiwi','rambutan']
list2 = [5,2,4,1,10]

# Put your code here


# ---
# ## Part 3: Python Coding Conventions
# 
# *Code is read much more often than it is written.*
# <sub>~Guido van Rossum, Author of PEP8</sub>
# 
# There are several proposed Python Enhancement Proposals (PEP), with the goal to improve the readability and consistency of Python code.  [PEP 8 is a document that provides guidelines and best practices on how to write Python code](https://www.python.org/dev/peps/pep-0008/).  In your studies and career, you may spend a few minutes, or a whole day, writing a piece of code. Once it is written, you will likely not need to write it again, but you *will* likely need to read it.  And, others will need to read it and understand what you have written.  **Readability matters**, motivating the effort to write code following certain consistency rules.  
# 
# There are numerous conventions for Python coding.  For now, we do not want to bog you down with all the details.  For now, we will focus on best practices for *naming* data types (variables, functions,etc) and for *commenting* code.
# 
# **Name Conventions**
# 
# Choosing sensible names will save you time and energy later.  The best way to name your objects in Python is to use descriptive names to make it clear what the object represents. 
# 
# | Type 	| PEP8 Naming Convention 	| Examples |
# | :------- |:--------|:------|
# |Variable |	Use a lowercase single letter, word, or words. Separate words with underscores to improve readability. 	| length_inches, list_groceries, my_variable |
# |Function |	Use a lowercase word or words. Separate words by underscores to improve readability.| 	multiple_by_three, my_function|
# 
# **Tips**:
# - Never use spaces in your names (use underscores instead so that each name is a string of characters)
# - Avoid single character names unless it is clear what it means (ex: `growth_rate` is preferred to `g`)
# - If variable contains a value with units, include units in the name (ex: `weight_kg`, `height_ft`)
# - Avoid capitalizing variable and function names (capitals will be used for naming classes/constants/others objects, that come later)
# 
# **Comment Conventions**
# 
# Especially when learning to code, **feel free to use comments often!**  This will help you understand your code and make it easier for you to review later.  If you are tasked with a challenging task, use a comment block at the beginning to describe in your own words the goal of your code.  
# 
# For more information on the PEP8 Python Style Guide, visit [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/)

# ---
# The following examples will give you practice building from snippets of code and chosing quality variable names.
# 
# &#9989;&nbsp; **3.1 Question:** Write a loop that prints the first 20 elements of the Fibonacci sequence.
# 
# You look online and find the following snippet of code on https://www.programiz.com/python-programming/examples/fibonacci-sequence:
# ```
# ----------------
# n1, n2 = 0, 1
# COUNT = 0
# Elem = 20
# 
# print("Fibonacci sequence:")
# while COUNT < Elem:
#     print(n1)
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     COUNT += 1
#     
# ----------------
# 
# ```
#     
# Using this code as a base, write your own code **that follows the best practices that have been described above.**

# In[ ]:


# Put your code here.

# First cite source material
# Answer based on: https://www.programiz.com/python-programming/examples/fibonacci-sequence, Accessed 8/18/20



# &#9989;&nbsp; **3.2 Question:** Make a list with the 5th through 10th number of the Fibonacci sequence.  Print the contents of the list to provide an output that matches:
# ```
# The 5 th element of the Fibonacci sequence is 3
# The 6 th element of the Fibonacci sequence is 5
# The 7 th element of the Fibonacci sequence is 8
# The 8 th element of the Fibonacci sequence is 13
# The 9 th element of the Fibonacci sequence is 21
# The 10 th element of the Fibonacci sequence is 34
# ```

# In[ ]:


# Put your code here.

# First cite source material
# Answer based on: https://www.programiz.com/python-programming/examples/fibonacci-sequence, Accessed 8/18/20



# &#9989;&nbsp; **3.3 Question:** Go back to the code that you wrote in part 2 of this notebook.  Add comments and adjust the variable names to ensure they follow best practices.  
# 

# ---
# ##  Part 4: Experimenting with Python dictionaries (time permitting)
# 
# One of the goals of CMSE 201 is for you to develop the skills necessary to learn new Python techniques on the fly by reading pieces of code and searching google for useful information when necessary -- let's give that a shot!
# 
# Hopefully you're starting to feel comfortable with Python lists at this point, but this isn't the only tool available for storing information in Python. Another useful Python object for storing information is called a "dictionary". Rather than using integer numbers as the indices for accessing the information contained within the dictionary, a Python dictionary uses words, called **"keys"**, to access the information.
# 
# Take a look at the code below. This code creates a simple dictionary that stores information about CMSE 201 this semester and then prints out a bit of information about the course.

# In[ ]:


# Create a dictionary to store information about CMSE 201
course = {"course_title": "Computational Modeling and Data Analysis I",
           "course_code": "CMSE",
           "course_number": 201,
           "section_numbers": [1, 2, 3, 4, 5, 6, 7, 8],
           "instructors": ['Finzell', 'Law-Kam Cio', 'Law-Kam Cio', 'Fang', 'Cheng', 'Frisbie', 'Karimian', 'Frisbie']}

# print some information about the course
print('The instructors for '+course['course_code']+str(course['course_number'])+' are:\n')
for name in course['instructors']:
    print(name)
            


# &#9989;&nbsp; **Review** the above code and talk with your group to ensure that you understand what the code is doing. In a new Markdown cell below this one, **write down everything you notice about how a Python dictionary is created when compared to a Python list and how information stored in the dictionary is accessed.** Also comment on anything else you noticed about the code that you find interesting or new to you.

# &#9989;&nbsp; **Practice** creating your own python dictionary. In a new code cell, **create a Python dictionary that stores a bit of information about yourself**:
# 
# * Your name as a **string**
# * Your major as a **string**
# * The year that your favorite song, movie, or book was first released or published as an **integer**
# * The courses you're currently taking this semester as a **list**
# 
# Once you've created the dictionary, try printing out some of the information from the dictionary to make sure you set it up correctly.

# ---
# ### &#128721; STOP
# Check in with an instructor before you leave class!
# 
# 

# ---
# ## Assignment wrapup
# 
# Please fill out the form that appears when you run the code below. **You must completely fill this out in order to receive credit for the assignment!** 

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
# 
# ## Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "In-class assignments" folder, find the appropriate submission link, and upload it there.
# 
# See you next class!

# Copyright &#169; 2021, [Department of Computational Mathematics, Science and Engineering](https://cmse.msu.edu/) at Michigan State University, All rights reserved.

# In[ ]:




