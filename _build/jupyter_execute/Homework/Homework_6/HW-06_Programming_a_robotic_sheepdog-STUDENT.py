#!/usr/bin/env python
# coding: utf-8

# # Homework 6: Programming a Robotic Sheepdog (Extra Credit)
# 
# <img src="https://cmse.msu.edu/sites/_cmse/assets/Image/image002.jpg"
#      alt="CMSE Grapical Image"
#      align="right" 
#      height="82" 
#      width="82" />
# 
# 
# 
# In this homework you will continue to learn about agent-based modeling, by developing and implementing a set of rules for how agents (sheep, sheepdog) interacts with each other.  We will measure its effectiveness and compare different sets of rules to each other.  Make sure to use Slack and help room hours if you run into issues!
# 
# ___

# ## Goals
# 
# ### By the end of the homework assignment you will have practiced:
# 
# 1. Modeling a real world scenario.
# 2. Building and manipulating agent-based models.
# 3. Assessing model outcomes.
# 4. Defining functions to check the state of a model
# 

# ## Assignment instructions
# 
# Work through the following assignment, making sure to follow all of the directions and answer all of the questions.
# 
# **This assignment is due at 11:59pm on Friday, April 29th.** It should be uploaded to D2L in the approach "Homework" submission folder.  Submission instructions can be found at the end of the notebook as well.

# ## Grading
# 
# * Academic Integrity (1 points)
# * Question 1: Scattering sheep (3 points)
# * Question 2: These sheep were made for walkin' (10 points)
# * Question 3: All bark and no bite (12 points)
# * Question 4: Go dog go (11 points)
# * Question 5: Test for success (8 points)
# 
# Total points possible: **45**
# ___

# ---
# # Academic integrity statement (1 point)
# 
# In the markdown cell below, put your personal academic integrity statement (composed during the Day04 In-Class Assignment). By including this statement, you are confirming that the work you submit in the assignment is wholly your own.  

# <font size=6 color="#009600">&#9998;</font> *Put your personal academic integrity statement here.*

# # Introduction
# 
# An agent-based model is a model where a set of agents interact according to a set of rules.  This is a general framework that can model many different phenomena. Here we will use a 2D grid, where the cells are given numbers to represent one of the following:
# 
# * 0 = empty space
# * 1 = fence
# * 2 = sheep
# * 3 = dog
# 
# The fence forms a pen where the sheep need to sleep every night.  However, the sheep don't always like to go to the pen, and would rather stay up past their bedtime.
# 
# One particular farmer (you) has come up with a 21st century solution: **a robotic sheepdog**.  This dog will help round up the sheep and get them into their pen at night.  One problem is that we're not sure the best way to program this robot in order to get the sheep into the pen as fast as possible.
# 
# ---
# 
# Let's get started by defining our grid:

# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np

nx = 40
ny = 40
fenceline = 10

states = ['empty','fence','sheep','dog']
state_color = np.linspace(0,1,len(states))

system_state = np.zeros([ny,nx]) # intialize everything to empty

dog_start_pos = [int(ny-1),int(nx/2)]
system_state[dog_start_pos[0],dog_start_pos[1]] = 3  # put a dog at the top, in the middle
system_state[fenceline,:] = 1                 # put a fence along y = 10
system_state[fenceline,17:24] = 0             # put a hole in the fence


# Now lets define a function to plot our state, using symbols for the fence, the dog and the sheep.

# In[ ]:


def plotstate(state,time=0):
    
    # first create two vectors based on the x and y sizes of the grid
    x_range = np.linspace(0, state.shape[0], state.shape[0]) 
    y_range = np.linspace(0, state.shape[1], state.shape[1])
    
    # use the numpy meshgrid function to create two matrices 
    # of the same size as myarray with x and y indexes
    x_indexes, y_indexes = np.meshgrid(x_range, y_range)
    
    # make a list of all the x and y indexes that are not empty.
    fence_x = x_indexes[state == 1];
    fence_y = y_indexes[state == 1]; 
    sheep_x = x_indexes[state == 2]; 
    sheep_y = y_indexes[state == 2];
    dog_x = x_indexes[state == 3]; 
    dog_y = y_indexes[state == 3];
 
    # plot the squares and triangles.  make the size of the polygons 
    # larger than the default so they're easy to see!   
    plt.plot(fence_x,fence_y, 's',markersize=20)  
    plt.plot(sheep_x,sheep_y, 'o',markersize=20)  
    plt.plot(dog_x,dog_y, '1',markersize=20)
    
    # Set the x and y limits to include half a space overlap so we don't cut off the shapes
    plt.ylim([-0.5,state.shape[0] + 0.5]) 
    plt.xlim([-0.5,state.shape[0] + 0.5])
    
    # display the current time on the plot
    plt.text(0,0,"time={0}".format(time),fontsize=18)
    
    # Turn the axes off
    plt.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False)
    plt.gca().set_aspect('equal', adjustable='box')


# In[ ]:


plt.figure(figsize=(10,10))
plotstate(system_state)


# Doesn't really look like a dog, but let's use our imaginations.  We're almost ready, but we're missing something.... oh yes. The sheep.

# ## Question 1:  Scattering sheep (3 points)
# 
# Write a function that randomly places the sheep in the field above the fence.  It should take as an argument the `system_state`, the number of sheep to place (`N`), and a `fenceline` parameter that describes the y-position of the fence.  It should return a new state with the sheep. 
# 
# **Importantly,** the sheep cannot overlap with anything that is not empty space (i.e. `state[try_y,try_x]` must equal zero), and the sheep must be placed above the fenceline!
# 
# **Review the code below. At each empty comment (there are three, denoted by ??), write a comment that describes what the chunk of code directly below it is supposed to be doing.**

# In[ ]:


from copy import copy

def place_sheep(state,N,fenceline):
    
    newstate = copy(state)
    
    sheep_placed = 0
    
    while ?? :# sheep_placed condition
        # suggest somewhere for a sheep to be placed 
        try_x = np.random.randint(state.shape[1])
        try_y = np.random.randint(state.shape[0])
        
        # check if this is appropriate.  
        # if yes, set good_place to True.  if no, set good_place to False.
        if ??:
            good_place = True
        else:
            good_place = False
            
        # if good, place the sheep, if not try again
        if good_place is True:
            # update sheep_placed and assign sheep to the newstate.
            get_ipython().show_usage()
    
    return newstate


# Let's call this state `initial_state` since we'll use it to start our agent-based model simulations.  The following should plot your new system.  Run it a few times and make sure it always gives you something appropriate.

# In[ ]:


initial_state = place_sheep(system_state,20,fenceline)
plt.figure(figsize=(10,10))
plotstate(initial_state)


# ## Question 2:  These sheep were made for walkin' (10 points)
# 
# Of course these sheep aren't going to just stand there.  They will move, randomly over time.  For each time step (say, 1 second), let's say they will move according to the following probabilities and rules:
# 
# ```
# - choose to move with probability p_move
# - if moving 
#      - choose direction (up, down, left, right) with equal probability
#      - do not execute the move if it goes beyond the borders
#      - only execute the move if the new space is empty
#      - do not execute an upward move if sheep is at the fenceline
# ```
# Where the latter condition assumes that once the sheep are in the pen, they remember how good it feels to be home.
# 
# ### 2.1 Task (4 points)
# **Write a function** that takes in: 1) a system state, 2) a sheep's x and y position, 3) p_move and 4) the fenceline.  Have this function attempt to move the specified sheep according to the rules above.
# 
# **Review the code below. At each empty comment (there are three, denoted by ####), write a comment that describes what the chunk of code directly below it is supposed to be doing.**

# In[ ]:


def move_sheep(state,sheep_x,sheep_y,pmove,fenceline):

    # decide whether to move
    r1 = np.random.random()
    if r1 < pmove:
        # if yes, decide to move up, down, left or right
        # store the new location in the variables try_x and try_y

        r2 = np.random.random()
        
        if #### : # move left
            #### # update sheep position
            
        elif r2 < 0.5: # move up
            
            if #### fenceline condition
                #### # update sheep position
            else:
                #### # update sheep position
                
        elif #### : # move right
            #### # update sheep position
            
        else: # move down
            #### # update sheep position
            
        # check and see if the move is good
        good_move = True
        
        # set good_move to False if conditions are violated
        
        if #### # position conditions:
            good_move = False
            
        elif #### # position conditions:
            good_move = False
            
        elif #### # position conditions:
            good_move = False
            
        # if the move is good, make the move
        if good_move is True:
            # make the move
            state[sheep_y,sheep_x] = 0
            state[try_y,try_x] = 2
    
    # return the state
    return state


# Great!  Now let's write a function to move the whole system forward in time.  This will use the `move_sheep` function.  First we need to find all the sheep.  This can be done easily with the `np.where` function.  You might not have seen this before, so read the doc page before you use it.  

# In[ ]:


sheep_loc = np.array(np.where(initial_state==2))


# ### 2.2 Task (2 points)
# 
# **What is `sheep_loc`?  What do the first and second axes represent?**

# <font size=6 color="#009600">&#9998;</font> *Answer here*

# ### 2.3 Task (2 points)
# **Use `sheep_loc` below to get the x and y position of the first sheep:**

# In[ ]:


# your code here


# ### 2.4 Task (2 points)
# **Use `sheep_loc` to get the total number of sheep:**

# In[ ]:


# your code here


# Now we use `sheep_loc` to finish the `evolve_system` function below, which will (at least try to) move all of the sheep.

# In[ ]:


def evolve_system(state,pmove,fenceline):
    sheep_loc = np.array(np.where(state==2))
    
    # determine how many sheep there are
    nsheep = len(sheep_loc[0])
    
    # write a loop to iterate over each sheep
    for i in range(nsheep):
        sheep_x = sheep_loc[1][i]
        sheep_y = sheep_loc[0][i]
        # call move_sheep for each sheep_x and sheep_y position
        state = move_sheep(state,sheep_x,sheep_y,pmove,fenceline)

    return state


# OK, now we'll test out our code:

# In[ ]:


from copy import copy
from IPython.display import display, clear_output
import time 

nsteps = 20
pmove = 0.5
fenceline = 10

state = copy(initial_state)

fig = plt.figure(figsize=(8,8))
for i in range(nsteps): 
    state = evolve_system(state,pmove,fenceline)
    plotstate(state,time=i)
    time.sleep(0.01)         # Sleep for 0.01 s to slow down the animation
    clear_output(wait=True) # Clear output for dynamic display
    display(fig)            # Reset display
    fig.clear()             # Prevent overlapping and layered plots

plt.close()                 # Close dynamic display


# Wow!  Just... wow.
# 
# ---

# ## Question 3:  All bark and no bite (12 points)
# 
# Now we need some sheep-sheepdog interaction.  Time to make some changes to our ruleset:
# 
# ```
# - choose to move with probability p_move
# - if moving
#      - choose x dir or y dir with equal probability
#      - choose toward dog or away from dog as follows
#          * p = 0.5 - delta (towards dog)
#          * p = 0.5 + delta (away from dog)
#      - do not execute the move if it goes beyond the borders
#      - only execute the move if the new space is empty
#      - do not execute an upward move if sheep is at the fenceline
# ```
# where we've introduced another parameter `delta` which can take on values between 0 and 0.5.

# ### 3.1 Task (4 points)
# 
# **Use `move_sheep` function from question 2 to make a new `move_sheep_bias` function that accounts for the dog's position:**

# In[ ]:


def move_sheep_bias(state,sheep_x,sheep_y,pmove,fenceline,delta):

    # your code here


# ### 3.2 Task (4 points)
# **Write an `evolve_system_bias` function to call this with the delta parameter:**

# In[ ]:


def evolve_system_bias(state,pmove,fenceline,delta):
    # your code here


# Then test our code again, this time only plotting every 10 steps:

# In[ ]:


from IPython.display import display, clear_output
import time 

nsteps = 500
plot_every = 10
pmove = 0.5
fenceline = 10
delta = 0.25

state = copy(initial_state)

fig = plt.figure(figsize=(8,8))
for i in range(nsteps): 
    state = evolve_system_bias(state,pmove,fenceline,delta)
    if i % plot_every == 0:
        plotstate(state,time=i)
        time.sleep(0.01)         # Sleep for 0.01 s to slow down the animation
        clear_output(wait=True) # Clear output for dynamic display
        display(fig)            # Reset display
        fig.clear()             # Prevent overlapping and layered plots

plt.close()                 # Close dynamic display


