#!/usr/bin/env python
# coding: utf-8

# # Bootcamp 6: Matplotlib
# This notebook includes some basic examples of for using matplotlib!

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import math
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


'''a basic plot example'''

x_values = np.linspace(0,4*math.pi,100) # write a comment to explain what this line is doing
y_values = np.cos(x_values) # write a comment to explain what this line is doing

plt.plot(x_values,y_values,label='my function') # write a comment to explain what this line is doing
plt.xlabel('x') # write a comment to explain what this line is doing
plt.ylabel('y') # write a comment to explain what this line is doing
plt.title('x vs. cos(x)') # write a comment to explain what this line is doing
plt.legend(loc='best') # write a comment to explain what this line is doing
plt.grid() # write a comment to explain what this line is doing
plt.tight_layout() # write a comment to explain what this line is doing


# In[ ]:


'''an example with plt.subplot()'''

x_values = np.linspace(0,4*math.pi,100) 
y_values = np.cos(x_values)
y2_values = x_values**2
y3_values = 2*x_values+1

plt.figure(1, figsize=(6,10)) # write a comment to explain what this line is doing
plt.subplot(3,1,1) # write a comment to explain what this line is doing
plt.plot(x_values,y_values,label='cos(x)',color='green',marker='o') # write a comment to explain what this line is doing
plt.xlabel('x') 
plt.ylabel('y') 
plt.legend(loc='lower center') # write a comment to explain what this line is doing

plt.subplot(3,1,2) # write a comment to explain what this line is doing
plt.plot(x_values,y2_values,label='x**2',color='blue',linestyle='--') # write a comment to explain what this line is doing
plt.xlabel('x') 
plt.ylabel('y')
plt.legend(loc='upper left') # write a comment to explain what this line is doing

plt.subplot(3,1,3) # write a comment to explain what this line is doing
plt.plot(x_values,y3_values,label='2*x+1',color='blueviolet',linestyle='-.',linewidth=4) # write a comment to explain what this line is doing
plt.xlabel('x') 
plt.ylabel('y') 
plt.legend(loc='lower right',fontsize=12) # write a comment to explain what this line is doing

plt.tight_layout()


# ## Task
# 
# Using the array of values below, calculate the sin(values) and then plot them using matplotlib. Make sure to include axis labels, a title, and a legend. Experiment with the colors, markers, line style, and linewidth.

# In[ ]:


# put your code and pseudocode here

x_for_sin = np.arange(0,6*np.pi,0.2) # write a comment to explain what this line is doing


# ## Task
# 
# 1. Write a function to calculate $y=ax^2+bx+c$
# 2. Using your function, calculate values for three different sets of a,b,c values. You may also use different x-values for each set if you choose.
# 3. Using plt.subplot(), plot the three results, each in different plot. Make sure to include a axis labels, a title, and a legend. Vary the colors, markers, line widths, etc. until you have a plots you like the look of!
# 4. Save your plot when you are done!

# In[ ]:


# Put your pseudocode and code here



# In[ ]:




