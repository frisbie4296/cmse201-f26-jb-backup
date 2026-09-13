#!/usr/bin/env python
# coding: utf-8

# # Bootcamp 1: Python Fundamentals

# # SOLUTION VIDEO [HERE](https://mediaspace.msu.edu/media/Bootcamp+1+Walk-through/1_3vfzvzbo)
# This notebook covers "Python fundamentals," including:
# 
# 1. <b>Data types</b>
# 1. <b>Lists</b>
# 1. <b>Loops</b>
# 
# For each topic, we briefly recap what we covered in class, then include practice problems for you to solve. These problems are meant to be instructive and help you learn/review the material. A few "challenge problems" are included!
# 
# <b>Important Note:</b> You don't have to complete all problems in order. Focus on sections where you want/need the most practice.

# # 1. Data Types

# Types are how we store and represent data in programs.

# ## 1.1 Primitive Data Types

# Primitive data types are the most basic way we store data. The following cell defines variables that are instances of three common primitive data types.

# In[2]:


"""Primitive data types."""
# integer data type
x = 5

# float data dype
value = 1.23

# string data type
string = "CMSE 201 is fun!"


# In the cell below, print out the `type` of each variable.

# In[3]:


"""EXERCISE: Print out the type of each variable defined above."""
print(type(x))
print(type(value))
print(type(string))


# In[4]:


"""EXERCISE: Here's a new primitive data type we haven't seen before. Print out it's type."""
mystery_variable = b"1011"
print(type(mystery_variable))


# Important: You DO NOT need to know about the above data type for the midterm.
# 
# You SHOULD KNOW about primitive data types including `int`, `float`, and `str` and how to work with them. You SHOULD ALSO KNOW how to check the type of a variable.

# ## 1.2 One Equal Sign Versus Two Equal Signs

# The following is crucial to know!
# 
# 1. An expression with <b>one equals sign</b>, for example `x = 5`, is an <b>assignment</b>. It says: "Hey Python, <i>assign</i> the value of `5` to the variable named `x`."
# 1. An expression with <b>two equals signs</b>, for example, `x == 5`, is a <b>comparison</b>. It says: "Hey Python, does the variable `x` have the value `5`?" This expression returns `True` or `False`.

# In[5]:


"""EXERCISE: Use two equal signs to check if the type of x is an integer (int in Python)"""
type(x) == int


# In[6]:


"""EXERCISE: Use two equal signs to check if the value of x is 5."""
x == 5


# In[7]:


"""EXERCISE: Use one equal sign to change the value of x to be 7."""
x = 7


# In[8]:


"""EXERCISE: Use two equal signs to check if the type of x is an integer (int in Python)"""
type(x) == int


# In[9]:


"""EXERCISE: Use two equal signs to check if the value of x is 5."""
x == 5


# We often use two equals signs (comparisons) in `if` statements and `for` loops.

# ## 1.2 "Container" Data Types

# Container data types store several primitive data types, just like a container stores several objects.
# 
# (Containers can also store containers themselves. For example, we can have a list of lists.)
# 
# Common container data types we have seen:
# 
# 1. `List`: A container of items with particular data types. Items an a `list` CAN be changed.
# 1. `Dictionary`: An container of items that are "key, value" pairs. NOTE: In Python, `dict` is short for dictionary.
# 
# The cell below defines each of these data types.

# In[10]:


"""Container data types."""
# lists
xlist = [1, 1, 2, 3, 5]

# tuples
xtuple = (1, 1, 2, 3, 5)

# dictionaries
strings_and_ints = {"one": 1, "one": 1, "two": 2, "three": 3, "five": 5}


# Most container objects have a length.

# In[11]:


"""EXERISE: Print out the length of each container data type defined above."""
# solution
print(len(xlist))
print(len(xtuple))
print(len(strings_and_ints))


# Note that dictionaries can only have one unique key for each value, to there's only four items in the dictionary.

# ### Practice Problems for `List`

# Here's four practice problems for the `list`. We'll see more when we look at `list`s below.

# In[12]:


"""EXERCISE: Print out the third number in xlist."""
print(xlist[2])


# In[13]:


"""EXERCISE: Change the third number in xlist to have the value -5."""
xlist[2] = -5


# In[14]:


"""EXERCISE: Append the number 8 to the list xlist, then print out the new list."""
xlist.append(8)
print(xlist)


# In[15]:


"""Test cases. Run this cell to check your solutions. If correct, no errors will occur."""
assert xlist == [1, 1, -5, 3, 5, 8]


# ### Practice Problems for `Dict`

# In[ ]:


"""EXERCISE: Print out the value for the key "one" in the dictionary given above."""


# In[ ]:


"""EXAMPLE: Python allows you to see all keys and values in a dict, as follows."""
print("Keys = ", strings_and_ints.keys())
print("Values =", strings_and_ints.values())


# In[ ]:


"""EXERCISE: Check if the key "eight" is in the dictionary's keys."""


# In[ ]:


"""EXERCISE: Add the key, value pair "eight", 8 to the dictionary given above."""


# In[ ]:


"""EXERCISE: Check if the key "eight" is in the dictionary's keys and 
if the value 8 is in the dictionary's values.
"""


# # Lists and Loops

# We know lists are containers. Lists are also called sequential data types in Python, meaning they store a sequence of objects.
# 
# Note: Objects in a list do not have to be of the same type! (For example, [1, "two"] is a valid list.)
# 
# Lists are mutable, meaning they can be changed. (Tuples are immutable, meaning they cannot be changed.)
# 
# There are several ways to create lists in Python. Some examples are shown below.

# In[ ]:


"""EXAMPLE: Creating lists in Python."""
# by listing all values
list1 = [1, 2, 3, 4, "I", "declare", "a", "thumb", "war"]

# by using list(range(...)) to get range of values in a list
list2 = list(range(4)) # = [0, 1, 2, 3]

# by using multiplication to get a list of a certain length with a certain value
list3 = [1] * 5 # = [1, 1, 1, 1, 1] (a list of five ones)

# by converting other containers into lists
xtuple = (1, 2, 3)
xlist = list(xtuple) # = [1, 2, 3]


# ## Practice Problems with Lists and Loops

# Complete the following problems to get practice with lists.

# In[16]:


"""EXERCISE: Create a list with all integers from zero to twenty."""
### ANSWER
# solution 1
values = list(range(20 + 1))

# solution 2
values = []
for x in range(20 + 1):
    values.append(x)


# In[17]:


"""Test cases."""
assert len(values) == 21
assert values == [x for x in range(20 + 1)]


# In[18]:


"""EXERCISE: Make the fourth entry in the list equal to zero."""
values[5] = 0


# In[19]:


"""Test cases."""
assert values[5] == 0
assert sum(values) == int(21 * 20 / 2 - 5)


# In[20]:


"""EXERCISE: Append the integer 21 to the list."""
values.append(21)


# In[21]:


"""Test cases."""
assert len(values) == 22
assert values[-1] == 21


# For the next exercise, you'll need to check if a number is even. This can be done by using the "modulus operator" `%` in Python. The value of `a % b`, where `a` and `b` are integers, is the remainder of `a / b`. For example, `5 % 2 = 1`, since 5 divided by 2 has a remainder of 1.
# 
# To check if a number `num` is even, you can thus use `num % 2 == 0`.

# In[22]:


"""EXERCISE: Make every entry with an even element equal to (the integer) zero."""
# solution 1
for index in range(len(values)):
    if values[index] % 2 == 0:
        values[index] = 0


# In[23]:


"""Test cases."""
assert [x % 2 == 1 for x in values]


# # Loops

# Loops are extremely useful in programming. They prevent us from having to write out every instruction explicity. The caveat is you have to be careful to write the loop correctly <i>for all</i> cases!
# 
# In class, we covered
# 
# 1. `while` loops: Keep performing the code in the <i>body</i> of the loop while an expression is `True`.
# 1. `for` loops. Perform the code in the <i>body</i> of the loop for a given number of iterations or values.

# In[24]:


"""EXAMPLE: A typical while loop."""
# variable that we care about
x = 0

# while loop
while x < 5:
    # body of the loop
    print(x)
    x += 1


# In[25]:


"""EXAMPLE: A typical for loop."""
# variable that we care about
x = [0, 1, 2, 3, 4]

for value in x:
    print(value)


# As can be seen, the `for` loop produces the same output as the `while` loop. This is generally true, for any loop:
# 
# <i>Any loop can be written as a `for` loop.</i>
# 
# Because of this, we only focus on `for` loops below. Sometimes it is easier or more natural to use a different style of loop, so you should be comfortable with `while` loops as well.

# ## For Loops: Two Common Constructions

# We use two main types, or "constructions," of `for` loops in Python.
# 
# (1) <b>"Loop by index."</b> We use this to loop over the indices in an iterable object.
# 
# (Note: *Iterable* means a sequential data type. That is, a data type that "is able to be iterated over." Examples include lists and tuples.)
# 
# (2) <b>"Loop by value."</b> We use this to loop over the values of an iterable object.

# In[26]:


"""EXAMPLE: Loop by index."""
values = ["a", "b", "c", "d"]

for index in range(len(values)):
    print(values[index])


# We commonly use variables like `i`, `j`, or `k` for the above `index` variable. We'll continue to use `index` for pedagogy in this notebook.

# In[27]:


"""EXAMPLE: Loop by value."""
values = ["a", "b", "c", "d"]

for value in values:
    print(value)


# We commonly use variables like `x`, `y`, or `val` (short for value) for the above `value` variable. (Really, anything that's NOT `i`, `j`, or `k` so we don't confuse ourselves with the "loop by index" construction above.) We'll continue to use `value` for pedagogy in this notebook.

# ### When to use which?

# *Each for loop type is useful in different situations.*
# 
# To just loop over values in an iterable object, "loop by value" is sufficient and simpler to program.
# 
# You can use "loop by index" when:
# 
# * You need to access values from multiple lists at the same index.
# * You need neighboring values from the list.

# ## Practice Problems

# In the following practice problems, consider which type of for loop construction is easiest to solve the problem. For extra practice, solve each problem using both constructions.

# In[28]:


"""EXERCISE. Given two lists of the same length, use ONE loop to print out all elements from each list,
in alternating order.

Example: Given [1, 2] and [3, 4], your code should produce the output
1
3
2
4
"""
list1 = ["I", "ace", "CMSE 201"]
list2 = ["will", "the", "midterm!"]

# YOUR CODE HERE

for index in range(len(list1)):
    print(list1[index])
    print(list2[index])


# In[29]:


"""EXERCISE: Given a list, print out the value in each list squared."""
xlist = [1, 2, 3, 4, 5]

# YOUR CODE HERE
for x in xlist:
    print(x**2)


# In[30]:


"""EXERCISE: Given a list, create a new list of squared values.
Example: Given [1, 2, 3], your code should produce the new list [1, 4, 9] stored in some variable."""
xlist = [1, 11, 21, 1211]

# YOUR CODE HERE

newxlist = []
for x in xlist:
    newxlist.append(x**2)
print(newxlist)

# solution using "loop by index"
newxlist = [None] * len(xlist)
for index in range(len(xlist)):
    newxlist[index] = xlist[index]**2
print(newxlist)


# In[31]:


"""EXERCISE: Given a list, compute the sum of all elements in the list.
Example: Given [1, 2, 3], store the resulting sum 1 + 2 + 3 = 6 in some variable."""
numbers = [x * (x - 1) * (x - 2) for x in range(5, 20)]

# YOUR CODE HERE
# solution using "loop by value"
val = 0
for x in numbers:
    val += x
print("The sum is", val)

# solution using "loop by index"
val = 0
for index in range(len(numbers)):
    val += numbers[index]
print("The sum is", val)


# In[32]:


"""EXERCISE: Given a list, compute the product of all elements in the list.
Example: Given [1, 2, 3], store the resulting product 1 * 2 * 3 = 6 in some variable."""
numbers = list(range(1, 10))

# YOUR CODE HERE
val = 1
for x in numbers:
    val *= x
print("The product is", val)

# solution using "loop by index"
val = 1
for index in range(len(numbers)):
    val *= numbers[index]
print("The product is", val)


# In[33]:


"""EXERCISE: Given a list, compute the "nearest neighbor sum" of the list. That is, a list of the same length
whose nth value is defined as 

a[n] = a[0] for n = 0,
a[n] = a[n - 1] + a[n] for all n > 0

Example: Given [1, 2, 3], you should produce the list [1, 1 + 2, 2 + 3] = [1, 3, 5]."""
xlist = list(range(1, 10))

# YOUR CODE HERE
nsum = [None] * len(xlist)

nsum[0] = xlist[0]
for index in range(1, len(xlist)):
    nsum[index] = xlist[index - 1] + xlist[index]

print(nsum)


# In[34]:


"""EXERCISE: Given a list, compute the "cumulative sum" of the list. That is, a list of the same length
whose nth value is defined as 

a[n] = a[0] for n = 0,
a[n] = a[0] + a[1] + ... + a[n - 1] + a[n] for all n > 0

Example: Given [1, 2, 3], you should produce the list [1, 1 + 2, 1 + 2 + 3] = [1, 3, 6]."""
xlist = list(range(1, 10))

# YOUR CODE HERE

cumsum = []
cumsum.append(xlist[0])

for index in range(1, len(xlist)):
    cumsum.append(sum(xlist[:index + 1]))

print(cumsum)


# In[35]:


"""CHALLENGE PROBLEM: Given a list, produce a new list whose elements are reversed.

Example. Given [1, 2, 3], your code should produce a new list that is equal to [3, 2, 1]."""
numbers = list(range(20))

# solution 1
reverse = []
for index in range(len(numbers)):
    last_index = len(numbers) - index - 1
    reverse.append(numbers[last_index])
print(reverse)


# # Summary

# * Primitive data types include `int`, `str`, and `float`.
# * Collections include `list` and `dict`.
# * The collection `list` is also called a sequential data type.
# * Loops allow us to write complex code more simply by not having to type every instruction.
# * All loops, including `while` loops, can be written as a `for` loop.
# * There are two common constructions with for loops: "loop by value" and "loop by index."

# # More Practice

# * If these types of programming problems helped you, you may find additional help on websites like the ones listed [HERE](https://docs.google.com/document/d/13ZV6qrqy1ydUnZeM2D3tm5DJH2rqdOg2m295BWSka3U/edit?usp=sharing)!
# * Go back through homework assignments after these problems.
# * Rewatch videos in pre-class assignments and work through pre-class/in-class assignments.

# Good luck on the quiz!
