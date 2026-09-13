#!/usr/bin/env python
# coding: utf-8

# # Day 5 In-class Assignment: Savings for Everyone
# ![Snowballs](https://www.palmettocitizens.org/images/personal-savings3.jpg)

# ### <p style="text-align: right;"> &#9989; Put your name here.
# <p style="text-align: right;"> &#9989; Put your group member names here.

# ## Learning Goals:
# 
# By the end of this assignment you should be able to:
# 
# * Review code that uses `if`, `elif`, and `else` statments and understand the logical flow of the program
# * Write `if`/`elif`/`else` statements in Python.
# * Create and use basic functions in Python.
# 

# ---
# ## Part 1: Understanding `if` statements in Python
# 
# As you saw in the pre-class assignment, `if` statements provide an mechanism for "**branching**" to occur in your code. Depending on whether or not something is determined to be true, your code can pursue one branch, or another, or do nothing at all. The `else` statement allows your code to execute *something* even if none of the `if` or `elif` statements you write are found to be true. By combining these sorts of commands in a variety of ways we can create a very complex system of branches in our code.
# 
# &#9989;&nbsp; **As a group, review and run** the following bit of example code.
# 
# &#9989;&nbsp; **As a group, add comments** to explain what various parts of the code are doing. 

# In[ ]:


some_numbers = [2, -5, 16, 17, -6, 23, 0]

for i in range(len(some_numbers)):
    number = float(some_numbers[i])
    if number < 0:
        print('Square root is not real.')
    else:
        print('Square root of',number,'is',number**(1/2))
        
for number in some_numbers:
    if number > 0:
        print(number,'is positive.')
    elif number < 0:
        print(number,'is negative.')
    else:
        print('The number is zero.')


# &#9989;&nbsp; **Question**: What does `float(some_numbers[i])` do?

# <font size="+3">&#9998;</font> *Put your answer here*

# &#9989;&nbsp; **Question**: What does the `len()` function do?

# <font size="+3">&#9998;</font> *Put your answer here*

# &#9989;&nbsp; **Question**: What does the `range()` function do?

# <font size="+3">&#9998;</font> *Put your answer here*

# ---
# ## Part 2: Writing your own `if` statements
# 
# Sometimes in computational modeling and data science, you need to be able parse a set of numbers or data and execute particular tasks based on the how those numbers compare to each other. Conditional statements that use things like `<`, `>`, `>=`, or `==` combined with logical operators like `and` and `or` provide an excellent mechanism for comparing values! Try the following:
# 
# &#9989;&nbsp; **Write a program** that compares three variables v1, v2, and v3 (initial values are provide below) and does the following using `if` statements:
# 
# 1. If v1 is equal to v2, print "woohoo!"
# 2. If v1 is the smallest value of the three (i.e., v1 is less than both v2 and v3), print out "v1 is tiny!"
# 3. If v1 is the smallest value of the three, add a nested if statement to print out a statement saying whether v2 or v3 is the largest value.
# 
# Try several values of v1, v2 and v3 and ensure that you see the correct behavior. 
# 
# **Suggestion**: Make sure you work together with your group to solve this. **Planning it out on the whiteboard can also be useful!**
# 
# **Note**: Although you learned briefly about functions in your pre-class assignment, don't worry about using functions just yet!

# In[ ]:


# Put your code here. Initial values for v1, v2, and v3 are provided.
# Make sure to test out new values to ensure your code works as intended!

v1 = 1
v2 = 4
v3 = 3


# &#9989;&nbsp; **Question**: What happens in your code if either v2 or v3 is less than v1? If you're not sure, **test it out with a bit of code**, you can't (really) break things by experimenting!

# <font size="+3">&#9998;</font> *Put your answer here*

# ---
# ## Part 3: Continued Investment
# 
# You're back at your bank job, calculating the total amount of money people save in their retirement accounts. Previously, your boss asked you to calculate the different amount of money people would save if there was one interest rate for people that started saving early (under 30) and another interest rate (twice the original interest rate) if they started saving later (30 or older). 
# 
# Your boss used your calculations to justify to *their* boss that offering a "better interest rate for older investors" was a good marketing strategy. Your boss's boss accepted the plan with one modification. Rather than give people over 30 double the interest rates, the interest rates would be structured in the following way:
# - People that start to save when they are between **18-24 years old** will receive an interest rate of **6.5%**
# - People that start to save when they are between **25-31 years old** will receive an interest rate of **8.5%**
# - People that start to save when they are between **32-39 years old** will receive an interest rate of **11.0%**
# - People that start to save when they are **40 years or older** will receive an interest rate of **17.0%**
# 
# (Also, it is assumed that **everyone will retire at 65**)
# 
# The bank rolled out the plan, and it worked *really well.* Now, there are dozens of new applications for savings accounts, and your boss says you need to calculate the expected savings for all of these new applications. 
# 
# You will need to **write a piece of code that will go through each of these new applications and calculate each individual's expected retirement savings.  Your code should make a list of all of the expected retirement savings.**
# 
# **Note:** In finding a solution to this problem, we **strongly recommend** that you use your code from the previous assignment involving compound interest. Repurposing old code is a common practice among computational professional!

# ### 3.1 Plan out your code
# 
# #### You and your groups members are expected to **use the whiteboards in the classeroom or a virtual whiteboard (e.g. [Google Jamboard](https://jamboard.google.com/) or [Aww app](https://awwapp.com/)) to come up with your plan.**. 
# 
# *Things to think about:*
# - How will you go through each application?
# - What variables will change for each application?
# - What calculations do you need to make for each application?
# - How can you use the code you wrote in the previous compound interest assignment?
# 
# (**Note:** Answering these questions is not the same as coming up with a plan!)

# *Write your plan here*

# ## &#128721; STOP AND ASK YOUR INSTRUCTOR TO COME OVER AND CHECK YOUR PLAN

# ### 3.2 Write out your code
# 
# Below are lists of all of the new applications, including the clients name, the amount they will save each year, and the age at which they're starting to save. 
# 
# **Write your code below. Store the final retirement savings in the list `final_retirement_savings`**

# In[ ]:


# New applications
client_name = ["Michael Mitchell","Ashley Moore","Fred Walker","Walter Wood","Jesse Gonzalez","Phillip Sanders","Marie Jenkins","Annie Brown","Christopher King","Carl Phillips","Betty Perez","Ashley Hernandez","Carlos Davis","Richard Jackson","Jean Cox","Sara Allen","Peter Butler","Justin Collins","Kevin Miller","Andrew Russell"]
savings_per_year = [4680,4680,4320,5880,5280,5640,4680,5520,5040,4200,4920,5400,5280,4560,5040,4440,5640,5040,4800,4680]
start_savings_age = [20,31,35,39,40,37,26,21,36,25,25,36,33,27,35,31,28,19,31,34]

final_retirement_savings = []


# In[ ]:


# Put your code here


# Once you think you've got everything coded up correctly, run the following cell to see how much money everyone ended up with. **Make sure to review the print statement formatting techiques used in this code.** This could be useful for future assignments.

# In[ ]:


# Print out the final savings for all of the new applications

for kk in range(len(final_retirement_savings)):
    print("{} will save ${:.2f} million by the time they retire".format(client_name[kk],final_retirement_savings[kk]/1.0e6))


# &#9989;&nbsp; **Question**: Which client will retire with the *largest* amount of money in their savings account? When did they start saving? How much money did they add every year?

# <font size="+3">&#9998;</font> *Put your answer here*

# &#9989;&nbsp; **Question**: Which client will retire with the *smallest* amount of money in their savings account? When did they start saving? How much money did they add every year?

# <font size="+3">&#9998;</font> *Put your answer here*

# &#9989;&nbsp; **Question**: Compare the people that retired with the most and least amount of money. What was the leading cause of the differences between the two? Is there anything that the person with the least amount of money saved could have done differently?

# <font size="+3">&#9998;</font> *Put your answer here*

# ---
# ### &#128721; STOP
# Check in with all of your group members to make sure you all understand everything to this point!

# ---
# ## Part 4: Writing Functions
# 
# In the pre-class assignment, you were introduced to how to write functions and when to use them.
# 
# To review:
# 
# 1. Functions are handy when you have code you have to run many times but want to avoid copying and pasting
# 2. Functions can prevent bugs by reducing the places you have to change code
# 3. Functions can make your code easier to read by allowing you to **compartmentalize** your code into separate functions which you can then call in the main body of your code
# 4. Functions can save future you time by allowing you to write functions you can use in future notebooks!
# 
# In general, if a piece of code is **repeated more than three times** or **may be useful later**, you should turn it into a function!
# 
# ---
# 
# In today's assignment and a previous assignment, you used a block of code that calculated the total amount of money saved for retirement. Let's use this bit of code to get some practice writing functions.
# 
# ### 4.1: Writing a function
# **Write a function that calculates the total amount of money saved in a retirement account.** Remember, your should define your function to accept all of the appropriate model parameters as input arguments. When you're finished, you should be able to insert this function directly into the code you wrote in the previous exercise.

# In[ ]:


# Put your code for your new function here


# ### 4.2 Testing your function
# 
# It's good to get into the habit of testing your function to see if it does what you want/expect it to do.
# 
# **Try running your function for the investor "Michael Mitchell" from above. Do you get the same answer you got before?** When you run your test, can you use the information directly from the lists above to get Michael's information?

# In[ ]:


# Test your function with the above inputs here.


# ### Part 4.3: Using your Function
# 
# **In the cell below, put your code from Part 3.2.** Then, **modify the code and use the function you wrote to calculate the total amount of money saved in the retirement account.**

# In[ ]:


# Put your code here


# Once you think you've got everything coded up correctly, run the following cell to see how much money everyone ended up with. If you get an unexpected error, double-check your code and discuss with your group what might be causing your bug.

# In[ ]:


# Print out the final savings for all of the new applications

for kk in range(len(final_retirement_savings)):
    print("{} will save ${:.2f} million by the time they retire".format(client_name[kk],final_retirement_savings[kk]/1.0e6))


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

# ## Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "In-class assignments" folder, find the appropriate submission link, and upload it there.
# 
# See you next class!

# &#169; Copyright 2023,  Department of Computational Mathematics, Science and Engineering at Michigan State University
