#!/usr/bin/env python
# coding: utf-8

# # Day 6 In-class Assignment: Using functions for fun and profit!
# 

# ### <p style="text-align: right;"> &#9989; Put your name here.
# <p style="text-align: right;"> &#9989; Put your group member names here.

# <img src="http://3p76s62sopuo2hcrwa1rxucp.wpengine.netdna-cdn.com/wp-content/uploads/uber-cover-car-hailing.png" width=400px>
# 
# As we've mentioned previously, writing functions in Python can be _very_ useful. In this assignment, you'll spend some more time writing functions so that it starts to become second nature. If you get into the habit of writing functions early on, you'll find that you start writing more efficient code as the problems you're trying to solve get more complicated!
# 
# In this assignment, we'll use functions to compute distances and optimize rideshare routes.

# ## Learning Goals:
# 
# By the end of this assignment you should be able to:
# 
# * Confidently write and execute functions in Python using varying numbers of input parameters, default parameters, and returned values

# ---
# ## Part 1: Revisiting the last function from the pre-class assignment
# 
# In your pre-class assignment, you were asked to do the following:
# 
# 1. Write a function called `x_squared`.
# 2. The function should take in a list of $x$-values of any length, but should have a default of [1,2,3].
# 3. The function should return a new list of values that are $x^2$ values of the original input values.
# 4. Print the resulting new list.
# 
# Hopefully you were able to figure this out, but if not here's one possible solution:

# In[ ]:


def x_squared(x_values=[1,2,3]):
    x_sq = []
    for x in x_values:
        x_sq.append(x**2)
        
    return x_sq


# In[ ]:


x2 = x_squared()
print(x2)


# Notice that when the function is called, **it doesn't take any input and yet produces an output**. This is the upside to defining a default value for the input. Of course, I can also make the $x$-values to be anything I want. Like so:

# In[ ]:


x = [3, -5, 10, -6, -7, 2]
x2 = x_squared(x)
print(x2)


# ---
# ## Part 2: Computing distances with functions
# 
# <div align="center"><img src="https://i.imgur.com/FrMebl0.png" width=300px></div>
# <div style="text-align: center"> Anything look familiar about this map? </div>
# <br>
# 
# 
# For the next part of this assignment, we're going to think about how we might be able to write functions that can be used to compute distances on a map.
# 
# ### Part 2.1: Computing the Euclidean distance
# 
# "Euclidean distance" is simply the distance of the straight line that connects two points in Euclidean space. It's basically the distance "as the crow flies". On a map, it might look something like this:
# 
# <div align="center"><img src="https://i.imgur.com/KSmguA5.png" width=500px></div>
# <div style="text-align: center"> </div>

# Recall that, for two points defined as $(x_1, y_1)$ and $(x_2, y_2)$, the Euclidean distance is given by:
# 
# $$d = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2} $$
# 
# ### 2.1.1 Plan out your code: Euclidean distance
# 
# &#9989;&nbsp; **As a group**, design a function called `calc_euc_dist` that calculates the *Euclidean distance* between two points. **Use the `x-squared` function above as a starting point.** Your function should take a **starting point and a stopping point as input variables** and **return** the distance estimate. Don't worry about the units of this distance for this problem.
# 
# You and your groups members are expected to **use your whiteboard**. 
# 
# *Things to think about:*
# - What value(s) will your function take?
# - Will you use any default values?
# - How will you translate the mathematical expression for the Euclidean distance into code?
# - What value(s) will your function return?

# <font size="+3">&#9998;</font> *Write your plan here*

# ## &#128721; STOP AND ASK YOUR INSTRUCTOR TO COME OVER AND CHECK YOUR PLAN

# ### 2.1.2 Translate your plan into code: Euclidean distance
# 
# &#9989;&nbsp; Translate your plan from the previous problem into a function that calculates the Euclidean distance between two points.
# 
# **Work with your group to figure this out!**

# In[ ]:


# Put your function here


# ### 2.1.3 Test your code: Euclidean distance
# 
# &#9989;&nbsp; **Make up some $x$ and $y$ values, plug them into your function, and make sure your code works correctly.** (*How will you know if your code is running correctly?*)

# In[ ]:


# Put your test code here


# ### Part 2.2: Computing the "Lyft" distance
# 
# For this part of the assignment, let's say that you've been thinking about starting a new rideshare company similar to Uber or Lyft. You've started thinking about how you should go about estimating the amount you should charge for a given ride, but you've realized that computing the Euclidean distance between two points doesn't really make sense. Now you need to create a new function that computes an estimate for the total distance of the ride for your new "Lyft-like" service.
# 
# When you're driving a car you can't just travel in a straight line between two points, you're forced to drive along the grid structure defined by where the streets are. Your path might look something like this:
# 
# <div align="center"><img src="https://i.imgur.com/ieJ1Z4k.png" width=500px></div>
# <div style="text-align: center"> Another potentially familiar place... </div>
# <br>
# 
# For the purposes of computing these new "Lyft"-like distances, you're going to assume that the drivers for your company are generally pretty good about taking the shortest possible route, and you're also going to assume that, most of the time, the streets will have a pretty standard grid-like structure. After all, it would be pretty hard to predict just how irregular the routes might end up being.

# ### 2.2.1 Plan out your code: Lyft Distance
# 
# &#9989;&nbsp; **As a group**, design a function called `calc_lyft_dist` that calculates the *Lyft distance* between two points. Your function should take a **starting point and a stopping point as input variables** and **return** the distance estimate. Your estimate will essentially tell you how many blocks the driver will travel to get to the destination.
# 
# You and your groups members are expected to **use your whiteboard**. 
# 
# *Things to think about:*
# - What value(s) will your function take?
# - Will you use any default values?
# - How will you calculate the Lyft distance?
# - What value(s) will your function return?

# <font size="+3">&#9998;</font> *Write your plan here*

# ### 2.2.2 Translate your plan into code: Lyft distance
# 
# &#9989;&nbsp; Translate your plan from the previous problem into a function that calculates the Lyft distance between two points.
# 
# **Work with your group to figure this out!**

# In[ ]:


# Put your function here


# ### 2.2.3 Test your code: Lyft distance
# 
# &#9989;&nbsp; **Make up some $x$ and $y$ values, plug them into your function, and make sure your code works correctly.** (*How will you know if your code is running correctly?*)

# In[ ]:


# Put your test code here


# ### 2.3 Creating a fare-computing function
# 
# Let's assume that you want to be able to quickly calculate an estimate for the cost of the trip so that you can let your riders know roughly how much you'll charge them.  To start with, you're going to use a flat rate of **40 cents** per unit distance the driver travels.
# 
# &#9989;&nbsp; **Write another function** called `trip_cost` that **uses the function you just wrote** for computing the total distance of the ride to ***print* the cost of the trip** so that it reads "The cost of the trip will be $< amount >" where < amount > is the total in dollars that the trip will cost. Your function should take the starting point, the stopping point, and the rate (with a default value) as inputs.

# In[ ]:


# Put your function here


# ---
# ## Part 3: Combining your functions
# 
# Now that you've written two different functions for finding the distance, you're thinking that it would be more convenient if you could use the same function to compute both the Euclidean distance and the Lyft distance. It would also make it a lot easier to compare how much longer the Lyft distance is than the Euclidean distance.
# 
# &#9989;&nbsp; **Write a function** that is capable of computing the Euclidean distance **or** the Lyft distance based on a keyword argument call `path_type`. 
# * If the `path_type` is 'Lyft', compute the Lyft distance, otherwise compute the standard Euclidean distance.
# * Make sure that the default stopping point is (0,0).
# 
# As before, your function should **return** the distance.

# In[ ]:


# Put your code here


# &#9989;&nbsp; **Write another function** that **uses your previous function** to compute both the Euclidean distance and the Lyft distances and **prints**:
# 
# "The Lyft distance is < X > times longer than the Euclidean distance"
# 
# where < X > is the appropriate ratio of the two distances.
# 
# **Compare the two distances** for a starting point of (-2, -6) and stopping point of (4,5).

# In[ ]:


# Put your code here


# ---
# ### &#128721; STOP
# Good work so far! Check in with your instructor regarding your progress so far and see if you have enough time left to continue with today's assignment.

# ---
# ## TIME PERMITTING: Planning your route
# 
# Now that you've worked out a system for estimating travel distances and ride fares, you're ready to start testing your new rideshare service. You fire up your fancy new program and immediately get three simultaneous rider requests, but luckily they all are looking for a ride to the same place -- the airport!
# 
# You plan on picking up all three passengers on the **same trip** so that you can drop them all off at the same time. You want to take the shortest possible route so that you minimize the cost of gas and, in turn, the amount of money the trip costs you!
# 
# **The challenge**: You need to create a function that takes in a starting position, a list of three rider locations, and a stopping location and determines the order of rider pickups that will require the least amount of driving. You want to make the default stopping location be the airport, since you figure this is where people will be headed most often. You should be able to use your function for computing the Lyft distance to help solve this problem.
# 
# ### You are expected to work out a plan for your function on your whiteboard! You may need to draw a diagram to figure out how to solve this.
# 
# Once you've come up with a plan, try **writing the function**. The function should **return the list of rider locations in the appropriate pick-up order and the total distance of the trip**.
# 
# Let's assume that:
# 
# 1. Your starting location is (-2,3).
# 2. The ride locations are (-1, -2), (3,3), and (2, -1).
# 3. The stopping location, the airport, is at (4,0).
# 

# In[ ]:


# Put your code here


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
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "In-class assignments" folder, find the appropriate submission link, and upload it there.
# 
# See you next class!

# &#169; Copyright 2021,  Michigan State University Board of Trustees
