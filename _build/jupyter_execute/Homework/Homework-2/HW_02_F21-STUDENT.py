#!/usr/bin/env python
# coding: utf-8

# # Homework 2: If Statements, Functions, and Modules

# ### <p style="text-align: right;"> &#9989; **Put your name here** </p>

# # __CMSE  201 &ndash; Fall 2021__
# 
# <img src="https://cmse.msu.edu/sites/_cmse/assets/Image/image002.jpg"
#      alt="CMSE Logo"
#      align="right" 
#      height="100" 
#      width="100" />
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

# ## Assignment instructions
# 
# Work through the following assignment, making sure to follow all the directions and answer all the questions.
# 
# **This assignment is due at 11:59 pm on Friday, October 1st.** It should be uploaded into the "Homework Assignments" submission folder for Homework #2.  Submission instructions can be found at the end of the notebook.

# ---
# ## Grading
# 
# * Part 1: Designing a Zoo Layout (7 points)
#     * 1.1: (2 points)
#     * 1.2: (5 points)
# * Part 2: Functions (20 points)
#     * 2.1: Backpacking in Europe (10 points)
#     * 2.2: Stock Prices (10 points)   
# * Part 3: Modules and matplotlib (12 points)
# 
# Total points possible: **40**
# 
# ---

# # ---
# # Academic integrity statement (1 point)
# 
# In the markdown cell below, put your personal academic integrity statement (composed during the Day04 In-Class Assignment). By including this statement, you are confirming that the work you submit in the assignment is wholly your own.  

# <font size=6 color="#009600">&#9998;</font> *Put your personal academic integrity statement here.*

# <img src="https://www.jbzoo.org/uploads/images/JBZ_Summer2021_MapWebFINAL.jpg"
#      alt="John Ball Zoo, Grand Rapids, MI"
#      align="center" 
#      height="800" 
#      width="800" />

# ## Part 1: Designing a Zoo Layout
# 
# You are working with a team to redesign a zoo layout. The designers have decided that the zoo will be divided into sections based on the continent the animals are found on and their habitats. You have the data table below containing the species name, continent, and if their habitat requirements are primarily water, primarily flying, or primarily land.
# 
# 
# | Species | Continent | Water Habitat | Flying Habitat | Land Habitat |
# | :----- | :----- | :------ | :----- | :----- |
# | River Otter | North America | Yes | No  | No  |
# | Viscacha | South America | No | No | Yes  |
# | Emperor Penguin | Antarctica | Yes | No  | No |
# | Toco Toucan | South America | No | Yes | No |
# | Lion | Africa | No | No  | Yes |
# | Platypus | Australia | Yes | No | No |
# | Pink Flamingo | Europe | No | Yes | No |
# | Binturong | Asia | No | No | Yes |
# | Grizzly Bear | North America | No | No | Yes |

# ### 1.1 Making Lists (2 points)
# 
# &#9989;&nbsp; In the cell below, create a list of lists that contains all of the data in the table above. The structure of the list should be `animal_data = [list0, list1, list2,...]` with as many entries as rows. Each list in `animal_data` is the information for one animal. For example, `list0` would contain all of the information about the river otter (`list0 = ['River Otter', 'North America','Yes','No','No']`).

# In[102]:


# put your code here


# ### 1.2 Categorizing Animals
# 
# &#9989;&nbsp; Loop through your list from part 1.1 with a `for` or `while` loop, and using appropriate `if/elif/else` statements, determine the region and habitat for each animal in the zoo and print them out as a string.
# 
# For example, for _River Otter_ your loop should print `River Otter is in the North America Region in a primarily Water Habitat`.
# 
# **Note:** Your solution should use the information in the Contintent/Water Habitat/Flying Habitat/Land Habitat along with appropriate `if/elif/else` statements. 

# ### 1.2.1 Pseudocoding (2 points)
# 
# &#9989;&nbsp; Write out your plan for how you will write your code to solve the problem in the cell below.

# In[104]:


# put your pseudocode here


# ### 1.2.2 Now turn your pseudocode in to code! (3 points)
# 
# &#9989;&nbsp; In the cell(s) below, write out your solution. Don't forget to use code comments where appropriate!

# In[106]:


# put your code here


# ## Part 2: Functions

# ## 2.1 Backpacking in Europe
# 
# You and your friends are trying to plan a backpacking trip to Europe, but all of the information you can find is in metric units (meters, liters, kilograms) and your friends are only familiar with imperial units (feet, gallons, pounds). However, you remember that you know python and can write yourself a tool to convert units as necessary!

# ### 2.1.1 (2 points)
# 
# &#9989;&nbsp; In the cell below, write a separate calculation for converting liters to gallons, meters to feet, and kilograms to pounds. You should use the internet to determine the values for conversion. **Test your conversions by converting 2 liters to gallons, 5000 meters to feet, and 150 kilograms to pounds.**
# 
# For example, there are 3600 seconds in one hour, so to convert from hours to seconds, you need to multiply the number of hours by 3600.
# 
# `hours = 4
# seconds_in_an_hour = 3600
# time_in_seconds = hours*seconds_in_an_hour
# print(time_in_seconds)`

# In[108]:


# put your code here


# ### 2.1.2 (2 points)
# 
# While it's pretty easy to do multiplication in python, it's rather slow to have to type a new equation every time, so to make things faster for you and your friends, you will write a function that takes in the metric value and returns the imperial value. 
# 
# &#9989;&nbsp; In the cell below, write a function to calculate the conversion of liters to gallons.

# In[110]:


# put your code here


# ### 2.1.3 (5 points)
# 
# To make your conversion tool the most useful by all of your friends, you need to expand your function to calculate the conversions for meters and kilograms as well. Your function should be able to take a value and its metric units and return the imperial units.
# 
# &#9989;&nbsp; In the cell below, plan out your function using pseudocode.

# In[112]:


# put your pseudocode here


# &#9989;&nbsp; In the cell below, write your function. Feel free to add additional cells if necessary.

# In[114]:


# put your code here


# ### 2.1.4 Checking your work (1 point)
# 
# &#9989;&nbsp; In the cell below, demonstrate that your code works as you intend with words and code examples.

# In[116]:


# put your explanation here


# ## 2.2 Tracking Stock Prices
# 
# You are investing in the stock market, and you want to keep an eye on the stocks that are **increasing or decreasing** the most over time. To do this, you will **write a function** to calculate the percent difference between open and close each day and plot it. 
# 
# Percent difference can be calculated by $\% \ difference = \frac{(close-open)}{open}$

# ### 2.2.1 Understanding Percent Difference (1 point)
# 
# In your own words, describe what the percent difference tells you about data. **Hint:** What does it mean if the percent difference is large? What about if it is small?

#  <font size="+3">&#9998;</font> *Put your answer here*

# ### 2.2.2 Planning (1 point)
# 
# &#9989;&nbsp; In the cell below write out your plan for your percent difference function.

# In[118]:


# put your pseudocode here


# ### 2.2.3 Developing your function (5 points)
# 
# &#9989;&nbsp; In the cell below, write your percent difference function and test it using the test data. Feel free to add additional cells as needed.

# In[120]:


# test data
test_open = [40,42,48,36,40,45]
test_close = [41,46,37,38,44,45,42]
test_days = list(range(len(test_open)))


# In[121]:


#put your code here


# ### 2.2.4 Checking your work (1 point)
# 
# &#9989;&nbsp; In the cell below, demonstrate that your function works with code and exmaples.

# In[123]:


# put your explanation here


# ### 2.2.5 Plotting Data (2 points)
# 
# &#9989;&nbsp; Using your function, calculate the daily percent difference for the stock data below and plot your results.

# In[125]:


# Stock data source: https://eoddata.com/stockquote/NYSE/GME.htm?e=NYSE&s=GME
daily_open = [19.0, 17.35, 17.34, 18.47, 18.18, 19.41, 19.96, 20.42, 38.09, 38.49, 35.5, 41.55, 37.37, 39.23, 42.59, 96.73, 88.56, 354.83, 265.0, 383.17, 316.56, 140.76, 112.01, 91.19, 54.04, 72.41, 56.61, 50.77, 50.01, 50.75, 52.4, 52.99, 49.55, 48.49, 41.28, 46.69, 44.97, 44.7, 169.56, 117.46, 104.54, 116.93, 122.51, 125.0, 128.17, 154.89, 217.71, 269.43, 241.64, 275.0, 277.52, 203.16, 217.84, 214.0, 195.73, 205.26, 197.5, 157.98, 123.49, 197.68, 180.75, 187.5, 197.5, 193.36, 191.45, 171.0, 185.21, 183.22, 185.88, 169.7, 158.11, 141.88, 143.57, 163.0, 156.0, 171.8, 164.14, 158.4, 159.1, 149.0, 150.98, 183.55, 172.1, 176.56, 175.0, 177.49, 159.0, 161.83, 160.86, 160.11, 161.31, 137.0, 145.7, 147.44, 160.0, 159.85, 174.54, 172.91, 170.79, 171.0, 175.85, 181.0, 229.0, 229.8, 262.97, 222.0, 233.48, 248.88, 265.71, 256.02, 258.0, 292.0, 303.12, 282.0, 222.35, 236.5, 226.36, 215.24, 224.0, 219.86, 216.95, 217.73, 221.45, 221.16, 214.0, 211.25, 213.59, 209.69, 213.4, 204.8, 202.83, 204.0, 196.0, 179.83, 190.88, 191.42, 187.68, 180.49, 160.0, 170.15, 163.14, 173.9, 187.79, 185.3, 181.0, 180.36, 183.0, 175.72, 170.6, 165.0, 162.0, 156.74, 152.73, 148.0, 154.59, 151.8, 161.36, 158.43, 159.88, 160.47, 161.0, 161.19, 163.25, 156.77, 153.8, 162.38, 166.29, 206.65, 200.68, 207.7, 205.0, 212.7, 224.0, 213.86, 212.05, 206.25, 201.86, 180.09, 198.41, 193.75, 200.65]
daily_close = [17.25, 17.37, 18.36, 18.08, 17.69, 19.94, 19.95, 31.4, 39.91, 35.5, 35.5, 39.36, 39.12, 43.03, 65.01, 76.79, 147.98, 347.51, 193.6, 325.0, 225.0, 90.0, 92.41, 53.5, 63.77, 60.0, 50.31, 51.2, 51.1, 52.4, 52.4, 49.51, 45.94, 40.69, 40.59, 46.0, 44.97, 91.71, 108.73, 101.74, 120.4, 118.18, 124.18, 132.35, 137.74, 194.5, 246.9, 265.0, 260.0, 264.5, 220.14, 208.17, 209.81, 201.75, 200.27, 194.49, 181.75, 120.34, 183.75, 181.0, 181.3, 194.46, 189.82, 191.45, 191.45, 186.95, 184.5, 177.97, 170.26, 158.36, 141.09, 140.99, 166.53, 156.44, 154.69, 164.37, 158.53, 158.51, 151.17, 151.18, 168.93, 177.77, 178.58, 176.19, 173.59, 162.2, 160.73, 159.48, 161.01, 161.11, 143.22, 146.92, 144.79, 164.5, 159.92, 180.6, 180.67, 168.83, 170.49, 176.79, 180.01, 209.43, 242.56, 254.13, 222.0, 222.0, 249.02, 282.24, 258.18, 248.36, 280.01, 300.0, 302.56, 220.39, 233.34, 229.44, 222.5, 222.97, 223.59, 213.82, 200.37, 220.4, 219.34, 212.31, 209.51, 213.25, 210.88, 214.14, 204.36, 202.83, 202.83, 199.56, 190.66, 191.38, 191.23, 189.25, 180.06, 167.62, 166.82, 169.04, 173.49, 191.18, 185.81, 178.85, 180.36, 183.94, 178.54, 169.12, 164.86, 161.12, 157.65, 152.75, 146.8, 153.44, 151.77, 161.13, 159.05, 158.78, 162.35, 162.52, 163.93, 163.55, 157.05, 152.9, 159.3, 164.89, 210.29, 199.65, 205.22, 204.95, 209.2, 218.24, 212.97, 213.52, 202.75, 199.0, 198.8, 199.18, 190.41, 203.4, 199.24]
days = list(range(len(daily_open)))


# In[126]:


# put your code here


# ### 2.2.6 Making Observations (1 point)
# 
# &#9989;&nbsp; In 2.2.1, you provided reasoning for what percent difference calculations tell us about data. Given what you now know about percent differences, make observations about the percent difference measurements over time in your plot and describe anything you find particularly notable.

#  <font size="+3">&#9998;</font> *Put your answer here*

# ## Part 3: Modules and Plotting

# ### 3.1 Modules (2 points)
# The math module contains the basic trigonometric functions (sine, cosine, tangent, arcsine, arcosine, arctangent, etc.). 
# 
# &#9989;&nbsp; In the cell below, choose three of the trigonometric functions and generate x and y values for each. You should use the `math` module and/or the `numpy` module.

# In[129]:


# put your answer here


# ### 3.2 Plotting (2 points)
# 
# &#9989;&nbsp; In the cell below, make a plot for one of your trigonometric functions. Make sure to include axis labels, a title, and a legend.

# In[131]:


# put your answer here


# ### 3.3 Streamlining plots
# 
# In CMSE 201, you will be making plots often. To help future you save time, you are going to write a function to use when you make plots!
# 
# ### 3.3.1 (6 points)
# &#9989;&nbsp; In the cells below, write a function that takes the x and y values from all three of your trigonometric functions above and appropriate labels and returns a plot with a panel for each trigonometric function. You should use plt.subplot() and make use of labels, line shapes, and colors to make your plots clear. **You must also test your function to receive full credit**

# In[133]:


# put your answer here


# ### 3.4 Making your plotting function more flexible (2 points)
# 
# &#9989;&nbsp; In the cell below, look at your function from 3.3 and write in words and/or pseudocode how you might change it to handle any number of subplots.

# In[136]:


# put your answer here


# ---
# ## Assignment Wrap-up
# 
# Please fill out the following Form before you submit your assignment. **You must completely fill this out in order to receive credit for the assignment!**
# 
# **COMPLETE THIS SURVEY through [this link](https://forms.office.com/Pages/ResponsePage.aspx?id=MHEXIi9k2UGSEXQjetVoffh-a-g_jQVGqbV9Nr124R5UOEVGM1Y1Wjc4NDdGTDAwTFRVTTVSVkFBWi4u) or through cell below.**
# 

# In[137]:


###update this for homework 2
from IPython.display import HTML
HTML(
"""
<iframe 
	src="https://forms.office.com/Pages/ResponsePage.aspx?id=MHEXIi9k2UGSEXQjetVoffh-a-g_jQVGqbV9Nr124R5UOEVGM1Y1Wjc4NDdGTDAwTFRVTTVSVkFBWi4u" 
	width="80%" 
	height="1200px" 
	frameborder="0" 
	marginheight="0" 
	marginwidth="0">
	Loading...
</iframe>
"""
)


# ---
# 
# ### Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "Homework Assignments" section, find the submission folder link for Homework #2, and upload it there.
