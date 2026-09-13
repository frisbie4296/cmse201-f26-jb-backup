#!/usr/bin/env python
# coding: utf-8

# # Homework 2: If Statements, Functions, and Modules

# ### <p style="text-align: right;"> &#9989; **Put your name here** </p>

# # __CMSE  201 &ndash; Spring 2022__
# 
# <img src="https://cmse.msu.edu/sites/_cmse/assets/Image/image002.jpg"
#      alt="CMSE Logo"
#      align="right" 
#      height="100" 
#      width="100" />
# 
# 
# 
# ## Learning Goals
# 
# ### Content Goals
# - **Use if/elif/else statements to implement a logical flow**
# - **Write and execute functions**
# - **Use the python math module**
# - **Display data on plots using matplotlib**
# 
# 
# ### Practice Goals
# - **Commenting code**
# - **Using functions to build reusable/transferable code**
# - **Use visualization best practices to make informative plots**
# 
# 
# ___

# ## Academic integrity statement (1 Point)
# 
# In the markdown cell below, paste your personal academic integrity statement. By including this statement, you are confirming that you are submitting this as your own work and not that of someone else.
# 

# <font size=6 color="#009600">&#9998;</font> *Put your personal academic integrity statement here.*

# ## 1. Let it Snow!
# 
# While it is often assumed that a temperature of 0 &deg; C (32 &deg; F) marks the divide between rain and snow, snowfall is actually dependent on relative humidity as well as temperature [Jennings 2018](https://www.nature.com/articles/s41467-018-03629-7). High relative humidity (lots of moisture in the air) means that snowfall requires lower air temperatures than in places with low relative humidity. The table below shows the temperature (in Celsius) below which snow will fall for the corresponding range of relative humidity values. 
# 
# *Note: Values are taken from Jennings 2018 and have been rounded for ease of interpretation.* 
# 
# **Table 1: Relative Humidity and Snowfall Temperature**
# --
# |Relative Humidity Range (%)| Temperature (&deg; C)|
# |:---:|:---:|
# |90&ndash;100 |1.0|
# |80&ndash;89 |2.0|
# |70&ndash;79 |2.5|
# |60&ndash;69 |3.1|
# |50&ndash;59 |4.0|
# |40&ndash;49 |5.0|
# 
# ---
# Your task is to take the list of temperature values and determine if it will snow or rain for each relative humidity range using loops and if/else statements. Your code should create a list that contains the "Snow" or "Rain" result for all relative humidity ranges for each temperature data point. See the example output below for one temperature for more guidance.
# 
# ---

# #### Example Output:
# 
# For a temperature of 2.0 &deg;C, the resulting list should be:
# 
# `['Snow', 'Snow', 'Snow', 'Snow', 'Snow', 'Rain']`

# In[111]:


temperature = [0.0, 1.1, 3.0, 5.0, 7.5, -0.5, 0.4, 7.0, 4.3, 1.2] # temperature in degrees celsius
relative_humidity = [40, 50, 60, 70, 80, 90] #relative humidity list (optional to use)


# ### 1.1 Task (3 points)
# 
# In the cell below, write out the basic structure of your loops and if/else statements in pseudocode.

# <font size="+3">&#9998;</font> *Put your answer here*

# ### 1.2 Task (7 points)
# 
# In the cell below, translate your pseudocode into code. Include comments where needed.

# In[112]:


# put your code here


# ### 1.3 Task (2 points)
# 
# How do you know your code is working? Use words and/or code to support your answer.

# In[114]:


# put any code here


# <font size="+3">&#9998;</font> *Put any descriptions here*

# ## 2. CMSE 201 Homework Grade Calculator
# 
# As a student in CMSE 201, you may want to pay attention to your grades to have an idea of how you are doing this semester. Your task is to write a function to calculate the grade of your Homework 1 assignment. Your function should take in the score for each component, calculate the percentage grade, convert it to the 4.0 scale, and return the 4.0 scale grade. The rubric for Homework 1 is below for reference.
# 
# ---
# #### Homework 1 Rubric
# 
# Academic integrity statement (1 Point)
# 
# 0. Going to Office Hours (8 Points) 
# 1. Looping by Index (10 Points)
# 2. Looping by Value (10 Points)
# 3. Working with Lists and Dictionaries (9 Points)
# 4. Debugging Dictionary Construction (12 Points)
# 
# Total points possible: **50**
# 
# ---

# ### 2.1 Task (3 points)
# 
# In the cell below, write out your plan for your function in pseudocode. It should include the structure of your function (inputs and outputs) and how you will calculate the grade. You should use the grade information on the Course Website to determine the 4.0 scale.

# <font size="+3">&#9998;</font> *Put your answer here*

# ### 2.2 Task (3 points)
# 
# In the cell(s) below, translate your pseudocode into code. 

# In[115]:


# put your answer here


# ### 2.3 Task (3 points)
# 
# In the cell below, demonstrate that your function work correctly using words and/or code. Your explanation should in clude at least one example calculation using your function.

# In[117]:


# put any code here


# <font size="+3">&#9998;</font> *Put any descriptions here*

# ### 2.4 Task (3 points)
# 
# Suppose you wanted to generalize your function to be used for all of your CMSE 201 homework assignments. What are the limitations of this function? How might you address them to make your function more flexible?

# <font size="+3">&#9998;</font> *Put your answer here*

# ## 3. Basketball Scoring
#     
# You are in charge of writing Python code to keep score of a basketball game. You will write a function that takes in two team names, an array with the team name and an array with the type of play and returns the final score of the game.
# 
# ---
# Example output:
# 
# `MSU - 83, UMich - 67`

# ### 3.1 Task (2 points)
# 
# Write a series of if/else statements that adds 1 point to the score for free throws, 2 points for jumpers, layups, or dunks, and 3 points for three pointers. Use this lists below to write and test your function.

# In[118]:


# put your code here

points = np.array(['Layup','Jumper','Layup','Layup','Layup','Layup','Layup','Free Throw','Free Throw','Dunk','Layup','Free Throw','Free Throw','Three Pointer'])
team = np.array(['UMich','MSU','UMich','MSU','MSU','UMich','MSU','UMich','UMich','UMich','UMich','UMich','UMich','MSU'])


# ### 3.2 Task (2 points)
# 
# Now write pseudocode for how you will implement your code from above to write your function.

# <font size="+3">&#9998;</font> *Put your answer here*

# ### 3.3 Task (6 points)
# 
# Now write your function!

# In[120]:


# put your code here


# ### 3.4 Task (2 points)
# 
# Along with this homework assignment is a text file named `game.txt`. Using numpy, read in the data and then use your function to calculate the final score of the game. The data file is in the same format as the test lists given in 3.1. If you need to make any changes to your function to get it to work, explain why using code comments or additional Markdown cells.

# In[122]:


# put your code here


# ## Question 4: Drawing with matplotlib
# 
# You are taking a graphic design class, and you discovered that you can generate pretty designs on plots by using trigonometric functions and matplotlib. below are two equations that give the (x,y) points for values of k (ranging from 0 to 9000). When all 9000 points are plotted, you will see that it draws out a flower design.
# 
# $x(k) = \mathrm{cos}\Big(\frac{14 \pi k}{9000}\Big)\Big(1-\frac{3}{4}\mathrm{sin}\Big(\frac{20\pi k}{9000}\Big)-\frac{1}{4}\mathrm{cos}\Big(\frac{60 \pi k}{9000}\Big)\Big)$
# 
# $y(k) = \mathrm{sin}\Big(\frac{14 \pi k}{9000}\Big)\Big(1-\frac{3}{4}\mathrm{sin}\Big(\frac{20\pi k}{9000}\Big)-\frac{1}{4}\mathrm{cos}\Big(\frac{60 \pi k}{9000}\Big)\Big)$

# #### 4.1 Writing the Function (4 points)
# Using the starter code below, create a function that returns the values of x(k) and y(k). You can use math or numpy. 
# 
# The function `draw_flower_points` below is what you will use to generate your values to draw a flower. State the inputs and outputs of this function.

# In[124]:


# put your code here

def draw_flower_points(# add arguments here):
    # write your function here
    return x_k, y_k


# ### 4.2 Testing your function (2 points)
# 
# Using the `draw_flower_points` function above, test it out by generating a list (or array) of x values and a list (or array) of y values for k from 0 to 10 and print the results.

# In[ ]:


# put your answer here


# ### 4.3 Drawing the Flower (7 points)
# Now, using the `draw_flower_points` function, generate x and y values for k ranging from 0 to 9000. Using plt.subplot, plot the final flower design as well as at least 2 additional panels showing the drawing in progress (i.e. for values of k less than 9000). 
# 
# Your plot should include:
# * at least 3 total panels
# * axis labels (label the x-axis 'x' and the y axis 'y')
# * a legend
# * different linestyles for each panel
# * different line color for each panel

# In[ ]:


# put your answer here


# ---
# 
# ### Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "Homework Assignments" section, find the submission folder link for Homework #2, and upload it there.

# In[ ]:




