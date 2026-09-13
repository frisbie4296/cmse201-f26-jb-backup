#!/usr/bin/env python
# coding: utf-8

# # Day 7 In-class Assignment: Reviewing and practicing prior concepts

# ### <p style="text-align: right;"> &#9989; Put your name here.
# <p style="text-align: right;"> &#9989; Put your group member names here.

# ## Learning Goals:
# 
# The primary purpose of this assignment is to give you the opportunity to review and practice the types of coding concepts you've identified as having a weaker understanding of than other, or where you've identified some gaps in your knowledge.
# 
# As such, the learning goals embedding within this activity are those that have been covered in previous assignments.

# ---
# <a id="top"></a>
# ## Plans for today
# 
# For today's assignment, rather than have you follow one specific, pre-determined activity, you're going to use the reflection you did in your pre-class assignment to **target specific sections of the assignment that you feel like would be particularly beneficial for you to review or practice**.
# 
# Your instructors will float around and be ready to help answer questions you may have or help you to solve/troubleshoot issues you run into. You may also find it useful to check in with your group from time to time to see if anyone else might have idea for how to solve something you get stuck on or answer questions you might have.
# 
# **If you have any lingering questions from previous assignments from the course, you can ask questions about those as well**.
# 
# 
# ### Getting around in this document
# 
# To help you navigate this assignment, the notebook is divided up into section and these sections are listed below. You'll notice that you can actually click on each section to jump right to that section and within each section, there is another link you can click to jump back up to the top. **These links should help to minimize the amount of scrolling you need to do!**.
# 
# #### Concept Sections:
# 
# 1. [Defining variables and basic data types](#variables)
# 2. [Performing arithemtic operations and concatenating strings](#operators)
# 3. [Working with loops in Python](#loops)
# 4. [Connecting lists and loops to interact with data](#listsandloops)
# 5. [Conditional statements (using `if` in Python)](#if)
# 6. [Defining and using functions](#functions)
# 7. [Debugging code](#debugging)
# 
# ---

# <a id="variables"></a>
# ## 1. Defining variables and basic data types
# ### [back to top](#top)

# Variables and data types are how we store and represent data in programs. Being comfortable with what the different data types are and how you can store them in variable is fundamental to using Python.

# ### 1.1 Primitive Data Types

# Primitive data types are the most basic way we store data. The following cell defines variables that are instances of three common primitive data types.

# In[ ]:


"""Primitive data types."""
# integer data type
x = 5

# float data dype
value = 1.23

# string data type
string = "CMSE 201 is fun!"


# In the cell below, print out the `type` of each variable.

# In[ ]:


"""EXERCISE: Print out the type of each variable defined above."""


# In[ ]:


"""EXERCISE: Here's a new primitive data type we haven't seen before. Print out it's type."""
mystery_variable = b"1011"


# Important: You DO NOT need to know about the above data type for the quiz. This is just a useful reminder that the `type` function can be useful when you encounter something you're not familiar with.
# 
# You SHOULD KNOW about primitive data types including `int`, `float`, and `str` and how to work with them. You SHOULD ALSO KNOW how to check the type of a variable.

# ### 1.2 One Equal Sign Versus Two Equal Signs

# The following is crucial to know!
# 
# 1. An expression with <b>one equals sign</b>, for example `x = 5`, is an <b>assignment</b>. It says: "Hey Python, <i>assign</i> the value of `5` to the variable named `x`."
# 1. An expression with <b>two equals signs</b>, for example, `x == 5`, is a <b>comparison</b>. It says: "Hey Python, does the variable `x` have the value `5`?" This expression returns `True` or `False`.

# In[ ]:


"""EXERCISE: Use two equal signs to check if the type of x is an integer (int in Python)"""


# In[ ]:


"""EXERCISE: Use two equal signs to check if the value of x is 5."""


# In[ ]:


"""EXERCISE: Use one equal sign to change the value of x to be 7."""


# In[ ]:


"""EXERCISE: Use two equal signs to check if the type of x is an integer (int in Python)"""


# In[ ]:


"""EXERCISE: Use two equal signs to check if the value of x is 5."""


# We often use two equals signs (comparisons) in `if` statements and `for` loops.

# ### 1.3 "Container" Data Types

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

# In[ ]:


"""Container data types."""
# lists
xlist = [1, 1, 2, 3, 5]

# tuples
xtuple = (1, 1, 2, 3, 5)

# dictionaries
strings_and_ints = {"one": 1, "one": 1, "two": 2, "three": 3, "five": 5}


# We have been primarily workings the `list` data type to store data up to this point and this is the one you should be familiar with. The other can be useful to know about, but won't show up on a quiz.
# 
# Most container objects have a length.

# In[ ]:


"""EXERCISE: Print out the length of each container data type defined above."""


# Note that dictionaries can only have one unique key for each value, so there's only four items in the dictionary.

# #### Practice Problems for `List`

# Here's four practice problems for the `list`. We'll see more when we look at `list`s below.

# In[ ]:


"""EXERCISE: Print out the third number in xlist."""


# In[ ]:


"""EXERCISE: Change the third number in xlist to have the value -5."""


# In[ ]:


"""EXERCISE: Append the number 8 to the list xlist, then print out the new list."""


# In[ ]:


"""Test cases. Run this cell to check your solutions. If correct, no errors will occur."""
assert xlist == [1, 1, -5, 3, 5, 8]


# #### Practice Problems for `Dict` (this can be useful to review, but won't end up on the quiz)

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


# ---
# <a id="operators"></a>
# ## 2. Performing arithmetic operations and concatenating strings
# ### [back to top](#top)
# 
# When working with variables of different types in Python, those that are numbers (i.e. integers and floats) can be used to perform mathematical operations, but those that are strings cannot. However, you can use what looks like a mathematical operator, `+`, to concatenate (or merge) two strings together. You can also convert non-strings to strings with the `str` function.
# 
# Review the code below that defines some variable and manipulates them a bit.

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


# In[ ]:


"""EXERCISE: Test out multiply, dividing int_var and float_var."""


# In[ ]:


"""EXERCISE: Take the int_var variable and square it, what operator do you need to do that?"""


# Obviously, there is a lot of additional math you could do with Python variables. Feel free to experiment with other math you're not comfortable with or ask an instructor if you have any questions about doing math in Python.

# Make sure you're comfortable **concatenating** strings.

# In[ ]:


"""EXERCISE: Define a new string variable and concatenate it with the str_var variable.
Choose something that makes sense!"""


# ---
# <a id="loops"></a>
# ## 3. Working with loops in Python
# ### [back to top](#top)

# Loops are extremely useful in programming. They prevent us from having to write out every instruction explicity. The caveat is you have to be careful to write the loop correctly <i>for all</i> cases!
# 
# In class, we covered
# 
# 1. `while` loops: Keep performing the code in the <i>body</i> of the loop while an expression is `True`. We sometimes refer to this as "**looping by condition**."
# 1. `for` loops. Perform the code in the <i>body</i> of the loop for a given number of iterations or values.

# In[ ]:


"""EXAMPLE: A typical while loop."""
# variable that we care about
x = 0

# while loop
while x < 5:
    # body of the loop
    print(x)
    x += 1


# In[ ]:


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

# ## `for` loops: Two Common Constructions

# We use two main types, or "constructions," of `for` loops in Python.
# 
# (1) <b>"Loop by integer or index."</b> We use this to loop over the indices in an iterable object.
# 
# (Note: *Iterable* means a sequential data type. That is, a data type that "is able to be iterated over." Examples include lists and tuples.)
# 
# (2) <b>"Loop by value."</b> We use this to loop over the values of an iterable object.

# In[ ]:


"""EXAMPLE: Loop by index."""
values = ["a", "b", "c", "d"]

for index in range(len(values)):
    print(values[index])


# We commonly use variables like `i`, `j`, or `k` for the above `index` variable. We'll continue to use `index` for pedagogy in this notebook.

# In[ ]:


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

# In[ ]:


"""EXERCISE. Given two lists of the same length, use ONE loop to print out all elements from each list,
in alternating order.

Example: Given [1, 2] and [3, 4], your code should produce the output
1
3
2
4
"""
list1 = ["I", "ace", "CMSE 201"]
list2 = ["will", "the", "quiz!"]

# YOUR CODE HERE


# In[ ]:


"""EXERCISE: Given a list, print out the value in each list squared."""
xlist = [1, 2, 3, 4, 5]

# YOUR CODE HERE


# In[ ]:


"""EXERCISE: Given a list, create a new list of squared values.
Example: Given [1, 2, 3], your code should produce the new list [1, 4, 9] stored in some variable."""
xlist = [1, 11, 21, 1211]

# YOUR CODE HERE


# In[ ]:


"""EXERCISE: Given a list, compute the sum of all elements in the list.
Example: Given [1, 2, 3], store the resulting sum 1 + 2 + 3 = 6 in some variable."""
numbers = [x * (x - 1) * (x - 2) for x in range(5, 20)]

# YOUR CODE HERE


# In[ ]:


"""EXERCISE: Given a list, compute the product of all elements in the list.
Example: Given [1, 2, 3], store the resulting product 1 * 2 * 3 = 6 in some variable."""
numbers = list(range(1, 10))

# YOUR CODE HERE


# In[ ]:


"""EXERCISE: Given a list, compute the "nearest neighbor sum" of the list. That is, a list of the same length
whose nth value is defined as 

a[n] = a[0] for n = 0,
a[n] = a[n - 1] + a[n] for all n > 0

Example: Given [1, 2, 3], you should produce the list [1, 1 + 2, 2 + 3] = [1, 3, 5]."""
xlist = list(range(1, 10))

# YOUR CODE HERE


# In[ ]:


"""EXERCISE: Given a list, compute the "cumulative sum" of the list. That is, a list of the same length
whose nth value is defined as 

a[n] = a[0] for n = 0,
a[n] = a[0] + a[1] + ... + a[n - 1] + a[n] for all n > 0

Example: Given [1, 2, 3], you should produce the list [1, 1 + 2, 1 + 2 + 3] = [1, 3, 6]."""
xlist = list(range(1, 10))

# YOUR CODE HERE


# In[ ]:


"""CHALLENGE PROBLEM: Given a list, produce a new list whose elements are reversed.

Example. Given [1, 2, 3], your code should produce a new list that is equal to [3, 2, 1]."""
numbers = list(range(20))


# ---
# <a id="listsandloops"></a>
# ## 4. Connecting lists and Loops
# ### [back to top](#top)

# We know lists are containers. Lists are also called sequential data types in Python, meaning they store a sequence of objects.
# 
# **Note**: Objects in a list do not have to be of the same type! (For example, [1, "two"] is a valid list.)
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

# Complete the following problems to get practice with lists. **Note**: you will find some code cell below that use the `assert` command in Python to test the code you write. You do not need to know exactly what this command does, but you should be able to run those cells without getting an error. If you get an error, then something you didn't in your code isn't quite right.

# In[ ]:


"""EXERCISE: Using a loop, create a list with all integers from zero to twenty. Call the list values."""


# In[ ]:


"""Test cases."""
assert len(values) == 21
assert values == [x for x in range(20 + 1)]


# In[ ]:


"""EXERCISE: Make the fourth entry in the list equal to zero."""


# In[ ]:


"""Test cases."""
assert values[3] == 0
assert sum(values) == int(21 * 20 / 2 - 3)


# In[ ]:


"""EXERCISE: Append the integer 21 to the list."""


# In[ ]:


"""Test cases."""
assert len(values) == 22
assert values[-1] == 21


# For the next exercise, you'll need to check if a number is even. This can be done by using the "modulus operator" `%` in Python. The value of `a % b`, where `a` and `b` are integers, is the remainder of `a / b`. For example, `5 % 2 = 1`, since 5 divided by 2 has a remainder of 1.
# 
# To check if a number `num` is even, you can thus use `num % 2 == 0`.

# In[ ]:


"""EXERCISE: Find every entry in the list with an even number and set that entry equal to (the integer) zero."""


# In[ ]:


"""Test cases."""
assert [x % 2 == 1 for x in values]


# ---
# <a id="if"></a>
# ## 5. Conditional Statements (using `if` in Python)
# ### [back to top](#top)
# 
# This section includes practice examples centered on `if` statements with increasing complexity.
# 
# `if` statements are great way to control the flow of our code and add nuance an complexity to our algorithms.

# ### Task
# 
# Comment the code below to explain what each line is doing.

# In[ ]:


'''basic structure of an if statement'''

for i in range(10): # add a comment here to explain what this code is doing
    if i%2 != 0: #add a comment here to exlplain what this code is doing
        print(i, 'is odd!') #add a comment here to explain what the code is doing


# ### Task
# 
# Comment the code below to explain what each line is doing.

# In[ ]:


'''basic structure of an if-else statement'''

for i in range(10): 
    if i%2 != 0: 
        print(i, 'is odd!') 
    else:             #add a comment here to explain what the code is doing
        print(i,'is even!') #add a comment here to explain what the code is doing


# ### Task
# 
# Write an if-else statement that loops through the list of numbers below and prints "I am greater than 25" if the number is greater than 25 and "I am less than 25" otherwise. Comment your code to explain what each line is doing!

