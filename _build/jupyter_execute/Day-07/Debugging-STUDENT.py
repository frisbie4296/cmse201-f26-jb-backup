#!/usr/bin/env python
# coding: utf-8

# # Practice with Debugging

# ## 1: Debugging

# <img src="http://imgs.xkcd.com/comics/fixing_problems.png" width=300px>

# Getting code to run perfectly the first time is nearly impossible, even for people with years of experience. Therefore debugging is a very important skill all programmers need to have, regardless of what they are doing or how much experience they have. While it sounds intimidating, the process of debugging can actually be broken down to three simple steps:  
# 
# 1. Locate where the bug is occurring
# 2. Figure out what is causing the bug
# 3. Fix the bug
# 
# Luckily for us, the errors we see in Jupyter try their best to solve the first two steps for us! Take a look at the below example:

# In[ ]:


for i in range(3)
    i_squared = i * i
    print(i_squared)


# The error here is telling us that it thinks the issue is at the end of the for loop, so we'll start by looking there. Step one done!  
# 
# Now we'll try to figure out what is causing the bug. Here, the error is telling us that it is a **syntax error**. That usually means we have a typo somewhere. Maybe we forgot something in our for loop?  
# 
# After looking closely, it turns out that we did forget something -- the colon at the end. After fixing that, our code runs without a problem!

# In[ ]:


for i in range(3):
    i_squared = i * i
    print(i_squared)


# Sometimes it's hard to understand what Jupyter is trying to tell you when it gives you an error. If you're ever unsure, it can be really helpful to just copy and paste the error into Google. This can lead you to helpful forums and documentation. No matter what the error is, someone else has almost always had the same issue.  
# 
# Another helpful strategy is to run your code in sections to find where the error is occurring. Take the example from before. Try commenting out each line one at a time and rerunning your code. (Note that when commenting out the top line you'll have to add a line that assigns the variable i to some number) The error goes away after commenting out which line?

# In[ ]:


for i in range(3)
    i_squared = i * i
    print(i_squared)


# Now you've manually **located where the bug is occurring**. Now you know where to look to figure out what you need to fix. Again, you can see that you forgot a colon at the end of your for-loop, so you know **what is causing the bug**. Now you can easily **fix the bug**!

# #### Now it's your turn!
# Below are several examples with common errors. Practice using the three steps outlined above, as well as the debugging strategies, to make the following cells run. 

# In[ ]:


# First load in libraries. Did we forget to include something?
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


my_indices = [1.0, 2.0, 3.0, 4.0, 5.0]
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# get even numbers
my_even_indices = my_indices * 2
for index in my_indices:
current_number = my_list(index)
print(current_number)


# In[ ]:


x = np.array(1, 2, 3, 4, 5, 6)
y = np.array(1, 2, 3, 4, 5)


# In[ ]:


# print two arrays from 1 to 10
a = np.linspace(1, 10, 1)
print(a)
b = np.arrange(1, 10, 1)
print(b)


# In[ ]:


# References previous cell
plt.plot(x, y, 'r')
plt.title(Straight Line)
plt.xlable(x values)
plt.ylable(yvalues)

# We want this to be plotted in another figure. Also make it bigger if you can!
plt.scatter(x[3:7], y[3:7], 'r')
plt.xlabel("X-Values")
plt.ylabel("Y-Values")
plt.title(Practice Plot)
grid()


# In[ ]:


my_list = ()

for i in range(10)
    a = i + (i - 1)
    my_list.append(i / a)
    
Print(my_list)


# In[ ]:


## This may not have a specific error, but we don't want all of those lists! 

suits = ['A','B','C','D']
numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # 1 is ace, 11 12 13 are jack queen king
cards = []
for suit in suits:
    for num in numbs:
        cards.append(suit + str(num))
        print(cards)


# In[ ]:


for i in range(-10, 10):
    fraction = i / (i ** 2)
    print(fraction)


# In[ ]:


# We want to print out all four sounds

cat = 10
dog = 5
cow = 1
elif cat > dog
print('Meow!)
      if dog > pig 
       print('Woof!')
      if pig < cat < dog
          print('Oink!')
          if cow = pig
              print('Moo!')


# In[ ]:


sum_of_squared_values = 0
while i < 10
squared_list = []
squared_list.append[i * i]
sum_of squared_values == i * i
if i * i = i
print("I'm number one!")


# ---
# # 2. More debugging
# 
# ## More bug examples

# The cells below each contain code that, when run, will throw an error. For each of the following:
# 1. Describe what you think the code *should* be doing
# 2. What error message are you getting? What does that error message mean?
# 3. How could the code be corrected so that it will run without throwing an error *and* perform the task that you think it should be?
# 4. Try copying and pasting the code into a new cell and correcting it as you outlined in the above question.
# 
# Be sure to answer all of the questions for each piece of code.

# *Code Sample 1:*

# In[ ]:


B = [range(100)]
B[10]


# <font size=8 color="#009600">&#9998;</font> Do This - Erase the contents of this cell and replace it with your answer to the above questions (1-4)!  (double-click on this text to edit this cell, and hit shift+enter to save the text)

# In[ ]:


##Put your code here


# *Code Sample 2:*

# In[ ]:


##You may need to google the formula for standard deviation if it's something that you aren't familiar with
##But knowledge of the formula is not required to fix the bug
def mean_and_standard_deviation(data):
    mean = sum(data)/len(data)
    variance = 0
    for entry in data:
        variance += (data - mean)**2
    variance /= len(data)
    return mean, variance **(1/2)

D = [3.2, 7.8, 1.11, 10.98, 13.4, 8.8]

mean_and_standard_deviation(D)


# <font size=8 color="#009600">&#9998;</font> Do This - Erase the contents of this cell and replace it with your answer to the above questions (1-4)!  (double-click on this text to edit this cell, and hit shift+enter to save the text)

# In[ ]:


##Put your code here


# ## Bugs that don't break your code
# 
# The cells below each contain code that will run, but the result will not be correct (broken but not breaking). For each of the examples:
# 1. Describe what you think the code *should* be doing.
# 2. How do you know that the result of the code is incorrect?
# 3. How could the code be corrected so that it will run as expect it to?
# 4. Try copying and pasting the code into a new cell and correcting it as you outlined in the above question.
# 
# Be sure to answer all of the questions for each piece of code.

# *Code Sample 3:*

# In[ ]:


num = 32
if num > 1:
    for i in range(1,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is", num)
            break
    else:
        print(num, "is a prime number")


# <font size=8 color="#009600">&#9998;</font> Do This - Erase the contents of this cell and replace it with your answer to the above questions (1-4)!  (double-click on this text to edit this cell, and hit shift+enter to save the text)

# In[ ]:


##Try to put the correct code here


# *Code Sample 4:*

# In[ ]:


def factorial(num):
    factorial = 0
    for i in range(1, num + 1):
        factorial = factorial + i
    print("{}! =  {}".format(num, factorial))
    
factorial(2)
factorial(3)
factorial(4)


# <font size=8 color="#009600">&#9998;</font> Do This - Erase the contents of this cell and replace it with your answer to the above questions (1-4)!  (double-click on this text to edit this cell, and hit shift+enter to save the text)

# In[ ]:


##Try to put the correct code here


# ---
# # 3. Continuing to debug code
# 
# ## Even more bug examples!

# ### Fixing errors
# 
# **Question**: Resolve the errors in the following pieces of code and add a comment that explains what was wrong in the first place.

# In[ ]:


for i in range(10)
    print("The value of i is %i" %i)


# In[ ]:


def compute_fraction(numerator, denominator):
    fraction = numerator/denominator
    print("The value of the fraction is %f" %fraction)
    
compute_fraction(5, 0)


# In[ ]:


def compute_fraction(numerator, denominator):
    fraction = numerator/denominator
    print("The value of the fraction is %f" %fraction)
    
compute_fraction("one", 25)


# In[ ]:


import numpy as np

n = np.arange(20)
print("The value of the 10th element is %d" %n(9))


# In[ ]:


odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]

for i in odd:
    print(i)
    
for j in evven:
    print(j)


# In[ ]:


spanish = dict()
spanish['hello'] = 'hola'
spanish['yes'] = 'si'
spanish['one'] = 'uno'
spanish['two'] = 'dos'
spanish['three'] = 'tres'
spanish['red'] = 'rojo'
spanish['black'] = 'negro'
spanish['green'] = 'verde'
spanish['blue'] = 'azul'

print(spanish["hello"])
print(spanish["one"], spanish["two"], spanish["three"])
print(spanish["orange"])

