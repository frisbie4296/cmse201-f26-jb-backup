#!/usr/bin/env python
# coding: utf-8

# # Day 3 In-class Assignment: The power of compound interest
# <img src="https://g.foolcdn.com/image/?url=https%3A//g.foolcdn.com/editorial/images/463624/retirement-savings-jar-full-of-coins-and-alarm-clock.jpg&w=2000&op=resize" width=400px>
# 

# ### <p style="text-align: right;"> &#9989; Put your name here.
# <p style="text-align: right;"> &#9989; Put your group member names here.

# ## Learning Goals:
# 
# By the end of this assignment you should be able to:
# 
# * Use Python lists to store values
# * Use loops to iterate over a specified range or until a condition is met.
# * Compute the best retirement savings plan.
# 

# ---
# ## The Problem
# 
# You are working for a bank, writing code to calculate the revenue and expenses for the company. A person can deposit money in a retirement account at your bank, and the bank pays interest every year on the money in the retirement account. The mathematical expression for calculating the amount of money in the retirement account every year is:
# 
# $\mathrm{New~Retirement~Total} = (\mathrm{Old~Retirement~Total}) + [(\mathrm{Old~Retirement~Total})*(\mathrm{Interest~Rate})] + (\mathrm{Money~Added~to~Retirement})$
# 
# Or, if we simplify this a bit, we can re-write it as:
# 
# $\mathrm{New~Retirement~Total} = [(\mathrm{Old~Retirement~Total})*(\mathrm{1 + Interest~Rate})] + (\mathrm{Money~Added~to~Retirement})$
# 
# **Your job is to write a piece of code that calculates and stores (in a list) the total amount of money in the retirement account *every year* for some number of years** (your boss is going to make a plot of it, so make sure you have the value for each year!). 
# 
# Your boss tells you to model the total retirement savings for a ***range*** of different parameters (*e.g.* interest rates and annual contributions).
# 
# **You can assume that the person saving for retirement starts when they're 18 and continues until they're 65. Also assume that the interest rate and annual contributions are fixed.**

# ---
# ## 1. Planning your solution and pseudo-coding
# 
# Before you start writing any code you should come up with a plan for how you've going to solve the problem. During this phase you should identify and define the variables that are revelant to the problem, the equations you're going to need to model, the overall structure of the program that you will write, and how you will make sure the code is running correctly.
# 
# #### You and your group members are expected to use the white board at your table (or a virtual whiteboard app like [Google Jamboard](https://jamboard.google.com/) or the [Aww app](https://awwapp.com/)) to write out your ideas to ensure that everyone is on the same page and allow your instructors to see your progress.
# 
# Part of this planning process should involve writing "**pseudo-code**", a plain language description of the steps in your code (sort of like writing out in your code in form of a cooking recipe). **You actually already did a version of this on Day 1 when you and your group came up with an _algorithm_ for sorting people by their birthday.**
# 
# As a reminder, **an algorithm is**: a procedure for solving a problem in terms of the actions to be executed and the order in which those actions are to be executed. In other words, an algorithm is merely the sequence of steps taken to solve a problem. [[source](https://www.unf.edu/~broggio/cop2221/2221pseu.htm) of this definition]
# 
# You can see some examples of pseudocode [here](https://www.unf.edu/~broggio/cop2221/2221pseu.htm) and [here](https://www.geeksforgeeks.org/how-to-write-a-pseudo-code/).
# 
# Things you should decide on during your planning and psuedo-coding:
# 
# 1. What quantities in your model are "variables" that will change as a function of time? What are the initial values of these variables?
# 2. What quantities in your model are "parameters" that are constant over time? What are reasonable ranges for each parameter? 
# 4. How will you go about solving this problem for a given set of inputs?
# 5. How will you check to make sure your code is running correctly. 
# 
# 
# You should be able to justify your choices.
# 
# ### &#9989;&nbsp; 1.1 Record the details of you plan in the Markdown cell below.

# <font size=6 color="#009600">&#9998;</font> *Put your plan details here!* 

# ## &#128721; STOP AND ASK YOUR INSTRUCTOR TO COME OVER AND CHECK YOUR PSEUDOCODE
# 
# ---
# ## 2. Coding up your solution
# 
# Now that you and your group have come up with a plan for your code, it's time to put your plan into action.
# 
# ### &#9989;&nbsp; 2.1 Writing Code
# **Write your code for calculating the total retirement savings in the cell below. Start by writing code for a single set of parameter values (i.e., not a range).** It is simpler, and you can also add to it later.
# 
# **Hint: Remember to update the value of $\mathrm{Old~Retirement~Total}$ in your loop!**

# In[ ]:


# Put your code for calculating the total amount of retirement savings here


# ---
# ### &#128721; STOP
# 
# **Check to make sure your code is working correctly.**

# In[ ]:


# If your method for checking your results involves writing code, put it here


# *Explain how you know your code is working correctly.*

# <font size=6 color="#009600">&#9998;</font> *Put your explanation here!* 

# ## 3. Coding up your solution (Range of Values)
# 
# ### &#9989;&nbsp; 3.1 Putting in a Range of Values
# **Take the code you wrote in Part 2 and expand on it so that you can calculate total retirement savings for a range of different input parameters.** To start, try 3 different annual contribution values and 4 different interests rates, but try to write your code so that you could easily do greater or fewer numbers of values for both parameters.
# 
# **Note:** To explore a range of input parameters, you may want to use a "nested" loop (a loop inside a loop). Look back at the pre-class assignment for an example!

# In[ ]:


# Put your code for calculating the total amount of retirement savings for a range of values here


# ## 4. Bringing in new customers
# 
# Your boss says the bank is trying to attract customers that don't start saving for retirement until later in life, and they're trying to find a good way to do this. You suggest offering **double the usual interest rate** for people that don't start saving until they're 30. 
# 
# Your boss likes the idea and wants you to run the numbers. 
# 
# ### &#9989;&nbsp; 4.1 Answering your Boss' Question, Code
# **Who would end up with more money saved: someone that starts saving at 18 with a normal interest rate, or someone that starts saving at 30 with double the interest rate?**

# In[ ]:


# Put your code here


# ### &#9989;&nbsp; 4.2 Answering your Boss' Question, Answer
# 
# **Who would end up saving more money for retirement?**

# *Write your answer here*

# ---
# ## Assignment wrap-up
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


# ## Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "In-class assignments" folder, find the appropriate submission link, and upload it there.
# 
# See you next class!

# &#169; Copyright 2023,  Department of Computational Mathematics, Science and Engineering at Michigan State University.
