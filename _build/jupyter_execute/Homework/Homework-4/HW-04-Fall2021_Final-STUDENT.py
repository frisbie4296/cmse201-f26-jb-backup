#!/usr/bin/env python
# coding: utf-8

# # Homework 4: Fitting data using NumPy and SciPy

# # __CMSE  201 &ndash; Fall 2021__
# 
# <img src="https://cmse.msu.edu/sites/_cmse/assets/Image/image002.jpg"
#      alt="CMSE Logo"
#      align="right" 
#      height="100" 
#      width="100" />

# ### <p style="text-align: right;"> &#9989; Put your name here</p>

# ## Goals
# 
# ### By the end of the homework assignment you will have practiced:
# 
# 1. Loading in data
# 2. Polynomial fitting using NumPy
# 3. Fitting curves using SciPy
# 4. Plotting data and the correspoding best-fit results
# 5. Calculating residuals when fitting a models to data

# ## Assignment instructions
# 
# Work through the following assignment, making sure to follow all of the directions and answer all of the questions.
# 
# **This assignment is due at 11:59pm on Friday, Nov 5th.** 
# 
# It should be uploaded to D2L in the approach "Homework" submission folder.  Submission instructions can be found at the end of the notebook as well.

# ## Grading
# 
# - Academic Integrity (1 pt)
# - Part 1 (20 pts)
# - Part 2 (24 pts)
# 
# **Total:** 45 pts
# 

# ---
# # Academic integrity statement (1 point)
# 
# In the markdown cell below, put your personal academic integrity statement (composed during the Day04 In-Class Assignment). By including this statement, you are confirming that the work you submit in the assignment is wholly your own.  

# <font size=6 color="#009600">&#9998;</font> *Put your personal academic integrity statement here.*

# ---
# ## Part 1: Fitting Piece-wise Linear Functions to Data
# In this problem, we will look at fitting more unusual functions to data.
# 
# ### &#9989;&nbsp; Question 1.1: Setting up your Python modules (2 points)
# 
# In this homework, you will be mainly using Matplotlib, Pandas, NumPy, and SciPy's `curve_fit` function. Make sure to include all of the important `import` comments here.

# In[ ]:


# Load needed modules here


# ### Question 1.2: Generate and Plot Data (4 points)
# 
# #### &#9989;&nbsp; Question 1.2.1: Generating Piece-Wise Data Set (1 point)
#  
# Consider a function $y=f(x)$ such that:
# 
# \begin{eqnarray}
# f(x) &=& 2x \quad &\mathrm{for}& \quad 0 \leq x \leq 0.5 \\ 
# f(x) &=& 3-4x \quad &\mathrm{for}& \quad 0.5 \leq x \leq 1 
# \end{eqnarray}
# 
# **Create a set of 200 $x$ values that spans from $x = $ 0 to 1** (*Hint: consider using `np.linsapce`*). **Then use these $x$ values to create a set of $y$ values that follow the function $f(x)$ given above.**

# In[ ]:


# Put your code here


# #### &#9989;&nbsp; Question 1.2.2: Plotting Piece-Wise Data Set (1 point)
# 
# **Plot the $x$ and $y$ values generated in the previous problem. Label all axes on the plots.**

# In[ ]:


# Put your code here


# #### &#9989;&nbsp; Question 1.2.3: Adding Noise and Plotting (2 points)
# 
# **Generate a noisy version $y$ by adding Gaussian noise (I.e., `np.random.normal`) with mean zero and standard deviation 0.2 to all of the $y$ values from this function. (Essentially, make $y_{noisy} = f(x) \, + $ Gaussian($x$)). Plot the noisy data (versus $x$ values) in a new plot. Label all axes on the plots.**

# In[ ]:


# Put your code here


# ---
# ### 1.3: Polynomial Fitting (5 points)
# 
# #### &#9989;&nbsp; Question 1.3.1: Thinking about Fitting Piece-Wise Functions (1 point)
# 
# How would you use NumPy's `polyfit` and `poly1d` functions to fit a model like $f(x)$ (i.e., polynomial in two pieces) to the corrupted or noisy data? Explain your approach. Your answer should use only first order polynomials for this. *Hint: You may fit more than one polynomial to this type of data.*

# <font size=+3>&#9998;</font> *Put your explanation here.*

# #### &#9989;&nbsp; Question 1.3.2: Fitting Piece-Wise Functions (3 points)
# 
# Turn your plan above into code; **use the `polyfit` and `poly1d` functions to fit a model to the data. Make sure to print out the best fit parameters.**

# In[ ]:


# Put your code here


# #### &#9989;&nbsp; Question 1.3.3: Plotting the Best Fit Function (1 point)
# 
# **Plot the data together with the best fit model**. Include a legend to make it clear what information represents the data and what information represents the best fit. 

# In[ ]:


# Put your code here


# ---
# ### Question 1.4: Using Curve Fit for the data (8 points)
# 
# #### &#9989;&nbsp; Question 1.4.1: Writing the Function (3 points)
# **Write a function called `fitting_function`.** The function should:
# 1. Take the arguments: `x`, `m_1`, `b_1`, `m_2`, `b_2`, where `x` is a NumPy array and the rest are all fit parameters corresponding to the slopes of the lines/pieces and their intercepts. 
# 2. Return an array with values $f(x) = m_1*x + b_1$ when $0 \leq x \leq 0.5$ and $f(x) = m_2*x + b_2$ where $0.5 \leq x \leq 1$.

# In[ ]:


# Put your code here


# #### &#9989;&nbsp; Question 1.4.2: Fitting the Function and Plotting the Results (4 Points)
# 
# **Use SciPy's `curve_fit` function to find the best fit model parameters for the corrupted data using your `fitting_function`. Plot the data and the best fit. Label all axes and include a legend. Also print the resulting parameters.**

# In[ ]:


# Put your code here


# ---
# ## Part 2: Fitting Models to Real Data
# In this problem, we will look at fitting models to a real Wage data. You can download the [data.](https://drive.google.com/file/d/1DMSCODqMuapFHAl1jHnCy7yN-DOuKzQj/view?usp=sharing). You will use your model-fitting skills to see if you can find a good mathematical model for how the data behaves. 
# 
# #### &#9989;&nbsp; Question 2.1: Reading and inspecting the data (2 points)
# 
# Read in the data using Pandas. Print out a few rows of the data as well as the summary statistics of the data (mean, standard deviation, etc.) to get a sense of the data.

# In[ ]:


# Put your code here


# ### Question 2.2: Split the data into training and testing data. (2 points)
# 
# Ultimately the goal of fitting a model to data is so that we can use the model to make ***predictions.*** To help us with this process, we’re going to separate our dataset into two chunks:
# 
# - `wages_test`: a randomly selected sample of 300 data points that we’ll use to test our model.
# - `wages_train`: the rest of our dataset (i.e., everything *not* in `wages_test`), which we’ll use to create our model.
# 
# #### &#9989;&nbsp; Question 2.2.1: Generating `wages_test` (1 point)
# We’ve provided a bit of code below which will generate a set of random numbers. **Use the random numbers to create your `wages_test` dataset.**

# In[ ]:


import random
random.seed(6)
test_id = random.sample(range(2918), 300) 
test_id.sort()
#test_id
# use test_id to generate wage_test and wage_train
# Put your code here


# #### &#9989;&nbsp; Question 2.2.2: Generating `wages_train` (1 point)
# **Use the Pandas function `drop` to create your `wages_train` dataset.**

# In[ ]:


# Put your code here


# ### Question 2.3: Polynomial fitting (3 points)
# 
# #### &#9989;&nbsp; Question 2.3.1: Fitting the Polynomial (2 points)
# 
# **Using the NumPy `polyfit` function, fit a 3rd order polynomial to the `wage_train` data, with age being the predictor and wage being response. Make sure to print out the best fit parameters.** 

# In[ ]:


# Put your code here


# #### &#9989;&nbsp; Question 2.3.2: Plotting the Fit (1 point)
# 
# 
# **Use `poly1d` to plot the data together with the fit model. The plot should label all axes and include legends to make clear what information represents the data and what information represents the fits.** 

# In[ ]:


# Put your code here


# ### &#9989;&nbsp; Question 2.4: Finding and Removing outliers (8 points)
# 
# <img src="https://cdn1.byjus.com/wp-content/uploads/2020/10/Box-Plot-and-Whisker-Plot-1.png" alt="Moore" border="0" width=500px>
# 
# We can determine the quality of the data by computing the *residuals*, $r_i$, as the difference between each known data point $y_i$ and the *expected* $y$ value from the best fit model evaluated at $x_i$, i.e., $$r_i = y_i - f(x_i).$$  
# 
# #### &#9989;&nbsp; Question 2.4.1: Calculating Residuals (1 point)
# 
# **Use the equation above to calculate the residuals.**
# 
# Use residuals to identify outliers, and remove them to make wage_train2. Using wage_wage2 to perform polyfit with degree 3. Use `poly1d` to **plot the data together with the fit models (blue line for fitted model using all the trained data and green line for fitted model for cleaned training data). Label outliers in red **. The plot should label all axes and include legends to make clear what information represents the data and what information represents the fit. 
# 
# 

# In[ ]:


# Put your code here


# #### &#9989;&nbsp; Question 2.4.2: Identifying Outliers (2 points)
# 
# One way to identify outliers is to utilize the same principal as in boxplot above, where data points with:
# 
# \begin{eqnarray}
# r_i &<& Q_1 - 1.5 (Q_3 - Q1) \\
# \mathrm{or} \\
# r_i &>& Q_3 + 1.5 (Q_3 - Q1)
# \end{eqnarray}
# 
# are treated as outliers, where **$Q_1$ and $Q_3$ are the 25% and 75 % quantile of all the residuals.** 
# 
# **Determine the 25% and 75 % quantile of the residuals** (*Hint: You can use either Pandas `describe` function or Pandas `quantile` function for this*). **Use these values to isolate and separate the outliers from the `wages_train` dataset.** 

# In[ ]:


# Put your code here


# #### &#9989;&nbsp; Question 2.4.3: Plotting Outliers (1 point)
# 
# **Make a (scatter) plot showing the data to be kept in one color and the outliers in a different color.**

# In[ ]:


# Put your code here


# #### &#9989;&nbsp; Question 2.4.4: Refitting the Data ( 2 points)
# 
# **Use your cleaned data set (i.e., the one with the outliers removed) and fit it to a new model (once again, use a 3rd order polynomial). Make sure to print out the best fit parameters**

# In[ ]:


# Put your code here


# #### &#9989;&nbsp; Question 2.4.5: Plotting Everything Together ( 1 point)
# 
# **Finally, make a plot showing the following:**
# 1. The cleaned (non-outlier) data points.
# 2. The outlier data points.
# 3. Your original best fit line (i.e., the one fit using all of the `wage_train` data points)
# 4. Your new best fit line (i.e., the one fit using the data set with the outliers removed)
# 
# **Make sure to have a legend that clearly defines each of these components.**

# In[ ]:


# Put your code here


# #### &#9989;&nbsp; Question 2.4.6: Reflecting on your Best Fits ( 1 point)
# 
# **In the space below, comment on the differences between your two best lines (I.e., the one fit with outliers and the one fit without outliers). Are they different from one another? Where do they deviate? Where are they the same? Consider the best parameters in your answer, as well as the best fit lines.**

# <font size=+3>&#9998;</font> *Put your observations here.*

# ### Question 2.5: Calculating the Test Error. (5 point)
# 
# As mentioned previously, the main goal for building a model is to make prediciton for data unseen. We will measure the prediction ability of our model using `wages_test` data set, which has never been seen by our model-fitting procedure. 
# 
# 
# First, we would like to quantify how well our models fit the data. To do this, we will use the aggregate of the residuals, in the form of the **Mean Squared Error** $$MSE=\frac{1}{N}\sum_{i=1}^{N}r_i^2.$$ 
# 
# 
# #### &#9989;&nbsp; Question 2.5.1: Creating a Function to Calculate MSE (2 point)
# 
# **Create a function that:** 
# 1. Takes two numpy arrays; data $y$ values and best-fit model $y$ values 
# 2. Returns Mean Squared Error between the data and the best-fit model values.

# In[ ]:


### Put your code here


# #### &#9989;&nbsp; Question 2.5.2: Calculating MSE (1 point)
# 
# **Use your function from the previous problem, as well as your two best fit functions from 2.3.1 and 2.4.4, and calculate the MSE for each fit using the data from `wage_test`.** 

# In[ ]:


### Put your code here


# #### &#9989;&nbsp; Question 2.5.3: Reflecting on the Best Fit Models (2 points)
# 
# **Which model is better? Explain the reason using your own words.** 

# <font size=+3>&#9998;</font> *Explain your reasoning here.*

# ---
# ## Assignment Wrap-up
# 
# Please fill out the following Google Form before you submit your assignment. **You must completely fill this out in order to receive credit for the assignment!**
# 
# **COMPLETE THIS SURVEY through [this link](https://forms.office.com/r/kGDrV361LB) or through cell below.**

# In[ ]:


from IPython.display import HTML
HTML(
"""
<iframe 
	src="https://forms.office.com/r/kGDrV361LB" 
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
# Submit this assignment by uploading it to the course Desire2Learn web page.  
# Go to the "Homework Assignments" section, find the appropriate submission folder link, and upload it there.
# 

# &#169; Copyright 2020, [Department of Computational Mathematics, Science and Engineering](https://cmse.msu.edu) at Michigan State University.
