#!/usr/bin/env python
# coding: utf-8

# # Day 5 Pre-class Assignment: Boolean logic, if statements, and an introduction to functions

# ### <p style="text-align: right;"> &#9989; Put your name here</p>

# ### Goals for Today's Pre-Class Assignment
# By the end of this assignment, you should be able to:
# * Use if/else statements with true/false (boolean) conditional statements in Python.
# * Write simple functions in Python
# 
# ### Assignment instructions
# 
# Watch any videos below, read all included and linked to content, and complete any assigned programming problems.  Please get started early, and come to office hours if you have any questions and make use of Teams!
# 
# **This assignment is due by 11:59 p.m. the day before class,** and should be uploaded into the appropriate "Pre-class assignments" submission folder.  Submission instructions can be found at the end of the notebook.

# ---
# ## 1. Making decisions in Python
# 
# Sometimes when we're writing a program, we run into a situation where the right next step is contigent on whether or not a particular condition is true or not. If it *is* true, we might want to do one thing, but if it *is not* true, we might want to do something else entirely. This is sometimes referred to as "branching". Basically, conditional statements, where something is evaluated to be `True` or `False`, allow Python to make decisions about how to move forward. When it comes to making decisions in Python, there are two ideas that you need to understand:
# 1. The main command in Python is the `if` statement; or, more generally, the `if-then-else` construct
# 2. Boolean logic (the conditional True/False statement) allows you to perform tests that return `True` or `False`, which you then use to move foward.
# 
# Taken together, these two features of a programming language are essential for getting our codes to carry out complex tasks. These statments generally play a key role in data science as we often need the computer to sift through large data sets depending on what we wish to analyze.
# 
# You should also pause for a moment to reflect on that fact that you're already been exposed to Boolean logic statement when you've written `while` loops. Basically, the `while` loops tells Python to keep doing the same thing until the conditional statement becomes `False`.
# 
# **Now**, to learn more about boolean logic and if statements, watch the video below. <br>
# (If the YouTube video doesn't work, you can access a back-up version on [MediaSpace](https://mediaspace.msu.edu/media/Boolean+logic+and+%27if%27+statements/1_uml9tmi3))

# In[1]:


# Don't forget to watch the video in full-screen mode!
from IPython.display import YouTubeVideo  
YouTubeVideo("cozbOliNwSs",width=640,height=360)  # Boolean logic and if statements


# ---
# ## 2. Practice with `if` statements
# 
# 
# Now that you've learned a bit about `if` statements in Python, let's get some practice with those conditional statements!
# 
# Remember, `if` statements can be used for situations when we only want certain code to execute when a particular thing happens to be true.
# 
# For example, the following code loops over a range of values but only actually prints the value if the value is greater than 5. Try running the code!

# In[2]:


# loop over the values
for i in range(11):
    # If the value is greater than 5, print it
    if i > 5:
        print(i)


# Note that `if` statements can be used with any conditional statement that returns a `True` or `False`. For example, we can also do something like checking to see if a number is evenly divisible by 2. For this, we can use the __`modulus operator`__, which is a represented by a __`%`__ sign in Python. When you use the __`%`__ sign, Python divides the first number by the second number and returns the remainder. Try running the following code.

# In[ ]:


# loop over the values
for i in range(11):
    # If the value is divisible by 2, print it
    if i%2 == 0:
        print(i)


# &#9989;&nbsp; **Question**: What is the above code doing?

# <font size="+3">&#9998;</font> *Put your answer here*

# ### Using `and` and `or`:
# 
# We can also perform `if` statements using multiple conditions. Let's say we want all the numbers in the range from 0 to 10 that are greater than 5 **and** divisible by 2. How might we do that? Review and run the code below. Make sure you understand what's happening.

# In[ ]:


for i in range(11):
    # If the value is greater than 5 and divisible by two, print it
    # Notice that the word "and" is bold and in green, this means it serves a special purpose in Python
    if i > 5 and i%2 == 0:
        print(i)


# Now, what if we replace that `and` statement with an `or` statement? Try running the code!

# In[ ]:


for i in range(11):
    # If the value is greater than five or divisible by 2, print it
    # Notice that the word "or" is also bold and in green
    if i > 5 or i%2==0:
        print(i)


# &#9989;&nbsp; **Question**: How is the `or` statement different than the `and` statement?

# <font size="+3">&#9998;</font> *Put your answer here*

# &#9989;&nbsp; **Task:** Define `x` to be a list of the numbers 1 through 10. Create loop that goes through all the numbers in `x` and, if that number is even, use a print statment to print "This number is even:" followed by the number. Put your solution in the code cell below.

# In[ ]:


# Put your code here


# ### Inside the block vs. outside the block:
# 
# Remember that the number of spaces (or "indentation") before a given line of code determine which "block" it is in.  This is very important with `if` statements and can be especially confusing when nesting `if` statements and loops. 

# **The code below tries to compute the sum of all the numbers from 1 to 10 that are larger than 6.**  Review the code, and try to predict the output before running it.

# In[ ]:


# initializing the list
greater_than_6_list = []

for i in range(11):
    print("i equals",i)
    if i > 6:
        print("i is greater than 6")
    # appending the number that is greater than 6
    greater_than_6_list.append(i)

print("List of numbers to sum:",greater_than_6_list)
print("Sum of numbers is equal to:",sum(greater_than_6_list))
        


# &#9989;&nbsp; **Question**: What went wrong in the code above?

# <font size="+3">&#9998;</font> *Put your answer here*

# &#9989;&nbsp; **Task:** Copy the above code to the cell below and fix it to correctly compute the sum of the numbers greater than 6.

# In[ ]:


# Put your code here


# ---
# ## 3. More complex `if` statements
# 
# Sometimes just using several simple `if` statements in our code isn't enough to make sure the program does what it is supposed to do. Other times even more complicated `if` statements that use `and` or `or` to combine multiple conditional statements aren't sufficent either, so what do we do then?
# 
# You may often discover that you need to solve a problem that requires the code to do one thing if a particular condition is true and *something else* if that condition is not true. This is where the `else` command comes into play. Basically, the program knows to execute a certain piece of code when the `if` statement is true and a different piece of code for all other cases.
# 
# We can actually build even more complicated code by using the `elif` or "else-if" statement, which is basically a second `if` statement that is only executed if the first `if` statement was not satisfied. We can even tag an `else` on the end of all of that as well. Below is a diagram that helps illustrate the flow of an `if-elif-else` statement.
# 
# ![If_Flow](https://cdn.programiz.com/sites/tutorial2program/files/Python_if_elif_else_statement.jpg)
# 
# **Now**, watch the following video to get a sense for how all of these statements work together. The video starts out with some simple examples and then builds a progressively more complex bit of code that uses a combination of an `if` statement, a few `elif` statements, and a final `else` statement. <br>
# (If the YouTube video doesn't work, you can access a back-up version on [MediaSpace](https://mediaspace.msu.edu/media/Complex+%27if%27+statements/1_5lxv404t))

# In[3]:


# Don't forget to watch the video in full-screen mode!
from IPython.display import YouTubeVideo  
YouTubeVideo("8_wSb927nH0",width=640,height=360)  # Complex if statements


# &#9989;&nbsp; **Question**: Let's say that you were recently promoted to manager at work. While you're excited about all of the extra money that comes with the new position, you've started to realize that there's a bunch of extra responsbility associated with the job as well. One of those responsibilities is to create the work schedule based on all of the preferences of your new ~~minions~~ employees. You're thinking that you might be able to use a bit of Python to figure out which hours each person should work. Your employees have made the following requests:
# 
# * Luke would like to work in the morning
# * Ningyu would like to work in the evening
# * Nate didn't submit his request
# * Justin would like to work in the evening
# * Katrina would like to work in the evening
# * Jacob would like to work in the morning
# 
# Create a `for` loop that loops through the list of employee names (provided below) and prints out the following statements based on their preferences:
# 
# * If the employee requested mornings, print "You have to work from 9am-12pm."
# * If the employee requested evenings, print "You have to work from 6-9pm."
# * If the employee failed to submit a request, print "You have to work from 12-6pm."
# 
# You can use any combination of `if`, `elif`, and `else` statements to get the job done.

