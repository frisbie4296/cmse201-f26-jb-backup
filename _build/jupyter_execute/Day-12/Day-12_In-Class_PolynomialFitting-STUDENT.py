#!/usr/bin/env python
# coding: utf-8

# # Day 12 In-Class Assignment: Linear regression and polynomial fitting
# ---

# ### <p style="text-align: right;"> &#9989; Put your name here.</p>
# 
# #### <p style="text-align: right;"> &#9989; Put your group member names here.</p>

# <img src="https://upload.wikimedia.org/wikipedia/commons/8/8b/Moore%27s_Law_Transistor_Count_1971-2018.png" alt="Moore" border="0" width=800px>
# 
# Data from https://en.wikipedia.org/wiki/Moore%27s_law

# ## Fitting data and making predictions
# 
# Moore's law is often used to describe the ever-increasing power of computational hardware.  But what does it describe exactly?  
# 
# Moore's law is not a law, but an observation, dating back to the 1960's when Gordon Moore predicted that the number of transistors on a microprocessor would double every year.  This was later revised slightly in the 70s to a doubling every two years.
# 
# In this assignment we're going to examine Moore's Law using a dataset of transistor counts, number of cores, and clock speeds of CPUs released from the 1970s to 2019.
# 
# The **learning goals** of the assignment are to:
# 
# * Practice fitting data using the functions provided to you by the NumPy python package.
# * Using your model and fit to the data, explore how well your model can predict the future.
# 
# ## Assignment instructions
# 
# Work with your group to complete this assignment. Instructions for submitting this assignment are at the end of the notebook. The assignment is due at the end of class.

# ---
# ## Loading and viewing the data
# 
# Download the zip file `microprocessor-trend-data-master.zip` from the course website and unzip it.  Today we will use the files in the folder `microprocessor-trend-data-master/48yrs`.  Make sure the following files are accessible to this notebook by copying them to your working directory, or by uploading them to JupyterHub:  `transistors.dat`, `frequency.dat` and `cores.dat`.
# 
# "Transistors" is the number of transistors on a chip, which we can use to examine Moore's law directly.
# 
# "Frequency" is the clock speed of the processor in MHz.
# 
# "Cores" is the number of cores on a chip.
# 
# &#9989;&nbsp; **Task**: Look at these files in a text editor (e.g. TextEdit on Mac or Notepad on Windows) to examine their structure.  Load the data into numpy arrays.  You should have **six** numpy arrays after loading: `core_date`, `core_data`, `freq_date`, `freq_data`, `trans_date`, `trans_data`.

# In[ ]:


# Put your code here


# &#9989;&nbsp; **Task**: Below, plot each of these datasets vs time using three separate plots, with a linear scale for the y-axis.  Use symbols instead of lines and be sure to label the axes!

# In[ ]:


# Put your code here


# &#9989;&nbsp; **Task**: What do you observe from this data?

# / your response here /

# &#9989;&nbsp; **Task**: Plot these again using a log scale for the y axis.

# &#9989;&nbsp; **Task**: What are some additional observations you can make that were hidden in the linear-scale plots?

# / your response here /

# ---
# ## Linear Regression
# 
# As a first pass, your goal is to produce a fit to the data using a linear model using `np.polyfit` and `np.poly1d`. You should be familiar with these from today's pre-class assignment.
# 
# &#9989;&nbsp; **Task**: Separately, create a linear fit to each of the three datasets using `np.polyfit`. **Make a plot of the data along with the best fit line**. What are the parameters for your best fit? **Print out those parameter values**. 

# In[ ]:


# Put your code here


# ---
# ### Measuring goodness of fit
# 
# Now we're going to write a function that takes in our data, as well as our fit model, and returns the **root mean squared error**, or RMSE.  The RMSE is defined as:
# 
# \begin{equation}
# RMSE = \sqrt{\frac{1}{N} \sum_{i=1}^{N} \left( y_i - \hat{y_i} \right)^2}
# \end{equation}
# 
# where $y_i$ is a given data point, and $\hat{y_i}$ is the value of that point predicted by the model.
# 
# **A perfect model would have an RMSE of 0, since it would predict each data point with zero error.**
# 
# &#9989;&nbsp; **Task**: Complete the following function that computes the RMSE given a model and a set of data points.  **Note: the "model" is a function, such as that returned by `np.poly1d`.**

# In[ ]:


def rmse(x_points,y_points,model):
    """
    A function for computing the RMSE of a model, based on a set of points.
    
    Input:
    x_points  : array
                A set of x points (e.g. times) that correspond to the data points, y

    y_points  : array
                A set of y points (e.g. transistor counts) that correspond to the times
                x
                
    model     : function
                A model that takes in an x value and returns a y value
                
                
    Output:
    rmse      : float
                The root mean squared error of the model, computed using x and y
    """
    
    nx = len(x_points)
    ny = len(y_points)
    
    if nx != ny:
        print("Error! x and y must have the same length!")
        
    sum_sq = 0
    for i in range(len(x_points)):
        sum_sq += # complete this line!
        
    rmse = np.sqrt(sum_sq/nx)
    
    return rmse


# &#9989;&nbsp; **Task**: Now test out the function using the linear model below:

# In[ ]:


x = np.array([0,1,5,10,22])
y = np.array([-3,7,40,77,132])
params = np.polyfit(x, y, 1)
my_model = np.poly1d(params)

print("The RMSE of this model is:",rmse(x,y,my_model))
print("The RMSE of this model should be:",7.362174877644251)


# ---
# ### Higher order fitting
# 
# &#9989;&nbsp; **Task**: Now let's fit the transistor data with higher order polynomial functions (e.g. second order ($n=2$), third order ($n=3$), etc), using $n = 1,2,3,...,10$. For each order, compute the RMSE.  ***Then make a plot of RMSE vs. n.***

# In[ ]:


# Put your code here


# &#9989;&nbsp; **Task**: How does increasing the order of fit change the RMSE?

# / your answer here /

# &#9989;&nbsp; **Task**: Plot the 10th order fit against the transistor data on both the linear and log scales.

# In[ ]:


# your code here


# &#9989;&nbsp; **Task**: How does the 10-th order fit perform in the early years?  For the late years?  How do you think this fit could be improved?

# / your answer here /

# ---
# ## Predicting a new law for the number of processors (Time permitting)
# 
# As you saw above, there is another trend emerging for the number of processors that a given CPU has.  Before 2005, all processors were single-core.
# 
# &#9989;&nbsp; **Task**: Make a mask to create a subset of the cores data for years 2005 or later.

# In[ ]:


# Put your code here


# &#9989;&nbsp; **Task**: Fit this to functions with orders ranging from 1 to 5.  Record the RMSE for each model.

# In[ ]:


# your code here


# &#9989;&nbsp; **Task**: Plot the data, as well as the fit, for each of the five models.  Be sure to include a legend!

# In[ ]:


# Put your code here


# &#9989;&nbsp; **Task**: Make another masked dataset that also excludes the two datapoints with values greater than 200.

# In[ ]:


# Put your code here


# &#9989;&nbsp; **Task**: Give this the same treatment: fit to orders 1 through 5, save the models in a list, then loop through and use each model to plot a fit curve.

# In[ ]:


# Put your code here


# &#9989;&nbsp; **Task**: How did getting rid of those two points affect the fitted curves?

# / your answer here /

# ## Congratulations, you're done!
# 
# Submit this assignment by uploading your notebook to the course Desire2Learn web page.  Go to the "In-Class Assignments" folder, find the appropriate submission link, and upload everything there. Make sure your name is on it!

# &#169; Copyright 2021,  Michigan State University Board of Trustees

# In[ ]:




