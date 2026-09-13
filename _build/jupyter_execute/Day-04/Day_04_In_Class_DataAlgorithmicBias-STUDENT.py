#!/usr/bin/env python
# coding: utf-8

# # Day 4 In-class Assignment: Data and Algorithmic Bias, Academic Integrity, and Coding Best Practices
# 

# ### <p style="text-align: right;"> &#9989; Put your name here.
# <p style="text-align: right;"> &#9989; Put your group member names here.

# ## Learning Goals:
# 
# By the end of this assignment you should be able to:
# 
# * Identify how bias occurs in data and algorithms
# * Understand the impact data and algorithmic bias has on people
# * Apply practices to look for bias in your work and others, and minimize it
# * Search on google for snippets of code and compose solutions with integrity
# * Construct variable names following best coding practices
# 

# # Part 1: Discussing Data and Algorithmic Bias

# In the Pre-class you explored the concepts of Data and Algorithmic Bias by watching videos and reading an article.
# 
# &#9989;&nbsp; **Activity**:
# 
# Go around the group and take **about 2 minutes per person** for each person to summarize their thoughts/reflections from the pre-class assignment. Record the results of your group discussion below. **Make sure to include any observations made by your classmates that perhaps you didn't think about when you did the pre-class assignment**.

# <font size="+3">&#9998;</font> *Write your response here*

# &#9989;&nbsp; **Activity**:
# 
# Below there are several short articles that discuss examples of data or algorithmic bias. 
# 
# Each group member should choose a different article. 
# 
# Take **10-15 minutes** to read your article and prepare answers to the questions below. 
# 
# Then, take **1-2 minutes** each to share your answers to the questions with your group members.

# ## Examples here:
# 
# * [Amazon hiring Algorithm bias](https://www.theguardian.com/technology/2018/oct/10/amazon-hiring-ai-gender-bias-recruiting-engine)
# * [Health Care risk algorithm bias](https://www.scientificamerican.com/article/racial-bias-found-in-a-major-health-care-risk-algorithm/)
# * [Twitter Chatbot turning racist](https://spectrum.ieee.org/in-2016-microsofts-racist-chatbot-revealed-the-dangers-of-online-conversation)
# * [Predictive Policing](https://www.latimes.com/california/story/2022-07-04/researchers-use-ai-to-predict-crime-biased-policing)
# * [Health Insurance Premium Increases](https://www.propublica.org/article/health-insurers-are-vacuuming-up-details-about-you-and-it-could-raise-your-rates)
# * [How Uber Profits While Its Drivers Aren't Earning Money](https://www.vice.com/en/article/wnxd84/how-uber-profits-even-while-its-drivers-arent-earning-money)

# ## Questions for Discussion:
# 
# * How is data being used?
# * How does the actual usage of data relate to its intended usage?
# * Who owns and/or controls the data?
# * Who benefits from the data usage?
# * How is the data usage related to bias?

# <font size="+3">&#9998;</font> *Write your response here*

# ---
# ## Part 2: Practice searching for snippets of code and constructing your own code
# 
# As stated in the pre-class, we want you to learn how to use the internet as a resource in your coding.  In general, you should practice taking problems and breaking them into sub-problems.  Searching on the internet for solutions to sub-problems is an important skill. **It is also important to make sure that you do not take credit for someone else's work as your own.**
# 
# When you find helpful code from peers or the internet, you should write this code in your words and, when appropriate, indicate where your original code originated from.  Specifically:
# 1. Rename all variables using variable names that make sense **to you**.
# 2. Use your own structure (i.e. order the code in a way that makes the most sense **to you**)
# 3. Add comments to help clarify complicated syntax
# 4. If you received substantive value from another source (for example, complicated syntax or > 5 lines of content), cite the source (Author, URL, and Date Accessed)

# &#9989;&nbsp; **2.1 Question**: Construct a list of items and quantities for a grocery list.  Using the following two lists that have been provided, make a new list that contains all string-type variables such that the value at each index `i` in the new list should be the concatenation of the values for index `i` from `list1` and `list2`.  When complete, the final list should be
# 
# `['apples_5', 'oranges_2', 'bananas_4', 'kiwi_1', 'rambutan_10']`
# 
# **Remember**, do not place this exact question into google.  We do not want you to find the whole solution to a whole problem because a) **you will not learn how to code on your own**, b) you may feel tempted to plagiarize someone else's complete work, and c) you likely will waste time because the answer for this specific problem is not out there.
# 
# Instead, break this into smaller problems and search for those.
# Potential google search phrases:
# 
# [`python construct a list`](https://www.google.com/search?q=python+construct+a+list)
# 
# `python loop through a list`
# 
# `python concatenate values`
# 
# Notice that when searching for ways to accomplish this task using Python, it is important to include "python" in your search phrase!
# 
# **Talk with your group about other useful search phrases and share the resources you locate!**

# In[ ]:


# Remember, if you use a source, 
# 1) Rename the variables, 
# 2) Use your own structure, 
# 3) Add comments to help clarify complicated syntax
# 4) Cite the source if it provides substanative value




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

# In[1]:


# Create a dictionary to store information about CMSE 201
course = {"course_title": "Computational Modeling and Data Analysis I",
           "course_code": "CMSE",
           "course_number": 201,
           "section_numbers": [1,2,3,4,5,6,7],
           "instructors": ['Wang','Zhang','Bao', 'Chitwood', 'Bao','Frisbie','LaRose']}

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

# Copyright &#169; 2023, [Department of Computational Mathematics, Science and Engineering](https://cmse.msu.edu/) at Michigan State University, All rights reserved.
