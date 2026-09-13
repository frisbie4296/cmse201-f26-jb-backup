#!/usr/bin/env python
# coding: utf-8

# # Day 20 In-class Assignment: Random Walks

# ### <p style="text-align: right;"> &#9989; Put your name here.</p>
# 
# #### <p style="text-align: right;"> &#9989; Put your group member names here.</p>

# <img src="https://upload.wikimedia.org/wikipedia/commons/3/39/Random_walk_in2D_closeup.png" width=400px>
# 
# ## Goals for today's In-Class assignment
# 
# * Model a random walk
# * Learn about the behavior of random walks in one and two dimensions
# * Plot both the distribution of random walks and the outcome of a single random walk 
# 
# ## Assignment instructions
# 
# Work with your group to complete this assignment. Instructions for submitting this assignment are at the end of the notebook. The assignment is due at the end of class.

# ---
# ## Random Walks: What and Why?
# 
# Random walks are a great first step towards modeling dynamical systems in which there is a random component.  They are a very simple model of randomness:
# 
# * **Flip a coin**
# * **If heads: step to the left**
# * **If tails: step to the right**
# * **Repeat**
# 
# **Here we will run random walk simulations, study their properties, and see how they can be used to model diffusion in real systems.** But, random walks like this are used to model a wide range of systems, including financial markets, biochemical reaction networks, atomic-scale motions, and much more. 
# 
# In many situations, it is very useful to think of processes with randomness as a succession of random steps.  This can describe a wide variety of phenomena - the behavior of the stock market, models of population dynamics in ecosystems, the properties of polymers, the movement of molecules in liquids or gases, modeling neurons in the brain, or in [building Google's PageRank search model](http://www.math.cmu.edu/~pmelsted/papers/pagerank.pdf).  This type of model is known as a ["random walk"](https://en.wikipedia.org/wiki/Random_walk), and while the process being modeled can vary tremendously, the underlying process is simple.  In this project, we are going to model such a random walk and learn about some of its behaviors!

# ## Diffusion of particles

# ![Brown](https://upload.wikimedia.org/wikipedia/commons/c/c2/Brownian_motion_large.gif)

# Random walks are sometimes used to model [Brownian motion](https://en.wikipedia.org/wiki/Brownian_motion), which referred originally to the motions of a single grain of pollen suspended in a liquid solution.  But even though this process looks extremely chaotic, the average behavior of diffusing particles can be precisely determined.
# 
# One question we can ask is: **how far away from my starting point do I get?**.  This, unsuprisingly, depends on time.  The longer we randomly walk for, the farther we get from our starting point.  The "Einstein diffusion relation" was derived using some fancy mathematics, and it states that our average squared distance from the starting point increases ***linearly*** with time:
# 
# $\overline{d(t)^2} = 6Dt$
# 
# where $\overline{d(t)^2}$ is the squared distance from the starting position measured at time $t$, averaged over a set of observations. $D$ is a constant called the diffusion coefficient: the higher $D$ is, the faster we diffuse around.
# 
# **Today we are going to code random walks and test their ability to model the behavior of diffusive particles.**

# ---
# 
# ## Part 1:  One-dimensional random walk.
# 
# 
# Let's start with the simplest case: a 1D random walk; that is, a random walk on a line.
# 
# Imagine that you draw a line on the floor, with a mark every foot.  Have a group member start in one spot of the line (the point you have decided is the "origin", at $x=0$).  You then flip a coin 10 times.  Every time the coin comes up heads, you take one step to the right (in the + direction).  Every time it comes up tails, you take a step to the left (in the - direction).  

# If you don't have an actual coin, use the code below:

# In[ ]:


import numpy as np
coin_sides = ['heads','tails']
flip = 0


# In[ ]:


flip += 1
print("Flip",flip,"is",np.random.choice(coin_sides))


# ### 1.1
# 
# &#9989;&nbsp; **Record each coin flip below as well as your final distance from the origin**

# / your flips here /

# ___
# **Now it's time to automate this!  As a group you will try to answer the following questions:** 
# 
# * After $N_{flips}$ coin flips and steps, how far are you from the origin, on average?
# * If you repeat this experiment $N_{trial}$ times, what will the distribution of distances from the origin be, and what is the mean distance that you go from the origin?  (Note: "distance" means the absolute value of distance from the origin!)
# 
# ### 1.2
# 
# &#9989;&nbsp; **First:** as a group, come up with a solution to this coding problem. You may want to used a whiteboard for this. Use a flow chart, pseudo-code, diagrams, or anything else that you need to get started.  Check with an instructor before you continue! **Make sure you come up with a plan for not only how you are going to code your random walk, but how you will keep track of every new trial/walk you run.**
# 
# **Note**: Once you've drafted your plan, we're going to pursue one possible path toward a solution in the rest of the notebook, this may be different than how you planned it out. If this is the case, think about how the content below compares to the plan you came up with and reflect on which option you like more and why.

# ### Coding up a solution
# 
# ### 1.3
# &#9989;&nbsp; **After checking in with your instructors**: try individually writing a function, called `step1d`, with no inputs that creates a random integer, 1 or 0 (heads or tails), and then **returns** instructions to take a step either left or right, which means that it should return -1 or +1.  Call the function a few times and print out the value it returns to make sure it works - we'll use this as the basis of our random walk model. 
# 
# **Check with others in your group to compare their method for writing the step function to yours. If you get stuck on something, ask your group for help!**

# In[ ]:


# put your code here.  


# ### 1.4
# 
# &#9989;&nbsp; Now, **as a group** write a code in the space provided below to do a **single** random walk with $N_{step} = 1000$ using the function you have created.  You'll start at $x=0$ and take $N_{step}$ consecutive steps to the right or left. At the end print the value of $x$ (the final location of the particle).  Where did your particle go?  Run it a couple of times to see how this changes.

# In[ ]:


# put your code here.  


# Okay, great!  But, it would be much better if we could visualize what is happening.
# 
# ### 1.5
# &#9989;&nbsp; **Copy the code from above and modify it to keep track of the number of steps and your distance from the origin after each step, and plot it!**  (**Hint:** start with empty arrays or lists, and append to them.)  Run this a couple of times to see how it changes. You should get something that ends up looking like this (with variations from randomness):
# 
# <img src="https://raw.githubusercontent.com/msu-cmse-courses/cmse201-S21-student/master/assets/img/distance_v_steps_randomwalk.png" width=400px>
# 
# 

# In[ ]:


# put your code here.  


# Now, we want to see how several of these trajectories look at the same time.
# 
# ### 1.6
# &#9989;&nbsp; **So, now copy and paste your code from above and add an additional loop where you make five separate trajectories, and plot each of them one the same plot.**  There is more than one way that you could do this. You could store the trajectories using a 2D array or by creating a list composed of lists of trajectories.  Alternatively, you could all call the plot command within your loop and avoid storing the trajectories completely. The structure of the code is up to you!

# In[ ]:


# put your code here.  


# Ok.  Now we're getting somewhere.
# 
# ### 1.7
# &#9989;&nbsp; **Let's increase the number of trajectories from 5 to 1000.**  But what about all the memory that will be required to store that many trajectories? Let's be nice to our computers and not make them keep track of every single walk, just the final points.  **So, after copying and pasting your code from above, comment out the code that either saved the trajectories or plotted every walk and instead just store the final position from every random walk in a new list.** 
# 
# Once you have code that stores all of the final positions, calculate the **average squared distance** of the walk and **plot a histogram of the final positions**.

# In[ ]:


# put your code here.  


# We're almost ready to check if random walks are a good diffusion model!  All we have to do is add another layer to our loop structure.  We want to see how far the particle goes, on average, **as a function of the number of steps** (which is actually just a proxy for time, since the size of the time steps are all the same). 
# 
# ### 1.8
# &#9989;&nbsp; **Extend the code you wrote above to get the average of the square of the final position at 10 different time points (t = 100, 200, ..., 1000), and save the results to a list.**  Plot the results versus time below, and use axis labels.

# In[ ]:


# put your code here.  


# In[ ]:


# make plot here 


# ### 1.9
# 
# &#9989;&nbsp; *Put answer here.* Look at the above plot.  **Is this what you would have expected from the Einstein diffusion equation?  Why or why not?**

# <font size="+3">&#9998;</font> *Put answer here.*

# ---
# 
# ## Part 2:  Two-dimensional walk (if time allows)
# 
# Now, we're going to do the same thing, but in two dimensions, x and y. This time, you will start at the origin, pick a random direction (up, down, left, or right), and take one step in that direction.  You will then randomly pick a new direction, take a step, and so on, for a total of $N_{step}$ steps.  
# 
# ### 2.1
# &#9989;&nbsp; **Start by making a `step2d()` function that returns an integer that is 0,1,2, or 3 (left, right, up, down).**

# In[ ]:


# your code here


# ### 2.2
# 
# **Start at x=0,y=0, and run for 1000 steps, while keeping track of the trajectory.  Plot the result as x versus y.**  Do this a few times and see how it changes! 

# In[ ]:


# your code here


# Now plot the x and y values versus time, individually. 

# In[ ]:


# your code here


# How do these curves compare to the results of your 1D random walk?

# <font size="+3">&#9998;</font> *Put answer here.*

# -----
# ### Congratulations, we're done!
# 
# Now, you just need to submit this assignment by uploading it to the course <a href="https://d2l.msu.edu/">Desire2Learn</a> web page for today's submission folder (Don't forget to add your names in the first cell).
# 

# &#169; Copyright 2018,  Michigan State University Board of Trustees