# In[ ]:


employees = ['Luke', 'Ningyu', 'Nate', 'Justin', 'Katrina', 'Jacob']

# Put your code below this comment


# ___
# ## 4 Introduction to functions
# 
# The last bit of this assignment is designed to get you start thinking about an extremely useful tool in Python, the Python **function** construct!
# 
# Functions in Python are really handy when you have a bit of code that serves a specific purpose and you want to be able to use that bit of code over and over again without having to copy and paste it repeatedly. It also means that if you need to change how that code works, you can change the code inside the function and you don't have to change that code in several different places. Functions can also make your code much easier to read because you can compartmentalize your code into separate functions and then just call those function in the main body of your code.

# ### 4.1 What are functions and why would we use them?
# 
# Watch the following video for an overview of what functions are and why they can be **extremely useful!** <br>
# (If the YouTube video doesn't work, you can access a back-up version on [MediaSpace](https://mediaspace.msu.edu/media/Introduction+to+Functions+in+Python/1_gn36jgpc))

# In[4]:


# Don't forget to watch the video in full-screen mode!
from IPython.display import YouTubeVideo
YouTubeVideo("kY3yMXUu5qY",width=640,height=360) # Intro to Functions!


# &#9989;&nbsp; **Question**: In your own words, explain what a function is and why it is a very useful tool in programming?

# <font size="+3">&#9998;</font> *Put your answer here!*

# &#9989;&nbsp; **Question**: What are the three main things that functions provide?

# <font size="+3">&#9998;</font> *Put your answer here!*

# ### 4.2 How do we write functions in Python?
# 
# Watch the following video, to learn how functions are written in Python.<br>
# (If the YouTube video doesn't work, you can access a back-up version on [MediaSpace](https://mediaspace.msu.edu/media/How+to+write+functions+in+Python/1_seuv967w))

# In[5]:


# Don't forget to watch the video in full-screen mode!
from IPython.display import YouTubeVideo
YouTubeVideo("HWzDv1UHLZo",width=640,height=360) # How do we write functions?


# &#9989;&nbsp; **Question**: What are the four main pieces that make up a function in Python?

# <font size="+3">&#9998;</font> *Put your answer here!*

# &#9989;&nbsp; **Question**: What is the critical term needed to initially define a function?

# <font size="+3">&#9998;</font> *Put your answer here!*

# &#9989;&nbsp; **Question**: How do you ensure that the results of your function are output in a way that will allow you to store the results in a new variable?

# <font size="+3">&#9998;</font> *Put your answer here!*

# ### 4.3 Practice with writing functions
# 
# Watch the following video to review how you can write functions in Python. Pay attention to the different ways that you can output information from functions and input variables into functions.<br>
# (If the YouTube video doesn't work, you can access a back-up version on [MediaSpace](https://mediaspace.msu.edu/media/Practice+with+Functions+in+Python/1_9049fdj1))

# In[6]:


# Don't forget to watch the video in full-screen mode!
from IPython.display import YouTubeVideo
YouTubeVideo("EXO3WYqlA6A",width=640,height=360) # Practice writing functions


# &#9989;&nbsp; **Question**: Create (using _def_) a function that **returns** the length of a hypotenuse ($h$) given the lengths of the other two sides ($a$ and $b$). Remember that $h = \sqrt{a^2 + b^2}$. Name your function to be "`get_h`". 

# Note that the square root of `a` can be computed using `a**(1/2)`.

# In[ ]:


a = 4
b = a**(1/2)
print("The square root of",a,"is",b)


# In[ ]:


#Put your code here


# Run the function that you just created ("`get_h`"), and test to make sure it works in the cell below. 
# 
# Since the function __returns__ the result (instead of _printing_ the result), you need to create a new variable to store the value returned by your function. And then print out the value of this new variable to see whether it is what you expected. 
# 
# For example, if you provide the values as _a=3_ and _b=4_, the value returned by your function should be 5.0.

# In[ ]:


#Put your code here


# ## 4.4 Variable Scope
# 
# When writing functions (or any Python code really), we have another important consideration we have not talked about yet commonly called [**Variable Scope**](https://www.w3schools.com/python/python_scope.asp). **Variable Scope** refers to where and when variables can be accessed. A variable can only be accessed in the region it is created. For example, if you type `a = 1` in one Jupyter notebook and then `print(a)` in another notebook, the print statement will throw an error.
# 
# When writing functions, the goal is for them to reusable (meaning you can use them in other notebooks), so you must ensure that the function has everything it needs to execute the function call. Any variables that the function will use should be defined as input arguments, and any variables you want to access after running the function must be returned (and saved in your notebook as a new variable!). 
# 
# When you define a function in your notebook and run the cell, it is now loaded into your Jupyter notebook and can be called in any cell. It will remain defined in your notebook until you restart your Kernel or close the file. When you save the output or call the function, use unique variable names rather than overwriting previous variables. This will help your code be more clear and avoid hard-to-find bugs!
# 
# The questions below will help you explore what variable scope looks like in a Jupyter notebook.
# 
# ---

# &#9989;&nbsp; **Question**: In the cell below, we have definde three variables, `favorite_animal`, `favorite_food`, and `favorite_season`. Write a `print()` statement that prints out those three variables.

# In[ ]:


favorite_animal = 'otter'
favorite_food = 'spaghetti carbonara'
favorite_season = 'Fall'

# put your code here


# &#9989;&nbsp; **Question**: In the cell below, we have redefined the values of `favorite_animal`, `favorite_food`, and `favorite_season`. 
# 
# **Before you run this cell**, copy and paste your print statement above into the first line of the cell and the last line of the cell. What do you notice about the output? 

# In[ ]:


# put your print statement here

favorite_animal = 'elephant'
favorite_food = 'Chicken Parmesan'
favorite_season = 'Spring'

# put your print statement here too!


# &#9989;&nbsp; **Question**: In the cell below, you will see some code written but perhaps a little bit confusingly. Briefly describe what you see as potentially confusing about the code.

# In[ ]:


## What makes the code below a little confusing?

favorite_animal = 'elephant'
favorite_food = 'Chicken Parmesan'
favorite_season = 'Spring'

def my_favorite_things(favorite_animal = "penguin",favorite_food = "Spaghetti and Meatballs",favorite_season = "Winter"):
    string_of_favorites = "My favorite things are: " + favorite_animal + ', ' + favorite_season + ', and ' + favorite_food + "."
    return string_of_favorites

print(my_favorite_things())
print(my_favorite_things(favorite_animal, favorite_food, favorite_season))
print(my_favorite_things(favorite_food=favorite_food))


# <font size="+3">&#9998;</font> *Put your answer here!*

# &#9989;&nbsp; **Question**: In the cell below, there is a print statement that is throwing an error. Why is it throwing an error?

# In[ ]:


## Why does the code below throw an error message?

print(string_of_favorites)


# <font size="+3">&#9998;</font> *Put your answer here!*

# **For more information on defining functions in python, check out these links:**
# * [Tutorial on functions in python](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
# * [More function basics with executable examples](http://www.diveintopython3.net/your-first-python-program.html#declaringfunctions)
# 
# **Important**: One of the things you should remember is that when you want a function to return a values (rather than just print it), the `return` command needs to go at the end of the function. The moment a function comes across a `return` statement, it will exit the function and ignore any code that comes later in the function.

# ---
# ## Follow-up Questions
# 
# Copy and paste the following questions into the appropriate box in the assignment survey include below and answer them there. (Note: You'll have to fill out the section number and the assignment number and go to the "NEXT" section of the survey to paste in these questions.)
# 
# 1. In your own words, what is the propose of conditional statements (e.g. `if`/`elif`/`else`) when writing code?
# 
# 2. In your own words, what makes functions a useful programming concept/tool?
# 
# 3. In your own words, how would you define "variable scope"?

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

# &#169; Copyright 2023,  Michigan State University Board of Trustees