# In[ ]:


list_of_ints = [18, 34, 9, 4, 5, 43, 11, 49, 50, 14, 35, 37, 39, 22, 38, 36, 46, 44, 22, 16]

# put your pseudocode and code here


# ### Task
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


# ### Task
# 
# Write a set of if-elif-else statements to categorize the animals in this list as two-legged, four-legged, swimming, or something else. Comment your code to explain what each line is doing!

# In[ ]:


list_of_animals = ['parrot','mussel','penguin','polar bear','salmon','zebra','shark','clam']

#put your code and pseudocode here


# ---
# <a id="functions"></a>
# ## 6. Defining and using functions (functions will not be on Quiz 1, but will likely be involved in future quizzes)
# ### [back to top](#top)

# Like loops, functions are another extremely useful tool in programming. Functions allow use to run code in different places for different uses <i>without rewriting the code every time!</i>
# 
# Functions have the following key components.
# 
# 1. <b>Input:</b> What is "fed into" the function.
# 1. <b>Body:</b> The "body of a function" is the code inside of the function that executes when the function is called.
# 1. <b>Output:</b> Whatever a function "produces," depending on its input. "Output" is also called a <b>return</b> value.
# 
# Here's an example of a function that adds two numbers.

# In[ ]:


"""EXAMPLE: Defining a function in Python."""
def add(x, y):
    val = x + y
    return val


# Let's breakdown this function:
# 
# 1. <b>Input:</b> Two numbers, called `x` and `y`.
# 1. <b>Body:</b> The line `val = x + y`. (Generally, every line that's inside (indented) in the function is part of the body. Whether we include the `return` statement as part of the body depends on who you talk to and is not important here.)
# 1. <b>Output:</b>The sum of the two numbers, called `val`, which is returned by the function.

# <b>KEY POINT:</b> Variables INSIDE a function CANNOT be accessed OUTSIDE a function.
# 
# The names of the variables are "dummies" and can be changed.
# 
# <b>KEY POINT:</b> To get the output of a function, we must CALL the function.
# 
# You cannot access the variable `val` inside the function `add` above! To get it, you must call the function.

# In[ ]:


"""EXAMPLE: Calling a function."""
answer = add(10, 20)
print(answer)


# The function above is simple and wouldn't likely help us simplify our code as programmers. Functions that perform more complex tasks that we need to do repeteadly can <i>significantly help us as programmers.</i>

# ### The Difference Between `return` and `print`

# In a few words:
# 
# 1. `return` produces an output that can be stored in a variable when the function is called.
# 1. `print` displays variables to the screen. They cannot be stored by calling the function.

# In[ ]:


"""EXAMPLE: Difference between print and return."""

def return_string(string):
    return string

def print_string(string):
    print(string)


# Let's call the `return_string` function below:

# In[ ]:


output_from_return = return_string("hello")


# Nothing happens when we call the function. The output is stored in the variable called `output_from_return`.

# In[ ]:


print(type(output_from_return))
print(output_from_return)


# Now let's call the `print_string` function below:

# In[ ]:


output_from_print = print_string("hello")


# When we call this function, the string `hello` is printed to the screen. This happens because there is a `print` statement in the body of the function. When the function is called, every line in the body of the function gets evaluated.
# 
# Let's look at the variable `output_from_print`:

# In[ ]:


print(type(output_from_print))
print(output_from_print)


# The variable is `None` because the function doesn't return anything. (In other words, it returns `None`.)

# ### Practice Problems for Functions

# Solve the following exercises to get more practice with functions.

# In[ ]:


"""EXERCISE: Write a function called mult that 

inputs: two integers 

and 

returns: the product of the two integers.

Example: mult(4, 5) should return 4 * 5 = 20.
"""


# In[ ]:


"""Test cases. If your code is correct, no errors will be thrown."""
assert mult(4, 5) == 20
assert mult(1, 3) == 3
assert mult(2, 4) == 8


# In[ ]:


"""EXERCISE: Write a function called square that 

inputs: one integer 

and

returns: the squared integer.

Example: square(5) should return 5**2 = 25.
"""


# In[ ]:


"""Test cases. If your code is correct, no errors will be thrown."""
assert square(5) == 25
assert square(0) == 0
assert square(1) == 1


# In[ ]:


"""EXERCISE: Use your function square to compute the squared value of each element in a given list,
appending each to a new list."""
# given input
xlist = list(range(20 + 1))


# In[ ]:


"""EXERCISE: Write a function called contains which 

inputs: a list and an item 

and 

outputs: True if the item is in the list, else False.

Examples: contains([1, 2, 3], 2) should return True
          contains([1, 2, 3], 4) should return False
          contains(["a", "b", "c"], "c") should return True.
"""


# In[ ]:


"""Test cases. If your code is correct, no errors should be thrown."""
assert contains([1, 2, 3], 1)
assert not contains([1, 2, 3], 4)
assert contains(["a", "b", "c"], "c")


# In[ ]:


"""EXERCISE: Write a function called in_either that

inputs: two lists (call them list1 and list2) and an item

and

returns: True if the item is in either list, else False.

Hint: Can you utilize a function you've already written?

Examples: in_either([1, 2, 3], [4, 5, 6], 3) should return True
          in_either([1, 2, 3], [4, 5, 6], 7) should return False
"""


# In[ ]:


"""Test cases. If your code is correct, no errors should be thrown."""
assert in_either([1, 2, 3], [4, 5, 6], 3) == True
assert in_either([1, 2, 3], [4, 5, 6], 7) == False
assert in_either([1, 2, 3], [3, 5, 6], 3) == True


# In[ ]:


"""EXERCISE: Write a function called mymax which

inputs: a list of integers

and 

outputs: the maximum integer in the list.

NOTE: Python has a builtin function called max to do this. DO NOT USE this function!
"""


# In[ ]:


"""Test cases. If your code is correct, no errors should be thrown."""
assert mymax([66, 4, 3, 77, 1, 4, 5]) == 77
assert mymax([-3, -2, -9]) == -2
assert mymax([1]) == 1
assert mymax(list(range(99))) == 98


# In[ ]:


"""EXERCISE: Write a function called minimax which

inputs: a list of nonnegative integers

outputs: the ratio of the maximum value in the list to the minimum value in the list.

IF the minimum value in the list is zero, just return the maximum value.

Example: minimax([2, 5, 3, 8]) should return 8 / 2 = 4."""


# In[ ]:


"""Test cases. If your code is correct, no errors should be thrown."""
assert int(minimax([2, 5, 3, 8])) == 4
assert int(minimax([0, 5, 3, 8])) == 8
assert int(minimax([3, 5, 8, 100])) == 33


# In[ ]:


"""EXERCISE: Write a function called fib that

inputs: an integer n

and

outputs: the nth fibonacci number, defined by a[n] = a[n - 1] + a[n - 2] with a[0] = a[1] = 1.
"""


# In[ ]:


"""Test cases. If your code is correct, no errors should be thrown."""
assert fib(3) == 2
assert fib(7) == 13
assert fib(14) == 377


# In[ ]:


"""EXERCISE: Given the function prime below, which 

inputs: an integer

and

outputs: True if the integer is prime, else False


and a list of numbers, determine every number that is prime.

Store all prime numbers in a list called primes.
"""

from math import sqrt, floor

def prime(n):
    """Returns True if n is prime, else False."""
    for x in range(2, floor(sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True

numbers = list(range(1, 100))

# YOUR CODE HERE


# In[ ]:


"""Test cases. If your code is correct, no errors should be thrown."""
for x in primes[2:]:
    assert x % 2 == 1


# Note that functions can receive functions as input arguments!

# In[ ]:


"""EXAMPLE: The function given below

inputs: a function which inputs one integer and an integer

body: evaluates the function at the given integer

returns: the output of the input function
"""

def evaluate(func, val):
    """Evaluates the function func at the value val and returns the output.
    
    ASSUMES: func is a function with one input
             val is a valid input for func
    """
    output = func(val)
    return output

# example -- using the above function with our square function from above
output = evaluate(square, 5)
print(output)
assert output == 25


# In[ ]:


"""EXERCISE: Use the evaluate function, given above, with the function prime and the integer 1637 as inputs.

Store the outcome of evaluate in a variable called output."""


# In[ ]:


"""Test cases. If your code is correct, no errors should be thrown."""
assert output == True


# ---
# <a id="debugging"></a>
# ## 7. Debugging code
# ### [back to top](#top)
# 
# Since this notebook is already quite large, we've put a separate "Debugging" notebook on the course website under Day 07, if you want to practice debugging some code. Go check it out!

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
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "In-class assignments" folder, find the appropriate submission folder link, and upload it there.
# 
# See you next class!

# &#169; Copyright 2023,  The Department of Computational Mathematics, Science and Engineering at Michigan State University
