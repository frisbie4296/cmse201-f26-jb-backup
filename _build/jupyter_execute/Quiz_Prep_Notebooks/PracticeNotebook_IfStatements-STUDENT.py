#!/usr/bin/env python
# coding: utf-8

# # Practice with: `if` statements
# This notebook includes practice examples centered on if statements with increasing complexity.
# 
# If statements allow us to add complexity to code.

# ## Task
# 
# Comment the code below to explain what each line is doing.

# In[ ]:


'''basic structure of an if statement'''

for i in range(10): # add a comment here to explain what this code is doing
    if i%2 != 0: #add a comment here to exlplain what this code is doing
        print(i, 'is odd!') #add a comment here to explain what the code is doing


# ## Task
# 
# Comment the code below to explain what each line is doing.

# In[ ]:


'''basic structure of an if-else statement'''

for i in range(10): 
    if i%2 != 0: 
        print(i, 'is odd!') 
    else:             #add a comment here to explain what the code is doing
        print(i,'is even!') #add a comment here to explain what the code is doing


# ## Task
# 
# Write an if-else statement that loops through the list of numbers below and prints "I am greater than 25" if the number is greater than 25 and "I am less than 25" otherwise. Comment your code to explain what each line is doing!

# In[ ]:


list_of_ints = [18, 34, 9, 4, 5, 43, 11, 49, 50, 14, 35, 37, 39, 22, 38, 36, 46, 44, 22, 16]

# put your pseudocode and code here


# ## Task
# 
# Comment the code below to explain what each line is doing.

# In[ ]:


'''if-elif-else statments add further complexity to our code!'''

list_of_things = ['cheese',5.0,'puppies',1,3,'otters',9.7,1.5,'football']

for item in list_of_things: #add a comment here to explain what the code is doing
    if type(item)==str: #add a comment here to explain what the code is doing
        print(item, 'is a string!')
    elif type(item) == int:            #add a comment here to explain what the code is doing
        print(item,'is an integer!')
    else:             #add a comment here to explain what the code is doing
        print(item,'is a float!') 


# ## Task
# 
# Write a set of if-elif-else statements to categorize the animals in this list as two-legged, four-legged, swimming, or something else. Comment your code to explain what each line is doing!

# In[ ]:


list_of_animals = ['parrot','mussel','penguin','polar bear','salmon','zebra','shark','clam']

#put your code and pseudocode here


# Prepared by the Department of Computational Mathematics, Science and Engineering at MSU