# Maybe a little too intense.  I don't think our dog should be that scary.  
# 
# ### 3.3 Task (4 points)
# **Add a cutoff distance (`d_cut`), where if sheep are closer to the dog than `d_cut` then they use `move_sheep_bias`, but if they are farther then they move normally with `move_sheep`.**
# 
# Note: calculate distance as $d = \sqrt{(x_s - x_d)^2 + (y_s - y_d)^2}$, where $x_s$ is the x-position of the sheep, and $x_d$ is the x-position of the dog, etc.

# In[ ]:


def evolve_system_bias_cutoff(state,pmove,fenceline,delta,dcut):
    # find the dog
    dog_loc = np.array(np.where(state==3))
    dog_x = dog_loc[1][0]
    dog_y = dog_loc[0][0]
    
    sheep_loc = np.array(np.where(state==2))
    
    # determine how many sheep there are
    nsheep = len(sheep_loc[0])
    
    # write a loop to iterate over each sheep
    for i in range(nsheep):
        
        # your code here
        
    return state


# In[ ]:


nsteps = 500
plot_every = 10
pmove = 0.5
fenceline = 10
delta = 0.25
dcut = 15

state = copy(initial_state)

fig = plt.figure(figsize=(8,8))
for i in range(nsteps): 
    state = evolve_system_bias_cutoff(state,pmove,fenceline,delta,dcut)
    if i % plot_every == 0:
        plotstate(state,time=i)
        time.sleep(0.01)         # Sleep for 0.01 s to slow down the animation
        clear_output(wait=True) # Clear output for dynamic display
        display(fig)            # Reset display
        fig.clear()             # Prevent overlapping and layered plots

plt.close()                 # Close dynamic display


# That's better.

# ## Question 4:  Go dog go (11 points)
# 
# Here's the chance we've been waiting for!  Time to make our dog move.  But how?  We'll assume our robot can move much faster than the sheep, so we'll allow it to move one square every timestep.  
# 
# **But how should it move?**  To allow us to try out a set of different strategies, we'll assume we have a path that the dog follows, which is a list of states that are no more than one square apart.

# In[ ]:


y0,x0 = dog_start_pos
short_dog_path = [(y0,x0),(y0,x0-1),(y0,x0-2),(y0,x0-1)]


# ### 4.1 Task (1 points)
# **How many states are in this path?  What does this path describe?**

# <font size=6 color="#009600">&#9998;</font> *Answer here*

# ### 4.2 Task (4 points)
# **Make a path where the dog runs all the way to the left wall, then all the way to the right wall, and then back to its starting position.**  Do this by filling in the missing lines below:

# In[ ]:


dog_path = [(y0,x0)]
x = x0
y = y0

# first run to the left wall
while ?: 
    # update x
    x = x - 1
    
    # append (x,y) tuple to dog_path
    get_ipython().show_usage()

# then run to the right wall
while ?:
    # update x
    get_ipython().show_usage()
    
    # append (x,y) tuple to dog_path
    get_ipython().show_usage()
    
# then run back to the middle
while ?:
    # update x
    get_ipython().show_usage()
    
    # append (x,y) tuple to dog_path
    get_ipython().show_usage()


# Remember the dog can't move more than one square per loop, and since the dog will be running this loop over and over again (until the sheep are in the pen), we need to check the endpoints as well.  **Run this function below to see if your path is a good one:**

# In[ ]:


def pathcheck(path):
    # checks to see if the dog moves more than one square per timestep
    oldp = path[-1]
    goodpath = True
    for p in path:
        dy = p[0]-oldp[0]
        dx = p[1]-oldp[1]
        if abs(dx) + abs(dy) > 1:
            goodpath = False
        oldp = p
    return goodpath


# In[ ]:


pathcheck(dog_path)


# ### 4.3 Task (3 points)
# OK, now we'll make a `move_dog` function that uses this path:
# **Review the code below. At each empty comment (there are three, denoted by ???), write a comment that describes what the chunk of code directly below it is supposed to be doing.**

# In[ ]:


def move_dog(state,path,current_pos):
    
    next_pos = current_pos + 1
    # check if the next position is occupied
    get_ipython().run_line_magic('pinfo2', '?')
    
    next_y,next_x = path[next_pos]
    
    if ???:# empty!  or the dog is already there. 
        # Either way, its ok to move the dog
    
        # find the dog
        get_ipython().run_line_magic('pinfo2', '?')
    
        # delete dog from current position
        get_ipython().run_line_magic('pinfo2', '?')
        
        # add dog to next position
        get_ipython().run_line_magic('pinfo2', '?')
        
        # update current_pos
        get_ipython().run_line_magic('pinfo2', '?')
    
    return current_pos, state


# Now let's add this `move_dog` command to a new `evolve_system` function:

# In[ ]:


def evolve_system_dog(state,pmove,fenceline,delta,dcut,path,current_pos):
    state = evolve_system_bias_cutoff(state,pmove,fenceline,delta,dcut)        
    current_pos, state = move_dog(state,path,current_pos)

    return current_pos, state


# Let's test it out!

# In[ ]:


nsteps = 500
plot_every = 10
pmove = 0.5
fenceline = 10
delta = 0.25
dcut = 15
path = dog_path
dog_pos = 0

state = copy(initial_state)

fig = plt.figure(figsize=(8,8))
for i in range(nsteps): 
    dog_pos, state = evolve_system_dog(state,pmove,fenceline,delta,dcut,path,dog_pos)
    if i % plot_every == 0:
        plotstate(state,time=i)
        time.sleep(0.01)         # Sleep for 0.01 s to slow down the animation
        clear_output(wait=True) # Clear output for dynamic display
        display(fig)            # Reset display
        fig.clear()             # Prevent overlapping and layered plots

plt.close()                 # Close dynamic display


# ### 4.4 Task (2 points)
# **Run this code for 5000 steps, with `plot_every` = 100, and for 20000 steps, with `plot_every` = 400**

# In[ ]:


# your code here


# In[ ]:


# your code here


# ### 4.5 Task (1 points)
# **What do you observe?**

# <font size=6 color="#009600">&#9998;</font> *Answer here*

# ## Question 5: Test for success (8 points)
# 
# OK our sheepdog is not very effective right now.  Let's quantify exactly how bad it is.  Write a function that will check and see how many sheep are out of the pen (return an integer):

# In[ ]:


def sheep_still_out(state,fenceline):
    # return the number of sheep that are above the fenceline
    # in the current state
    
    # code here
    sheep_still_out = 0
    sheep_loc = np.array(np.where(state==2))
    nsheep = len(sheep_loc[0])
    
    for i in range(nsheep):
        sheep_y = sheep_loc[0][i]
        if sheep_y > fenceline:
            sheep_still_out += 1

    return sheep_still_out


# ### 5.1 Task (2 points)
# **Test this function to see how many are out of the pen in the initial and final states from above:**

# In[ ]:


# your code here


# Now let's use this function in a `while` loop to see how long it will take:

# In[ ]:


pmove = 0.5
fenceline = 10
delta = 0.25
dcut = 15
path = dog_path
dog_pos = 0
report_every = 1000

state = copy(initial_state)

i = 0
while (sheep_still_out(state,fenceline) > 0):
    i += 1
    dog_pos, state = evolve_system_dog(state,pmove,fenceline,delta,dcut,path,dog_pos)
    if i % report_every == 0:
        print("At time = {0} there are {1} sheep still out".format(i,sheep_still_out(state,fenceline)))

print("All sheep in the pen at time = {0}".format(i))


# ### 5.2 Task (4 points)
# **Put the above code in a `for` loop, and run this simulation 10 times.  Save the times in a list called `times`.** 

# In[ ]:


# your code here


# **Run the cell below to get statistics of your sheepdog.**

# In[ ]:


from math import sqrt
a = np.array(times)
print("It takes an average of {0} +- {1} s for this sheepdog to work".format(a.mean(),a.std()/sqrt(len(times))))


# ### 5.3 Task (2 points)
# **What quantity is being reported after the +- signs?**

# <font size=6 color="#009600">&#9998;</font> *Answer here*

# ---
# 
# ### Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "Homework Assignments" section, find the submission folder link for Homework #6, and upload it there.

# &#169; Copyright 2022, [Department of Computational Mathematics, Science and Engineering](https://cmse.msu.edu) at Michigan State University.

# In[ ]:




