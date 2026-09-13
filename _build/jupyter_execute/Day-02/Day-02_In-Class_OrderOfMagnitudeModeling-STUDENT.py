#!/usr/bin/env python
# coding: utf-8

# # Day 2 In-class Assignment: Order of Magnitude Modeling

# ### <p style="text-align: right;"> &#9989; **Put your name here** </p>
# #### <p style="text-align: right;"> &#9989; Put your group member names here</p>

# ## How many mice would it take to fill up this classroom?
# 
# ### (a.k.a., making order-of-magnitude estimates for fun and profit!)
# ![Mouse](https://www.jax.org/-/media/jaxweb/images/jax-mice-and-services/mice/web_0009_find-and-order-jax-mice.jpg?h=316&w=467&la=en&hash=D42556D3A616EC2E099378DB9CA5403D0C38C1E4)

# ## Learning Goals 
# 
# Why are we asking you to do this?
# 
# One type of modeling is called "order-of-magnitude estimation" or "order-of-magnitude modeling."  A physicist would call this a "Fermi Problem" after Enrico Fermi, a physicist who participated in the Manhattan Project and who was famously good at making estimates of this sort.  More specifically, this sort of modeling makes us think about:
# 
# * The quantities that should go into our models, and the reasonable values of those quantities.
# * How the different parts of our model might interact with one another.
# * What a "good enough" answer would be to a particular problem

# ## The Problem
# 
# In this project, your group is going to calculate an answer one of the following questions:
# 
# 1. How many grams of caffeine get consumed on MSU's campus each week?  
# 2. How much does the air above Lake Superior weigh?
# 3. If somebody left one of the bathroom faucets running at the Breslin Center, how long would it take to fill it up with water?  
# 4. If all of the toilet paper used per week in the United States were rolled out across the surface of Michigan could you cover the entire state? If so, could you cover it more than once?
# 5. Which has more mass, the air in this classroom or the brains in this classroom?  
# 6. On average, how many people are airborne in the world at a given moment?  
# 7. How many total miles do all Americans drive in their cars in one year, and how does this compare to the circumference of the Earth ($2.5 \times 10^4$ miles), the distance from the Earth to the Sun ($9 \times 10^7$ miles), and size of the Solar System ($10^9$ miles)?
# 8. After a particularly exciting Spartan football game, the fans rush the field. How many people can fit onto the football field at Spartan Stadium?
# 
# ---
# # Part 1
# 
# **As a group**, you will be assigned one of these problems to answer. You will need to come up with:
# 1. The questions that you need to ask and answer to come up with an estimate for your problem.
# 2. The equation(s) you will need to solve your problem.
# 3. The reasonable values that would go into the equation(s).
# 
# Once you have finished these steps, you and your group will implement a simple computer program to calculate a range of answers to your problem.
# 
# #### Use a virtual whiteboard app like [Google Jamboard](https://jamboard.google.com/) or the [Aww app](https://awwapp.com/) or the physical whiteboards in the classroom to write out your ideas to ensure that everyone is on the same page and allow your instructors to see your progress.

# ## 1.1 Describing Your Model
# **In the cell below, write down your assigned question and the parameters in your model.** Also write down the range of possible values for each of the parameters!
# 
# 

# <font size=6 color="#009600">&#9998;</font> *Put your answer here! (reminder: double-click on this cell to go into "edit mode" and then hit shift+enter when you're done)*
# 
# 

# ## 1.2 Coding Your Model
# In the cell below, write a program to calculate and print out an estimate for your model.

# > **Important**: When writing your code, **define variables for each value of interest.**  Then use those variables in your equations.  In other words, do not  hard-code the values in your equations (do not put *numbers* in your equations, put *variables* in your equations).  
# >
# > As an example, if I want to compute and then print the area of a right triangle, which I know to be $A = \frac{1}{2} b h$, I might write my code like so:
# >
# >> ```
# >> base = 10
# >> height = 5
# >>
# >> area = (base * height) / 2
# >>
# >> print("The area is:", area)
# >> ```  
# >       
# > By doing this, if I decide I need to change the `base` value or the `height` value, I can just change the value where they are defined. This can be especially useful if I have to use the values multiple times or if I want to experiment with changing the values.

# In[ ]:


# write a program in this cell to calculate and print out an estimate
# of the answer to the question you've chosen to solve!




# ## 1.3 Exploring Model Results
# **Now, run your model several times**, and each time change the values of the parameters to a different value in the range you think is valid.  In the cell below, write down all of your answers.  What is the total range, and approximately what is the average value?

# <font size=6 color="#009600">&#9998;</font> *Put your answer here!*

# ---
# ## &#128721; STOP AND ASK YOUR INSTRUCTOR TO COME OVER
# 
# # Part 2
# 
# ## 2.1 Pick a Second Model
# **Now, picking one of the other questions and going through the process of making another order-of-magnitude estimate.** Each group must choose a *different* question. Once you have decided on which question you are going to try to tackle, try working through the answer on your own, but check in with the members of your group if you run into issues or want to bounce ideas off each other.

# ## 2.2 Describe the Model
# **In the cell below, write down your chosen question and the parameters in your model.** Also write down the range of possible values for each of the parameters!

# <font size=6 color="#009600">&#9998;</font> *Put your answer here!*

# ## 2.3 Coding the Model
# 
# In the cell below, write a program to calculate and print out an estimate for your model.

# In[ ]:


# write a program in this cell to calculate and print out an estimate
# of the answer to the question you've chosen to solve!




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


# ### Submit this assignment by uploading it to the course Desire2Learn web page.  
# Go to the "In-class assignments" folder, find the assignment submission link for today's assignment, and upload it there.
# 
# #### Congratulations, you're done!
# 
# Make sure to complete the **Pre-class assignment before next class.** See you next class!
# 
# See you next class!

# &#169; Copyright 2023, Department of Computational Mathematics, Science and Engineering at Michigan State University.
