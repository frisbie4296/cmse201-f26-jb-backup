#!/usr/bin/env python
# coding: utf-8

# # Practice with: functions
# 
# This notebook includes practice with functions!
# 
# Functions are great for accomplishing repeated tasks and can be transferred between assignments. Be careful about how you use variables inside and outside of functions!

# ## Task

# In[ ]:


def my_favorite_animal(animal):
    print('My favorite animal is a/n',animal)

# What is the output of this function?
# How would you call this function to run it?


# ## Task
# 

# In[ ]:


def addition(num1,num2):
    return num1+num2

# What is the output of this function?
# How would you call this function to run it?
# How would you save the output to a variable?


# ## Task
# 
# Write a function that takes in an array of x-values, a slope, m, and an intercept, b, and returns the equation m*x+b. Test your work by calling the function! Make sure to comment your code.
# 
# For extra fun, save your results to variables and try making a plot!

# In[ ]:


# Put your pseudocode and code here
import numpy as np


# ## Task
# 
# Write a function that takes in an array of x values and returns the equation a*x^3 + b*x^2 + c*x + d
# 
# Write a second function that take in x and y values and plots the results.
# 
# Create a plot that contains at least 3 different lines using your two functions.

# In[ ]:


# put your code and pseudocode here



# ## Task
# 
# Write a function that takes in an array of values, calculates their sum, mean, and median, and returns the absolute value of the difference between the mean and median. Test your code by calling the function. Make sure to comment your code!

# In[ ]:


# Put your pseudocode and code here
random_distribution = np.random.wald(200,500,size=1000)


# Prepared by the Department of Computational Mathematics, Science and Engineering at MSU
