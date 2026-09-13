#!/usr/bin/env python
# coding: utf-8

# # Bootcamp 2: Initial Concepts Review Cheatsheet
# 
# <img src="https://cmse.msu.edu/sites/_cmse/assets/Image/image002.jpg"
#      alt="CMSE Logo"
#      align="right" 
#      height="82" 
#      width="82" />
# 
# Goal: Simple notebook to summarize some of the concepts from first couple weeks of CMSE 201

# **1. Variables**

# In[ ]:


int_var = 2   # Integer variable
float_var = 2.34  # floating point variable
str_var = 'bananas'  # string variable

print('1:', 'An integer plus a float works in python:',int_var+float_var)
#You can not do math with strings, but you can concatenate strings (if you turn your variables into strings first)
new_str_var = str(int_var)+' '+str_var+' is '+str(float_var)+' times the fun.'
print('2:',new_str_var)
# or you can just use a print statement with commas to make meaningful debugging and result statements
print('3:',int_var,'or',float_var, str_var,'are not all that fun.')


# **2. Lists**
# 
# A list stores a series of items in a particular order. You access items using an index, or within a loop.

# In[ ]:


list_ex = []   # initialize an empty list
list_ex.append('we')  # append an item to a list
list_ex.append('have')
list_ex.append('no')
list_ex.append('apples')
print('Print 1:',list_ex)  # print contents of variable or list
list_ex.remove('apples')  # remove specific entry from list, but only first entry with this value
print('Print 2:',list_ex)  # print contents of variable or list
list_ex.append('bananas')
print('Print 3:',list_ex)
print('Print 4:',list_ex[3])  # print the 4th value in the list 'list_ex'


# **3. Loops**
# 
# So far, we have learned:
#     - for loops  (repeats a block of code the number of times described in the "for" statement)
#     - while loops (repeats a block of code as long as a certain condition is true.)

# In[ ]:


for value1 in list_ex:   # loop through all the entries in list "list_ex"
    print('Current entry in variable value is:', value1)  # for each iteration, variable named "value1" 
                                                        #      will be assigned the next entry in "list_ex"


# In[ ]:


for index1 in range(len(list_ex)): # loop through integers from 0 to length of list "list_ex"
                                # for each iteration, variable named "index1"
                                #      will be assigned the next integer in 0 to length of list "list_ex"
    str_now = list_ex[index1]   # assign a variable the content of the index1-th entry of list "list_ex"
    print('The',index1,'entry in list_ex is',str_now)


# In[ ]:


index1 = 0
while index1 < len(list_ex):  # perform a while loop until index1 is equal to or greater than the length of list "list_ex"
    str_now = list_ex[index1]
    print('The',index1,'entry in list_ex is',str_now)
    index1 += 1               # increment whatever is in index1 by +1
    # Note this is the identical result as the for loop in cell above


# &#169; Copyright 2018,  Michigan State University Board of Trustees
