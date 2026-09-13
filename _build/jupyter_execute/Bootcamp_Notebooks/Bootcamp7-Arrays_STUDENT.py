#!/usr/bin/env python
# coding: utf-8

# # Bootcamp 7: Practice with Indexing and Masking 2D Arrays

# # Introduction
# 
# In this notebook, we will be reviewing how to create and index 2D numpy arrays (Part 1) and how to analyze and manipulate numpy arrays with masking (Part 2).
# 
# ---
# 

# In[ ]:


# Import modules
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Part 1: Indexing Arrays
# 
# In part 1, we will revisit some concepts related to indexing arrays and working with subsets of 2D arrays. Note that this was partly taken and modified from the Day-12 Pre-Class. Refer back to that notebook for more details. 
# 
# 
# ---
# 
# ## Array creation and basic properties 
# 
# ### Creating arrays
# The line below creates an 8x10 array of zeros called ```my_array```.  Note that you can do this with any numpy array method (```ones```, ```zeros_like```, ```ones_like```, etc.).  See [this page](http://docs.scipy.org/doc/numpy/reference/routines.array-creation.html) for a full list of routines for array creation.  You can also specify the array data type (float, int, etc.) by using the `dtype` argument, i.e., `dtype='float'` or `dtype='int'`.  By default, Numpy creates arrays of floating-point numbers.

# In[ ]:


# example 
a = np.zeros([8,10],dtype='int')
print("new array:\n", a)


# ### Shape and size of arrays
# The array `.shape` property tells you how large the array is in each dimension, `.ndim` tells you the number of dimensions, and `.size` tells you the total number of elements in the array. You can access each of the dimensions dim by `.shape[dim]`. Note that for 2D arrays, the dimensions refer to the number of rows (0th dimension) and the number of columns (1st dimension). 

# In[ ]:


print("the shape of this array is:", a.shape)
print("there are:", a.ndim, "dimensions")
print("there are", a.size, "total elements")

for i in range(a.ndim):
    print("the size of dimension", i, "is", a.shape[i])


# In[ ]:


"""EXERCISE: Create an 11 by 12 2D array with all ones as the elements and use the above \
commands to print the size of each dimension and the total number of elements in the array"""

# code here


# In[ ]:


# Given the 2D array below, report the same features of the array as stated above.

new_array = np.array([
       [ 2.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,  1.,  1.],
       [ 1.,  1.,  1.,  1.,  1.,  0.,  1.,  1.,  1.,  1.],
       [ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  1.],
       [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,  1.],
       [ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  1.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,  1.,  1.],
       [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
       [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  3.,  1.],
       [ 1.,  1.,  1.,  1.,  6.,  1.,  1.,  1.,  1.,  1.]])

# code here


# ---
# ## Slicing arrays 
# 
# Slicing arrays allows you to select some subset of the elements in a list or an array to manipulate or copy.  With slicing, there are three values that can be used along each dimension: `start`, `end`, and `step`, separated by colons.  
# 
# ### Here are some examples in 1D:
# 
# ```
# myarray[start,end]   # items start through end-1
# myarray[start:]      # items start through the end of the array
# myarray[:end]        # items from the beginning of the array through end-1
# myarray[:]           # a copy of the whole array
# myarray[start,end,step]  # every "step" item from start to end-1
# myarray[::step]      # every "step" item over the whole array, starting with the first element.
# ```
# 
# Note that negative indices count from the end of the array, so `myarray[-1]` is the last element in the array, `myarray[-2]` is the second-to-last element, etc.  You can also reverse the order of the array by starting at the end and counting to the beginning by negative numbers; in other words, `myarray[-1::-1]` starts at the end of the array and goes to the first element by counting down by one each time.

# In[ ]:


# create a 1D array with values 0...10
c = np.arange(0,10)
c

# Put your code below; if the above explanation is not enough to help you do the following, feel free to Google it 

#1. print the whole array

#2. print out some elements from the middle of the array

#3. print the second element through the second-to-last element

#4. print the first half of the array 

#5. print the second half of the array

#6. print every other element from 2-8 (inclusive)

#7. print every third element in the array

#8. print the array in backwards order


# ### 2D Cases
# The same sort of technique can be used with a multidimensional array, with `start`, `stop`, and (optionally) `step` specified along each dimension, with the dimensions separated by a comma. The syntax would be:
# `my2Darray[start1:stop1:step1, start2:stop2:step2]`
# with the same rules as above. You can also combine slicing with fixed indices to get some or all elements from a single row or column of your array.
# For example, array `b` created below is a $3\times 3$ array with the values 1–9 stored in it. We can do several different things:
# ```
# b[0,:]     # get the first row
# b[:,2]     # get the third column
# b[1,::2]   # get every other element of the first row, starting at element 0
# b[:2,:2]   # get a square array containing the first two elements along each dimension
# b[-2:,-2:] # get a square array containing the last two elements along each dimension
# b[::2,::2] # get a square array of every other element along each dimension
# b[-1::-1,-1::-1]  # original-size array, but reversed along both dimensions
# ```

# In[ ]:


# create a 2D array with values 0...10
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
b

# Put your code below; if the above explanation is not enough to help you do the following, feel free to ask!

# print the first row

# print the third column

# print every other element of the second row, starting with element 0

# print square array of first two elements along each dimension

# print reversed array


# ---
# # Part 2: Masking
# 
# Masking is another way to select particular elements of an array.  With a mask, instead of selecting elements **by index**, you are instead selecting them **by value**.  More specifically, you select them by whether or not their value satisfies a certain condition (e.g. `True` or `False`).

# ## Making a mask
# 
# To make a mask, all we need to do is evaluate a conditional statement on an array.  These conditional statements are the same ones we use for `if` statements and `while` loops.  Examples of these are:
# 
# - `my_mask = array == 7    # select elements equal to 7`
# - `my_mask = array < 3.1   # select elements less then 3.1`
# - `my_mask = array > 0     # select elements greater than 0`
# - `my_mask = array <= 10   # select elements less than or equal to 10` 
# - `my_mask = array != 2    # select elements not equal to 2`
# 
# In each of these cases, a mask is created and stored in the variable `my_mask`.  The mask is just another array, with the same shape as `array`, but filled with `True` or `False` values.

# In[ ]:


new_array = np.array([
       [ 2.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,  1.],
       [ 1.,  1.,  1.,  1.,  1.,  0.,  1.,  1.,  1.],
       [ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  1.],
       [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,  1.],
       [ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  1.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,  1.],
       [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
       [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  3.,  1.],
       [ 1.,  1.,  1.,  1.,  6.,  1.,  1.,  1.,  1.]])

new_mask = new_array > 2
print(new_mask)


# In[ ]:


# Put your code below

# make a mask that selects all of the zero values

# make a mask that selects all of the ones

# make a mask that selects all elements that are not equal to one


# ## Using a mask
# 
# To use a mask, we need to insert it into the "selection window" of the array.  Just like our indexing example above, this is done using square brackets:
# 
# ```
# my_mask = array == 7          # define a mask
# new_array = array[my_mask]    # use the mask to select only the elements where the mask is True
# ```
# 
# Masks can also be applied to different arrays, as long as they have the same shape:

# In[ ]:


# define a list of people
people = np.array(['Ahmad', 'Barbara', 'Colleen', 'Dameon', 'Eduardo'])

# define a list of heights
heights = np.array([6.0, 5.1, 6.4, 5.5, 6.2])

# create a mask using the heights array
tall_people_mask = heights > 6

# apply it to the people array
tall_people = people[tall_people_mask]
for person in tall_people:
    print(person,"is tall")


# In[ ]:


# Try adding an element to the people array (but not the heights array) and run the code again
# Do you understand the error?


# Masks can also be defined and used in the same line.  So instead of
# 
# ```
# my_mask = array == 7
# new_array = array[my_mask]
# ```
# 
# we can instead write:
# ```
# new_array = array[array == 7]
# ```
# which defines the mask `array == 7` and uses it in one line.
# 
# This makes for some compact and efficient code, but it can be confusing at first!  Let's practice:

# In[ ]:


new_array = np.array([
       [ 2.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,  1.],
       [ 1.,  1.,  1.,  1.,  1.,  0.,  1.,  1.,  1.],
       [ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  1.],
       [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,  1.],
       [ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  1.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,  1.],
       [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
       [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  3.,  1.],
       [ 1.,  1.,  1.,  1.,  6.,  1.,  1.,  1.,  1.]])

# Put your code below

# use a mask to make an array of only zeros, then print it

# use a mask to select all of the ones in new_array and count them

# use a mask to determine the sum of all of the elements, not counting the ones


# In[ ]:




